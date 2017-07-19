# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, date, time, timedelta
log_on = True

def log (*string):
    if log_on:
        print ' '.join(str(x) for x in string)
    # end if
# end def

class datedelta():
    start_date = None
    end_date = None
    START_TIME = time(0, 0, 0)
    END_TIME = "___end_time___"

    def __init__(self, start_date = None, end_date = None):
        self.start_date = start_date
        self.end_date = end_date
    # end def

    def move_to_hour(self, hours):
        start_date = self.start_date + timedelta(hours=hours)
        if start_date <= self.end_date:
            return datedelta(start_date, self.end_date)
        # end if
        return datedelta()
    # end def

    def daterange(self):
        car_date = self.start_date.date()
        end_date = self.end_date.date()
        while car_date <= end_date:
            yield car_date
            car_date = car_date + timedelta(days=1)
        # end for
    # end def

    def horas(self):
        return self.timedelta().total_seconds() /60/60
    # end def

    def timedelta(self):
        if not self.empty():
            return self.end_date - self.start_date
        # end if
        return timedelta()
    # end def

    def empty(self):
        return not (self.start_date and self.end_date) or self.start_date == self.end_date 
    # end def

    @staticmethod
    def for_dates(start_date, end_date):
        start_date = datetime.combine(start_date, datedelta.START_TIME)
        end_date = datetime.combine(end_date, datedelta.START_TIME)
        return datedelta(start_date, end_date)
    # end def

    @staticmethod
    def for_day(single_date, start_date, end_date):
        start_date = datetime.combine(single_date, start_date)
        if end_date == datedelta.END_TIME:
            end_date = datedelta.START_TIME
            single_date = single_date + timedelta(days=1)
        # end if
        end_date = datetime.combine(single_date, end_date)
        return datedelta(start_date, end_date)
    # end def

    def low_date(self, date1, date2):
        return date1 if date1 < date2 else date2
    # end def

    def intersect(self, date_delta):
        if self.empty():
            return datedelta(date_delta.start_date, date_delta.end_date)
        elif date_delta.empty():
            return datedelta(self.start_date, self.end_date)
        elif self.end_date > date_delta.start_date and self.start_date <= date_delta .start_date:
            return datedelta(date_delta.start_date, self.low_date(self.end_date, date_delta.end_date))
        elif date_delta.end_date > self.start_date and self.start_date >= date_delta.start_date:
            return datedelta(self.start_date, self.low_date(self.end_date, date_delta.end_date))
        # end if
        return datedelta()
    # end def

    def difference_single(self, date_delta):
        if self.empty():
            return multi_datedelta()
        elif date_delta.empty():
            return multi_datedelta([datedelta(self.start_date, self.end_date)])
        elif self.end_date >= date_delta.start_date and date_delta.start_date >= self.start_date:
            delta = multi_datedelta([datedelta(self.start_date, date_delta.start_date)])
            if date_delta.end_date <= self.end_date:
                delta = delta + datedelta(date_delta.end_date, self.end_date)
            # end if
            return delta
        elif date_delta.end_date >= self.start_date and self.start_date >= date_delta.start_date:
            if date_delta.end_date >= self.end_date:
                return multi_datedelta()
            # end if
            return multi_datedelta([datedelta(date_delta.end_date, self.end_date)])
        # end if
        return multi_datedelta([datedelta(self.start_date, self.end_date)])
    # end def

    def difference(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.difference_single(date_delta)
        else:
            delta = multi_datedelta([datedelta(self.start_date, self.end_date)])
            return delta.difference(date_delta)
        # end if
    # end def

    def __str__(self):
        return "{%s - %s}" % (unicode(self.start_date), unicode(self.end_date))
    # end def
# end class

class multi_datedelta():

    def __init__(self, date_deltas = []):
        self.date_deltas = date_deltas
    # end def

    def __iter__(self):
        for single_delta in self.date_deltas:
            yield single_delta
        # end for
    # end def

    def move_to_hour(self, hour):
        date_deltas = []
        for single_dalta in self.date_deltas:
            if not len(date_deltas):
                delta = single_dalta.move_to_hour(hour)
            else:
                delta = single_dalta
            # end if
            if not delta.empty():
                date_deltas.append(delta)
            else:
                hour = hour - single_dalta.horas()
            # end if
        # end for
        return multi_datedelta(date_deltas)
    # end def

    def horas(self):
        return self.timedelta().total_seconds() /60/60
    # end def

    def timedelta(self):
        time = timedelta()
        for single_dalta in self.date_deltas:
            time = time + single_dalta.timedelta()
        # end for
        return time
    # end def

    def difference_single(self, date_delta):
        multi_date_deltas = multi_datedelta()
        for single_dalta in self.date_deltas:
            delta = single_dalta.difference(date_delta)
            if not delta.empty():
                multi_date_deltas = multi_date_deltas + delta
            # end for
        # end for
        return multi_date_deltas
    # end def

    def intersect_single(self, date_delta):
        date_deltas = []
        for single_dalta in self.date_deltas:
            delta = date_delta.intersect(single_dalta)
            if not delta.empty():
                date_deltas.append(delta)
            # end for
        # end for
        return multi_datedelta(date_deltas)
    # end def

    def intersect_multi(self, multi_date_delta):
        multi_date_deltas = multi_datedelta()
        for single_dalta in self.date_deltas:
            multi_delta = multi_date_delta.intersect_single(single_dalta)
            if not multi_delta.empty():
                multi_date_deltas = multi_date_deltas + multi_delta
            # end for
        # end for
        return multi_date_deltas
    # end def

    def difference_multi(self, multi_date_delta):
        multi_date_deltas = multi_datedelta(self.date_deltas)
        for single_dalta in multi_date_delta.date_deltas:
            multi_date_deltas = multi_date_deltas.difference_single(single_dalta)
        # end for
        return multi_date_deltas
    # end def
    
    def difference_periodic(self, periodic_time_delta):
        log(self, 'difference_periodic', periodic_time_delta)
        if not periodic_time_delta.empty():
            multi_date_deltas = multi_datedelta(self.date_deltas)
            multi_date_deltas = periodic_time_delta.invert().intersect(multi_date_deltas)
            return multi_date_deltas
        # end if
        return multi_datedelta(self.date_deltas)
    # end def

    def intersect(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.intersect_single(date_delta)
        elif isinstance(date_delta, multi_datedelta):
            return self.intersect_multi(date_delta)
        # end if
        return multi_datedelta()
    # end def

    def difference(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.difference_single(date_delta)
        elif isinstance(date_delta, multi_datedelta):
            return self.difference_multi(date_delta)
        elif isinstance(date_delta, periodic_timedelta):
            return self.difference_periodic(date_delta)
        # end if
        return multi_datedelta()
    # end def

    def empty(self):
        return len(self.date_deltas) == 0
    # end if

    def __add__(self, date_delta):
        if date_delta.empty():
            if self.empty():
                return multi_datedelta()
            # end if
            return multi_datedelta(self.date_deltas)
        elif isinstance(date_delta, datedelta):
            return multi_datedelta(self.date_deltas + [date_delta])
        elif isinstance(date_delta, multi_datedelta):
            return multi_datedelta(self.date_deltas + date_delta.date_deltas)
        # end if
        return None
    # end if

    def __str__(self):
        string = ""
        for single_delta in self.date_deltas:
            string = string + str(single_delta) + ", "
        # end for
        return "(%s)" % (string, )
    # end def

# end class

class periodic_timedelta():
    def __init__(self, start_time = None, end_time = None):
        self.start_time = start_time
        self.end_time   = end_time
    # end def

    def empty(self):
        return not (self.start_time and self.end_time) or self.start_time == self.end_time
    # end if 

    def invert(self):
        return periodic_timedelta(self.end_time, self.start_time)
    # end def

    def intersec_by_day(self, single_date, date_delta):
        if self.start_time > self.end_time:
            delta1 = datedelta.for_day(single_date, datedelta.START_TIME, self.end_time)
            delta2 = datedelta.for_day(single_date, self.start_time, datedelta.END_TIME)
            delta = multi_datedelta([delta1, delta2])
        else:
            delta = multi_datedelta([datedelta.for_day(single_date, self.start_time, self.end_time)])
        # end if
        return delta.intersect(date_delta)
    # end def

    def intersect_single(self, date_delta):

        log (self, 'intersect', date_delta)
        multi_date_delta = multi_datedelta()
        for single_date in date_delta.daterange():
            multi_date_delta = multi_date_delta + self.intersec_by_day(single_date, date_delta)
        # end for
        return multi_date_delta
    # end def

    def intersect_multi(self, multi_date_delta):
        multi_delta = multi_datedelta()
        for single_delta in multi_date_delta.date_deltas:
            multi_delta = multi_delta + self.intersect_single(single_delta)
        # end for
        return multi_delta
    # end def

    def intersect(self, date_delta):
        if isinstance(date_delta, datedelta):
            return self.intersect_single(date_delta)
        elif isinstance(date_delta, multi_datedelta):
            return self.intersect_multi(date_delta)
        # end if
        return multi_datedelta()
    # end def

    def __str__(self):
        return "[%s - %s]" % (self.start_time, self.end_time)
    # end def

# end def

    