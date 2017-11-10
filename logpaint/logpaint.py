file = "DianmiHR365-2015-789.xls"
f = open(file, 'rb')
lines = f.readlines()
loglist = []
by_province7 = {}
province_all = {}
province_all_10 = {}
missday=[718, 829, 909, 920]
Jul=range(701, 732)
Aug=range(801, 832)
Spt=range(901, 931)
JAS=[]
JAS.extend(Jul)
JAS.extend(Aug)
JAS.extend(Spt)
print 'JAS',JAS



def sortedDict(adict):
    for i in range(4):
        t=max(adict.items(), key=lambda x: x[1])
        province_all_10[t[0]]=t[1]
        del province_all[t[0]]

def fillblankday(by_province):
    for k,v in by_province.items():
        by_province[k]=[]
    for province_day in loglist:
        if len(by_province[province_day[1]])==JAS.index(province_day[3]):
            by_province[province_day[1]].append(int(province_day[2]))
        else:
            for i in range(JAS.index(province_day[3])-len(by_province[province_day[1]])):
                by_province[province_day[1]].append(0)
            by_province[province_day[1]].append(int(province_day[2]))
    for k,v in by_province.items():
        if len(v)<92:
            for i in range(92-len(v)):
                by_province[k].append(0)


def handlemisspoint(by_province):
    for k, v in by_province.items():
        for i in JAS :
            if i != 701 and i != 930:
                v[JAS.index(i)] = (v[JAS.index(i)-1] + v[JAS.index(i)+1])//2 if i in missday else v[JAS.index(i)]



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
