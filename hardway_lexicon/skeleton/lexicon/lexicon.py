direction=['north','south','east','west','up','down','left','right','back']
verb=['go','kill','eat','stop']
stop=['the','in','of','from','at','it']
noun=['door','bear','princess','cabinet']
number=['1','2','3','4','5','6','7','8','9','0']

def scan(ipt):
    stuff=ipt
    words=stuff.split()
    words_list=[]
    for i in words:
        r=check_all(i)
        if r:
            words_list.append(r)
        else:
            words_list.append(('error',i))
    return words_list





def check_all(word):
    if check_direction(word):
       return check_direction(word)
    else:
        pass

    if check_verb(word):
       return check_verb(word)
    else:
        pass

    if check_stop(word):
        return  check_stop(word)
    else:
        pass

    if check_noun(word):
        return  check_noun(word)
    else:
        pass

    if check_number(word):
        return check_number(word)
    else:
        pass
    return False

def check_direction(word):
    for i in direction:
        if i==word:
            return ('direction',word)
        else:pass
    return False

def check_verb(word):
    for i in verb:
        if i==word:
            return ('verb',word)
        else:pass
    return False

def check_stop(word):
    for i in stop:
        if i==word:
            return ('stop',word)
        else:pass
    return False

def check_noun(word):
    for i in noun:
        if i == word:
            return ('noun', word)
        else:pass
    return False

def check_number(word):
    for i in word:
        if check_one_number(i)==False:
            return False
        else:
            pass
    return ('number',int(word))




def check_one_number(word):
    for i in number:
        if i == word:
            return word
    return False
