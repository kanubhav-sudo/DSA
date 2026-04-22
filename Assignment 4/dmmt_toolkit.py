# ---------------- BST ----------------
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.minValue(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def minValue(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# ---------------- GRAPH ----------------
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.graph.get(node, []))

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbour in self.graph.get(node, []):
                self.dfs(neighbour, visited)

# ---------------- HASH TABLE ----------------
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_func(key)
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_func(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_func(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)

# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("BST Operations")
    bst = BST()
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        root = bst.insert(root, v)

    print("\nInorder:")
    bst.inorder(root)

    print("\nSearch 20:", bool(bst.search(root, 20)))
    print("Search 90:", bool(bst.search(root, 90)))

    root = bst.delete(root, 20)
    print("\nAfter deleting 20:")
    bst.inorder(root)

    # Graph
    print("\n\nGraph Traversal")
    g = Graph()
    edges = [('A','B'),('A','C'),('B','D'),('B','E'),
             ('C','E'),('D','F'),('E','D'),('E','F'),('C','F')]
    for u,v in edges:
        g.add_edge(u,v)

    print("\nBFS:")
    g.bfs('A')

    print("\nDFS:")
    g.dfs('A')

    # Hash Table
    print("\n\nHash Table")
    ht = HashTable(5)
    keys = [10,15,20,7,12]
    for k in keys:
        ht.insert(k, k*10)

    print("Get 10:", ht.get(10))
    print("Get 15:", ht.get(15))
    print("Get 7:", ht.get(7))

    ht.delete(15)
    print("After deleting 15:", ht.table)
