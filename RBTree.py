# Junnan Shimizu
# 3/20/22
# Project_Three
# Course: CS337

class RBNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None
        self.red = False

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_parent(self):
        return self.parent

    def set_parent(self, value):
        self.parent = value

    def get_left_child(self):
        return self.left_child

    def set_left_child(self, value):
        self.left_child = value

    def get_right_child(self):
        return self.right_child

    def set_right_child(self, value):
        self.right_child = value

    def get_red(self):
        return self.red

    def set_red(self, value):
        self.red = value


class RBTree:
    def __init__(self):
        self.nil = RBNode(0)
        self.nil.set_red(False)
        self.root = self.nil

    def insert(self, value):
        new_node = RBNode(value)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if new_node.get_value() < x.get_value():
                x = x.get_left_child()
            else:
                x = x.get_right_child()
        new_node.set_parent(y)
        if y == self.nil:
            self.root = new_node
        else:
            if new_node.get_value() < y.get_value():
                y.set_left_child(new_node)
            else:
                y.set_right_child(new_node)
        new_node.set_left_child(self.nil)
        new_node.set_right_child(self.nil)
        new_node.set_red(True)
        self.fix_insert(new_node)
        print("Inserted:", value)

    def fix_insert(self, node):
        while node != self.root and node.get_parent().get_red():
            if node.get_parent() == node.get_parent().get_parent().get_right_child():
                y = node.get_parent().get_parent().get_left_child()
                if y.get_red():
                    y.set_red(False)
                    node.get_parent().set_red(False)
                    node.get_parent().get_parent().set_red(True)
                    node = node.get_parent().get_parent()
                else:
                    if node == node.get_parent().get_left_child():
                        node = node.get_parent()
                        self.rotate_right(node)
                    node.get_parent().set_red(False)
                    node.get_parent().get_parent().set_red(True)
                    self.rotate_left(node.get_parent().get_parent())
            else:
                y = node.get_parent().get_parent().get_right_child()
                if y.get_red():
                    y.set_red(False)
                    node.get_parent().set_red(False)
                    node.get_parent().get_parent().set_red(True)
                    node = node.get_parent().get_parent()
                else:
                    if node == node.get_parent().get_right_child():
                        node = node.get_parent()
                        self.rotate_left(node)
                    node.get_parent().set_red(False)
                    node.get_parent().get_parent().set_red(True)
                    self.rotate_right(node.get_parent().get_parent())
        self.root.set_red(False)

    def rotate_left(self, node):
        print("rotating left")
        y = node.get_right_child()
        node.set_right_child(y.get_left_child())
        y.get_left_child().set_parent(node)
        y.set_parent(node.get_parent)
        if node.get_parent() == self.nil:
            self.root = y
        else:
            if node == node.get_parent().get_left_child():
                node.get_parent().set_left_child(y)
            else:
                node.get_parent().set_right_child(y)
        y.set_left_child(node)
        node.set_parent(y)

    def rotate_right(self, node):
        print("rotating right")
        y = node.get_left_child()
        node.set_left_child(y.get_right_child())
        y.get_right_child().set_parent(node)
        y.set_parent(node.get_parent())
        if node.get_parent() == self.nil:
            self.root = y
        else:
            if node == node.get_parent().get_right_child():
                node.get_parent().set_right_child(y)
            else:
                node.get_parent().set_left_child(y)
        y.set_right_child(node)
        node.set_parent(y)

    def print_tree(self, root):
        if root == self.nil:
            return
        self.print_tree(root.get_left_child())
        print(root.get_value())
        self.print_tree(root.get_right_child())
