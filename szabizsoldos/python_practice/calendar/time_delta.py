import datetime
import time

def time_delta(t1, t2):
    dt1 = datetime.datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    dt2 = datetime.datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    if dt1 < dt2:
        return str(abs(round((dt1 - dt2).total_seconds())))
    else:
        return str(abs(round((dt2 - dt1).total_seconds())))


t = int(input())

for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(delta)
