from datetime import date
from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
    @classmethod
    def today(cls):
        print('Today is %s' % cls(date.today().isoweekday()).name)

# Now, let's call the `today` method to see the output
Weekday.today()