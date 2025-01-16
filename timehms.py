#Programming Project 4, Eleni Brennan, pledged

class TimeHMS:
    def __init__(self, hours, minutes, seconds):
        #checking if entered data is valid
        if not (0 <= hours <= 23):
            print('Invalid value for hours. Hours now set to 0.')
            hours = 0
        if not (0<= minutes <= 59):
            print('Invalid value for minutes. Minutes now set to 0.')
            minutes = 0
        if not (0 <= seconds <= 59):
            print('Invalid value for seconds. Seconds now set to 0.')
            seconds = 0
        
        #assigning variables 
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds
        
    def add_minutes(self, minutes: int):
        #making sure minutes entered cannot be negative
        if minutes < 0:
            print('Error')
            return
        
        #add minutes to self.minutes
        self.minutes += minutes
        #make minutes into hours
        self.hours += self.minutes // 60
        #make sure neither exceed 60 or 24
        self.minutes %= 60
        self.hours %= 24
        
    def add_seconds(self, seconds: int):
        #seconds cant be negative
        if seconds < 0:
            print('Error')
            return
        #same thing as add_minutes, but longer because of the seconds
        self.seconds += seconds
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes //60
        self.minutes %= 60
        self.hours %= 24
    
    def __add__(self, seconds: int):
        if seconds < 0:
            return TimeHMS(0, 0, 0)
        
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds + seconds
        
        new_hours = total_seconds // 3600 % 24
        total_seconds %= 3600
        new_minutes = total_seconds // 60
        new_seconds = total_seconds % 60
        
        return TimeHMS(new_hours, new_minutes, new_seconds)
    
    def __str__(self):
        am_pm='AM'
        self.night_or_day = am_pm
        hours = self.hours
        if hours >= 12:
            am_pm='PM'
            if hours > 12:
                hours -= 12
        if hours == 0:
            hours = 12   
        print(f'{hours}:{self.minutes:0>2}:{self.seconds:0>2}{am_pm}')
      
        
    def to_string_military(self):
        #time with leading zeros on hours 
        print(f'{self.hours:0>2}{self.minutes:0>2}{self.seconds:0>2}')
        
    def to_string_24(self):
        #time without leading zeros on hours
        print(f'{self.hours}:{self.minutes:0>2}:{self.seconds:0>2}')
                
        
    def __eq__(self, TimeHMS):
        if (self.seconds == TimeHMS.seconds) and (self.minutes == TimeHMS.minutes) and (self.hours == TimeHMS.hours):
            return True
        else:
            return False
        #returns true if argument is a TimeHMs object that represents a time different from this object
        #otherwise, return false
    
    def __ne__(self, TimeHMS):
        if (self.seconds != TimeHMS.seconds) and (self.minutes != TimeHMS.minutes) and (self.hours != TimeHMS.hours):
            return True
        else:
            return False
        #returns true if argument is a TimeHMs object that represents a time different from this object
        #otherwise, return false
    
time_instance = TimeHMS(12, 4, 5)

time_instance.add_seconds(4)

print(time_instance) 

        