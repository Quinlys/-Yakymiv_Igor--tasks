# -*- coding: utf-8 -*- 


def have_same_items(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    if list1 == list2:
        return True
    else:
        return False

