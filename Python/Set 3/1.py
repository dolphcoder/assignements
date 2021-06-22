#1
import datetime
to = datetime.date.today()
yes = to - datetime.timedelta(1)
tom = to + datetime.timedelta(1)
print('Yesterday: {}\nToday: {}\nTomorrow: {}'.format(yes,to,tom))
