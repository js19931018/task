animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

choose=raw_input('Please choose a method to get element O/C:')
if choose=='C':
    select=raw_input('Cardinal:')
    select=int(select)
    print 'The %dst animal is at %d and is a %s'%(select+1,select,animals[select])
    print 'The animal at %d is %dst animal is a %s'%(select,select+1,animals[select])
if choose=='O':
    select=raw_input('Ordinal:')
    select = int(select)
    print 'The %dst animal is at %d and is a %s'%(select,select-1,animals[select])
    print 'The animal at %d is %dst animal is a %s'%(select-1,select,animals[select])