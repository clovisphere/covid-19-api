#!/usr/bin/env python
import os
import atexit
from app import create_app, db
from app.models import User
from app.api_v1.stat import populate_stat_table, update_stat_table


if __name__ == '__main__':
    app = create_app(os.environ.get('FLASK_ENV', 'development'))
    with app.app_context():
        # TODO: this is ONLY for development, it'd should be removed in PROD.
        db.drop_all()
        db.create_all() 
        # populate statistics table
        populate_stat_table()
        # create test user if user doesn't exit
        if User.query.get(1) is None:
            user = User(username='demo')
            user.set_password('demo')
            db.session.add(user)
            db.session.commit()
    # TODO: some cleanup needed, it's a bit ugly 
    # this for the scheduler, in principle, this should work
    from apscheduler.schedulers.background import BackgroundScheduler
    # initialize scheduler
    scheduler = BackgroundScheduler()
    # add job - hack to pass app.context
    scheduler.add_job(func=update_stat_table, trigger='interval', args=[app], hours=5, id='update_statistics_table')
    # start scheduler
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
    
    # if you reach here, it means the app should start:-)
    app.run()
