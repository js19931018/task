file = "DianmiHR365-2015-789.xls"
f = open(file, 'rb')
lines = f.readlines()
loglist = []
by_province7 = {}
province_all = {}
province_all_10 = {}
missday=[718, 829, 909, 920]
MISSDAY=[]
Jan=range(101, 132)
Feb=range(201, 229)
Mar=range(301, 332)
Apr=range(401, 431)
May=range(501, 532)
Jun=range(601, 631)
Jul=range(701, 732)
Aug=range(801, 832)
Spt=range(901, 931)
Oct=range(1001, 1032)
Nov=range(1101, 1131)
Dec=range(1201, 1232)
JAS=[]
DATE=[]
JAS.extend(Jul)
JAS.extend(Aug)
JAS.extend(Spt)
YEAR=[]
YEAR.extend(Jan)
YEAR.extend(Feb)
YEAR.extend(Mar)
YEAR.extend(Apr)
YEAR.extend(May)
YEAR.extend(Jun)
YEAR.extend(Jul)
YEAR.extend(Aug)
YEAR.extend(Spt)
YEAR.extend(Oct)
YEAR.extend(Nov)
YEAR.extend(Dec)

print 'JAS', JAS



def sortedDict(adict):
    for i in range(4):
        t=max(adict.items(), key=lambda x: x[1])
        province_all_10[t[0]]=t[1]
        del province_all[t[0]]

def fillblankday(by_province):
    date = YEAR[YEAR.index(DATE[0]):YEAR.index(DATE[-1]) + 1]
    for k,v in by_province.items():
        by_province[k]=[]
    for province_day in loglist:
        if len(by_province[province_day[1]])==date.index(province_day[3]):
            by_province[province_day[1]].append(int(province_day[2]))
        else:
            for i in range(date.index(province_day[3])-len(by_province[province_day[1]])):
                by_province[province_day[1]].append(0)
            by_province[province_day[1]].append(int(province_day[2]))
    for k,v in by_province.items():
        if len(v)<(len(MISSDAY)+len(DATE)):
            for i in range(len(MISSDAY)+len(DATE)-len(v)):
                by_province[k].append(0)


def handlemisspoint(by_province):
    date = YEAR[YEAR.index(DATE[0]):YEAR.index(DATE[-1]) + 1]
    for k, v in by_province.items():
        for i in date:
            if i != date[0] and i != date[-1]:
                v[date.index(i)] = (v[date.index(i)-1] + v[date.index(i)+1])//2 if i in missday else v[date.index(i)]

def getdatedict():
    for i in loglist:
        date =int(i[3])
        if date not in DATE:
            DATE.append(date)
        else:
            pass
    date=YEAR[YEAR.index(DATE[0]):YEAR.index(DATE[-1])+1]
    for i in date:
        if i not in DATE:
            MISSDAY.append(i)

    print 'DATE',len(DATE),DATE
    print  MISSDAY



def getresult():

    for line in lines:
        l = line.split()
        if len(l) == 4:
            date = l[3][32] + l[3][33] + l[3][35] + l[3][36]
            l.pop()
            l.append(int(date))
            loglist.append(l)
    loglist.sort(key=lambda x: x[3])
    print 'lgl', loglist
    getdatedict()
    for province_day in loglist:
        if by_province7.has_key(province_day[1]):
            by_province7[province_day[1]].append(int(province_day[2]))
            province_all[province_day[1]] += int(province_day[2])
        else:
            by_province7[province_day[1]] = [int(province_day[2])]
            province_all[province_day[1]] = int(province_day[2])

    sprovince_all = sortedDict(province_all)

    print 'bp7', by_province7

    fillblankday(by_province7)
    handlemisspoint(by_province7)



    return by_province7

if __name__ == '__main__':
    print getresult()
