#1
names = input('Enter names: ').split()
if len(names) <= 1:
    if len(names) == 0:
        names = ['Nobody']
    print('{} likes this.'.format(*names))

else:
    s = ((', '.join(['{}']*(len(names)-1)))+' and {} likes this.').format(*names)
    print(s)