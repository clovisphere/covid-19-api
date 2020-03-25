from datetime import datetime, timedelta
from markupsafe import escape
from . import api
from .. import db
from ..models import Stat
from ..utils import get_daily_report

@api.route('/stat')
def get_all_stat():
    return Stat.query.get_or_404(1).export_data()

@api.route('/stat/<country_code>')
def get_country_stat(country_code):
    country_code = escape(country_code).upper() # country codes are saved in upper case in db.
    data = Stat.query.get_or_404(1).export_data()
    return { country_code: data[country_code] } if country_code in data else { 'message': f'no data available '+ \
            'for country with ISO Alpha-2 Code: {country_code}' }


def populate_stat_table():
    """called when the app is started to populate the table with initial dataset."""
    period = (datetime.now() - timedelta(1)).strftime('%m-%d-%Y') # yesterday because data CSSE data is in UTC and only updated once daily.
    data = get_daily_report(period)
    if data: # only commit to db if there's new data available
        items = Stat(data=data)
        db.session.add(items)
        db.session.commit()

def update_stat_table(ctx):
    """To auto-update the data every 5 hour."""
    period = (datetime.now() - timedelta(1)).strftime('%m-%d-%Y')
    data = get_daily_report(period)
    if data:
        with ctx.app_context():
            d = Stat.query.get(1)
            d.data = data
            db.session.commit()
