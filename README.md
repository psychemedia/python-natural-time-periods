# python-natural-time-periods
Python package for returning time periods corresponding to natural language phrases.

*Original code referenced [here](https://blog.ouseful.info/2016/09/22/natural-language-time-periods-in-python/) and available via [this gist](https://gist.github.com/psychemedia/f17910ef74687b3a062bd403f79e340a).*

## Usage

Install using: `pip3 install --force-reinstall  --upgrade git+https://github.com/psychemedia/python-natural-time-periods.git`


The following period functions are defined:

- `today()`, `yesterday()`, `tomorrow()`
- `last_week()`, `this_week()`, `next_week()`, `later_this_week()`, `earlier_this_week()`
- `last_month()`, `next_month()`, `this_month()`, `earlier_this_month()`, `later_this_month()`
- `day_lastweek()`, `day_thisweek()`, `day_nextweek()`

````
import natural_time_periods as ntpd

ntpd.today()
>>> datetime.date(2017, 8, 9)

ntpd.last_week()
>>> (datetime.date(2017, 7, 31), datetime.date(2017, 8, 6))

ntpd.later_this_month()
>>> (datetime.date(2017, 8, 10), datetime.date(2017, 8, 31))

ntpd.day_lastweek(nt.MON)
>>> datetime.date(2017, 7, 31)

ntpd.day_lastweek(nt.MON, iso=True)
>>> '2017-07-31'
````

## TO DO

Provide an option to return `pandas` period objects.


----

### Related packages

- [DavidAmison/natural_time](https://github.com/DavidAmison/natural_time)
- [TimeConvert](https://github.com/xxx-convert/TimeConvert)
