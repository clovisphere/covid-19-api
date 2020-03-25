# COVID-19 API

What if we could use [Flask](https://palletsprojects.com/p/flask/) 
to build a basic [COVID-19](https://www.who.int/emergencies/diseases/novel-coronavirus-2019) API? I thought this 
would be an interesting weekend hack project, and a good way 
to learn both [Python](https://www.python.org/) and [Flask](https://palletsprojects.com/p/flask/) 
the right way - or is it [the hard way](https://www.amazon.com/Learn-Python-Hard-Way-Introduction/dp/0134692888)?

![How to use](screenshot/covid-19-api.gif)

## Important information

This API consumes data made available by 
the good people of [CSSE at Johns Hopkins](https://github.com/CSSEGISandData/COVID-19) - 
all I am doing is transforming the [.csv](https://en.wikipedia.org/wiki/Comma-separated_values) 
data and making it sexier :kissing_closed_eyes:.. So if you wanna thank someone, 
please thank the [CSSE guys](https://systems.jhu.edu/) :clap:, buy them :beers: on my behalf :grinning:

#### Prerequisite
+ [Python](https://www.python.org/downloads/)
+ [Pipenv](https://pipenv.pypa.io/en/latest/)

#### Usage
1. Clone the app

```bash
$ git clone https://github.com/clovisphere/covid-19-api.git
```
2. To bring to life your setup :stars: :rocket:

```bash
$ cd myproject # this repo
$ pipenv --python 3
$ pipenv install
$ pipenv shell
$ ./run.py
```

##### TO BE ADDED: API Documentation

(_work in progress_)

Enjoy :v::sunglasses:
