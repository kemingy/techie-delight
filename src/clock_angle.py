# Clock Angle Problem: Given time in hh:mm format, calculate the shorter angle
# between hour and minute hand in an analog clock.

import math

def parse(time):
    assert ':' in time
    hour, minute = time.split(':')
    return int(hour), int(minute)

def clock_angle(time):
    hour, minute = parse(time)
    degree_hour = hour * 360 / 12 + minute * 360 / 12 / 60
    degree_minute = minute * 360 / 60
    angle = int(math.fabs(degree_hour - degree_minute))

    angle = angle if angle <= 180 else 360 - angle
    return angle
