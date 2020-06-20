from f.tree_node import TreeNode


class AVLSearchTree:

    def __init__(self) -> None:
        self.root = None
        self.size = 0

    def __len__(self) -> int:
        return self.length()

    def __iter__(self):
        return self.root.__iter__()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value) -> None:
        self.put(key, value)

    def __delitem__(self, key) -> None:
        self.delete(key)

    def __contains__(self, key) -> bool:
        return True if self._get(key, self.root) else False

    def getTreeValues(self):
        result, items, queue = [], [], []
        if self.root is None:
            return result
        queue.append(self.root)
        while queue:
            current = queue.pop(0)
            items.append(current)
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        [result.append(item.value) for item in items]
        return result

    def length(self) -> int:
        return self.size

    def get(self, key):
        if self.root:
            node = self._get(key, self.root)
            return node.value if node else None
        else:
            return None

    def _get(self, key, node: TreeNode):
        if not node:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._get(key, node.left)
        else:
            return self._get(key, node.right)

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, node: TreeNode):
        if key < node.key:
            if node.hasLeftChild():
                self._put(key, value, node.left)
            else:
                node.left = TreeNode(key, value, parent=node)
                self._balance(node.left)
        else:
            if node.hasRightChild():
                self._put(key, value, node.right)
            else:
                node.right = TreeNode(key, value, parent=node)
                self._balance(node.right)

    def _balance(self, node: TreeNode):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self._rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self._balance(node.parent)

    def _rebalance(self, node: TreeNode) -> None:
        if node.balanceFactor < 0:
            if node.right.balanceFactor > 0:
                self.rotateRight(node.right)
                self.rotateLeft(node)
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.left.balanceFactor < 0:
                self.rotateLeft(node.left)
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def delete(self, key) -> None:
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self._delete(nodeToRemove)
                self.size -= 1
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Key is not in tree')

    def _delete(self, node: TreeNode) -> None:
        if node.isLeaf():
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        elif node.hasBothChildren():
            sub = node.findSubNode()
            sub.spliceOut()
            node.key = sub.key
            node.value = sub.value
        else:
            if node.hasLeftChild():
                if node.isLeftChild():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                elif node.isRightChild():
                    node.left.parent = node.parent
                    node.parent.right = node.left
                else:
                    node.replace(node.left.key, node.left.value, node.left.left, node.left.right)
            else:
                if node.isLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.isRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replace(node.right.key, node.right.value, node.right.left, node.right.right)

    def rotateLeft(self, node) -> None:
        """
        左旋前：
          E
        F   C
           D B
              A

        左旋后：
           C
         E   B
        F D   A

        左旋步骤：
          - 将右子节点（节点 C）提升为子树的根节点；
          - 将旧根节点（节点 E）作为新根节点的左子节点；
          - 如果新根节点（节点 C）已经有一个左子节点，将其作为新左子节点（节点 E）的右子节点。
            因为节点 C 之前是节点 E 的右子节点，所以此时节点 E 必然没有右子节点。
            因此，可以为它添加新的右子节点，而无须过多考虑。
        """
        root = node.right
        node.right = root.left
        if root.left is not None:
            root.left.parent = node
        root.parent = node.parent
        if node.isRoot():
            self.root = root
        else:
            if node.isLeftChild():
                node.parent.left = root
            else:
                node.parent.right = root
        root.left = node
        node.parent = root
        node.balanceFactor = node.balanceFactor + 1 - min(root.balanceFactor, 0)
        root.balanceFactor = root.balanceFactor + 1 + max(node.balanceFactor, 0)

    def rotateRight(self, node) -> None:
        """
        右旋前：
            E
          C   F
         B D
        A

        右旋后：
           C
         B   E
        A   D F

        右旋步骤：
          - 将左子节点（节点 C）提升为子树的根节点；
          - 将旧根节点（节点 E）作为新根节点的右子节点；
          - 如果新根节点（节点 C）已经有一个右子节点（节点 D），将其作为新右子节点（节点 E）的左子节点。
            因为节点 C 之前是节点 E 的左子节点，所以此时节点 E 必然没有左子节点。
            因此，可以为它添加新的左子节点，而无须过多考虑。
        """
        root = node.left
        node.left = root.right
        if root.right is not None:
            root.right.parent = node
        root.parent = node.parent
        if node.isRoot():
            self.root = root
        else:
            if node.isRightChild():
                node.parent.right = root
            else:
                node.parent.left = root
        root.right = node
        node.parent = root
        node.balanceFactor = node.balanceFactor + 1 - min(root.balanceFactor, 0)
        root.balanceFactor = root.balanceFactor + 1 + max(node.balanceFactor, 0)
