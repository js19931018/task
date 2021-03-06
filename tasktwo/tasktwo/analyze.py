import json
import re

f=open('route.json')
readfile=json.load(f)
print  readfile
path_list=[]
class PathNode(object):
    def __init__(self,dict_js,forthpath,forthname):
        self.node=dict_js
        self.singlename=dict_js['name']
        self.singlepath=dict_js['path']
        self.forthpath=forthpath
        self.forthname=forthname
        if  self.singlepath=='/':
            self.singlepath=''
            self.path=self.forthpath + self.singlepath
        elif  re.match(r'^/\s{0,50}',self.singlepath):
            self.path = self.forthpath  + self.singlepath
        else:
            self.path = self.forthpath + '/' + self.singlepath
        self.name=self.forthname+'/'+self.singlename
    def find_child(self):
        if 'children' in self.node:
            self.children=self.node['children'] #this is a list contain nums of childnode
            return True
        else:
            return False
    def traverse(self):
        self.save_traverse()
        if self.find_child():
            r=self.children

            for items in r:
                i=PathNode(items,self.path,self.name)
                i.traverse()

        else:
            pass

    def save_traverse(self):
        dict_node={'name':self.name,'path':self.path}
        path_list.append(dict_node)


def traverse_list():
    for items in readfile:
        i=PathNode(items,'','')
        i.traverse()
    return path_list




if __name__ == '__main__':
    traverse_list()
    print path_list




