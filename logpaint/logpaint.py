file = "DianmiHR365-2015-789.xls"
f = open(file, 'rb')
lines = f.readlines()
loglist = []
by_province7 = {}
province_all = {}
province_all_10 = {}




def sortedDict(adict):
    for i in range(4):
        t=max(adict.items(), key=lambda x: x[1])
        province_all_10[t[0]]=t[1]
        del province_all[t[0]]
def getresult():

    for line in lines:
        l = line.split()
        if len(l) == 4:
            date = l[3][32] + l[3][33] + l[3][35] + l[3][36]
            l.pop()
            l.append(int(date))
            loglist.append(l)
    loglist.sort(key=lambda x: x[3])
    print loglist
    for province_day in loglist:
        if by_province7.has_key(province_day[1]):
            by_province7[province_day[1]].append(int(province_day[2]))
            province_all[province_day[1]] += int(province_day[2])
        else:
            by_province7[province_day[1]] = [int(province_day[2])]
            province_all[province_day[1]] = int(province_day[2])

    sprovince_all = sortedDict(province_all)

    print 'sp:', province_all_10

    print by_province7
    print len(by_province7)
    for k, v in by_province7.items():
        if province_all_10.has_key(k):
            print len(v)
        else:
            del by_province7[k]
    return by_province7

if __name__ == '__main__':
    print getresult()
