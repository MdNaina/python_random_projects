import random


dice = random.randrange(1,7)

if dice == 1:
    print('''
    +-------+
    |       |
    |   $   |
    |       |
    +-------+''')

elif dice == 2:
    print('''
    +-------+
    | $     |
    |       |
    |     $ |
    +-------+''')

elif dice == 3:
    print('''
    +-------+
    | $     |
    |   $   |
    |     $ |
    +-------+''')

elif dice == 4:
    print('''
    +-------+
    | $   $ |
    |       |
    | $   $ |
    +-------+''')

elif dice == 5:
    print('''
    +-------+
    |   $   |
    | $   $ |
    |  $ $  |
    +-------+''')

elif dice == 6:
    print('''
    +-------+
    | $   $ |
    | $   $ |
    | $   $ |
    +-------+''')
