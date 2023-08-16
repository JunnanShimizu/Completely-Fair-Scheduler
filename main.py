# Junnan Shimizu
# 3/20/22
# Project_Three
# Course: CS337

import pandas as pd

import RBTree
import operating_system
import scheduler
import process
import test

if __name__ == '__main__':
    new_RBTree = RBTree.RBTree()
    new_RBTree.insert(3)
    new_RBTree.insert(6)
    new_RBTree.insert(7)
    print("Printing Tree (Inorder):")
    new_RBTree.print_tree(new_RBTree.root)
    new_RBTree.insert(8)
    new_RBTree.insert(1)
    new_RBTree.insert(8)
    print("Printing Tree (Inorder):")
    new_RBTree.print_tree(new_RBTree.root)
    new_RBTree.insert(6)
    new_RBTree.insert(5)
    new_RBTree.insert(1)
    new_RBTree.insert(7)
    print("Printing Tree (Inorder):")
    new_RBTree.print_tree(new_RBTree.root)
