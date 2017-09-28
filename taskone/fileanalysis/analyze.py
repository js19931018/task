import json
import re
from django.http import HttpResponse
from fileanalysis.models import Path_and_name,Path_name_file

f=open('/home/jsw/taskone/fileanalysis/route.json')
readfile = json.load(f)
print readfile
path_list=[]
class PathNode(object):
    def __init__(self, dict_js, forthpath, forthname):
        self.node = dict_js    #a dict contains base n-p
        self.singlename = dict_js['name']
        self.singlepath = dict_js['path']
        self.forthpath = forthpath
        self.forthname = forthname
        if  self.singlepath == '/':
            self.singlepath = ''
            self.path=self.forthpath + self.singlepath
        elif  self.singlepath[0] == '/':
            self.path = self.forthpath + self.singlepath
        else:
            self.path = self.forthpath + '/' + self.singlepath
        self.name=self.forthname+'/'+self.singlename

    def find_child(self):
        if 'children' in self.node:
            self.children = self.node['children'] #this is a list contain nums of childnode
            return True
        else:
            return False

    def traverse(self):
        self.save_traverse()
        if self.find_child():
            r = self.children

            for items in r:
                i = PathNode(items, self.path, self.name)
                i.traverse()

        else:
            pass

    def save_traverse(self):
        print 'self.node', type(self.node), type(self.name)
        dict_node = {'name': self.name, 'path': self.path, 'endcheck': [self.singlename, self.singlepath]}
        path_list.append(dict_node)


def traverse_list():

    for items in readfile:
        i = PathNode(items, '', '')
        i.traverse()
    addroot()
    fl = open('name_path.json', 'w')
    fl.write(json.dumps(path_list, ensure_ascii=False, indent=2))
    fl.close()
    return path_list

def traverse_list_request(file):
    del path_list[:]
    for items in file:
        i = PathNode(items, '', '')
        i.traverse()
    addroot()
    fl = open('/home/jsw/taskone/np.json', 'w')
    fl.write(json.dumps(path_list, ensure_ascii=False, indent=2))
    fl.close()
    return path_list


def addroot():
    path_list[0]['path'] = '/'

def save_to_sql(file):
    for i in file:
        q = Path_name_file(name=i['name'], path=i['path'], endcheck=i['endcheck'])
        q.save()

def analyzerequest(request):
    if request.method == "POST":
        file = request.body
        print file
        f = json.loads(file)
        print type(f)
        r = traverse_list_request(f)
        save_to_sql(r)
        return HttpResponse(r)
    else:
        pass








if __name__ == '__main__':
    traverse_list()
    print path_list





