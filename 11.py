class Node:
    def __init__(self, name, type="dir"):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


n = Node("hello")
n2 = Node('word')
n.children.append(n2)
n2.append = n


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        if name[-1] != "/":
            name += "/"
        if name == "../":
            self.now = self.now.parent
            return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        raise ValueError("invalid dir")


tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
tree.cd("bin/")
tree.mkdir("python/")
tree.cd("../")
print(tree.ls())
