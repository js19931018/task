# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.test import TestCase

from analyze import traverse_list


# Create your tests here.
class Testpath(TestCase):
    def testsinglepath(self):
        list_namepath=traverse_list()
        list_false_path=[]
        list_empty_path=[]
        for item in list_namepath:
            counter=0
            pcounter=-1
            if item['path']=='':
                list_empty_path.append(item['name'])
            for char in item['path']:
                counter = counter + 1
                if char=='/':
                    if counter-pcounter==1:
                         list_false_path.append(item['path'])
                    else:

                        pcounter=counter
                else:
                    pass
        self.assertEqual(list_false_path, [])
        self.assertEqual(list_empty_path, [])
'''
class Testnumber(TestCase):
    def testnumber(self):
        list_namepath_n=traverse_list()
        list_namepath_n.pop(0)
        list_not_equal=[]
        for item in list_namepath_n:
            pcountpath=0
            pcountname=0
            for char in item['name']:
                if char=='/':
                    pcountname = pcountname + 1
                else:
                    pass
            for char in item['path']:
                if char=='/':
                    pcountpath = pcountpath + 1
                else:
                    pass
            if (pcountpath+1) == pcountname:
                pass
            else:
                list_not_equal.append(item)
        print 'not equal:', list_not_equal
        self.assertEqual(list_not_equal,[])


'''





