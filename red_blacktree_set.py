class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class RBTreeSet:
    def __init__(self):
        self.TNULL = RBNode(0, color='black')
        self.root = self.TNULL

    def _pre_order_helper(self, node):
        if node != self.TNULL:
            print(node.value, end=' ')
            self._pre_order_helper(node.left)
            self._pre_order_helper(node.right)

    def _in_order_helper(self, node, res):
        if node != self.TNULL:
            self._in_order_helper(node.left, res)
            res.append(node.value)
            self._in_order_helper(node.right, res)

    def _post_order_helper(self, node):
        if node != self.TNULL:
            self._post_order_helper(node.left)
            self._post_order_helper(node.right)
            print(node.value, end=' ')

    def _search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.value:
            return node

        if key < node.value:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

    def _balance_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self._right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def _balance_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self._left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self._right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self._right_rotate(x.parent)
                    s = x.parent.left
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self._left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def _transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.value == key:
                z = node
            if node.value <= key:
                node = node.right
            else:
                node = node.left
        if z == self.TNULL:
            print("Couldn't find key in the tree")
            return
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self._transplant(z, z.right)
        elif z.right == self.TNULL:
            x = z.left
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self._balance_delete(x)

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = RBNode(key)
        node.parent = None
        node.value = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'
        y = None
        x = self.root
        while x != self.TNULL:
            y = x
            if node.value < x.value:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y == None:
            self.root = node
        elif node.value < y.value:
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = 'black'
            return
        if node.parent.parent == None:
            return
        self._balance_insert(node)

    def delete(self, key):
        self._delete_node_helper(self.root, key)

    def search(self, key):
        return self._search_tree_helper(self.root, key) != self.TNULL

    def inorder(self):
        res = []
        self._in_order_helper(self.root, res)
        return res

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def _minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def _maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def lower_bound(self, key):
        node = self.root
        result = None
        while node != self.TNULL:
            if node.value >= key:
                result = node
                node = node.left
            else:
                node = node.right
        return result.value if result else None

    def upper_bound(self, key):
        node = self.root
        result = None
        while node != self.TNULL:
            if node.value > key:
                node = node.left
            else:
            	result = node
            	node = node.right
        return result.value if result else None


