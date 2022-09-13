#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:41:36 2021

@author: bushra

Bushra Ibrahim

Exam 2

Question 3
"""
from binarytreeClass import *
from math import inf

b = BinaryTree('A')
b.insertLeft('B')
b.insertRight('C')
b.getLeftChild().insertRight('D')
b.getRightChild().insertLeft('E')
b.getLeftChild().getRightChild().insertLeft('F')
b.getLeftChild().getRightChild().insertRight('G')
b.getLeftChild().getRightChild().getLeftChild().insertLeft('H')
printTree(b)


preorder = []
preorder.append(b.getRootVal())
if b.getLeftChild() != None:
    preorder.append(b.getLeftChild().root)
    print(b.getLeftChild().root)

def Pre(b):
    preorder = []
    
    if b.getLeftChild() != None:
        Pre(b)
    if b.getRightChild() != None:
        Pre(b)
        
    preorder.append(b.getRootVal())
    preorder.append(b.getLeftChild())
    preorder.append(b.getRightChild())
    
    return preorder

#inorder = left, root, right

#postorder = root, left, right
