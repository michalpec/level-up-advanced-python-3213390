# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime
import math


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
        return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()
    times = []

    def get_time(line: str) -> str:
        return re.findall(r'\d{2}:\S+', line)[0]

    for line in races.splitlines():
        if 'Jennifer Rhines' in line:
            time = get_time(line)
            times.append(time)
    return times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    sum_time_seconds = 0
    for t in racetimes:
        m, sms = t.split(':')
        try:
            s, ms = sms.split('.')
        except:
            s = sms
            ms = 0
        sum_time_seconds += datetime.timedelta(minutes=float(m), seconds=float(s), milliseconds=float(ms)).total_seconds()

    avg_seconds = sum_time_seconds / len(racetimes)

    minutes = (avg_seconds % 3600) // 60
    seconds_milliseconds = (avg_seconds % 60)
    seconds = math.floor(seconds_milliseconds)
    milliseconds = (seconds_milliseconds - seconds)
    print(minutes, seconds, int(milliseconds*10))
    return ":".join([str(int(minutes)), str(seconds), str(int(milliseconds*10))])


if __name__ == "__main__":
    print(get_average())
