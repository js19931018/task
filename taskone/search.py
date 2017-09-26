'''search(path,*args) return a list contain result
if path is sql,search in sql,else search in a json file with the path,
args are keywords  see save-to-data to store data in sql'''





import os
import django
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taskone.settings")
django.setup()


from fileanalysis.models import Path_and_name
import json
import logging



def searchsql(keylist):
    l = []
    lk = []
    for i in keylist:
        pkeyword = '/'+i
        lk.append(pkeyword)

    p = Path_and_name.objects.filter(name__icontains=lk[0])
    lk.pop(0)
    for i in lk:
        print i
        p = p.filter(name__icontains=i)



    for item in p:
        l.append({'name': item.name, 'path': item.path})


    return l

def searchjson(path, keylist):
    f = open(path)
    r = json.load(f)
    l = []
    lk=[]
    for i in keylist:

        pkeyword = i
        lk.append(pkeyword)

    for item in r:
        check=True
        k = item['name'].split('/')
        for i in lk:

            if i not in k:
                check = False
            else:
                pass
        if check == True:
            l.append(item)
        else:
            pass

    return l

def search(path, *args):
    if path == 'sql':
        r = searchsql(args)
        logging.info('Search in sql:%s' % r)
        print r
        return r

    else:
        r = searchjson(path, args)
        logging.info('Search in sql:%s' % r)
        print r
        return r







if __name__ == '__main__':
    search('/home/jsw/taskone/fileanalysis/name_path.json', 'employee', 'employeeRelations')













