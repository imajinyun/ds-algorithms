from e.tree_node import TreeNode


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return self.root.__iter__()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __delitem__(self, key):
        self.delete(key)

    def __contains__(self, key):
        return True if self._get(key, self.root) else False

    def length(self):
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
        else:
            if node.hasRightChild():
                self._put(key, value, node.right)
            else:
                node.right = TreeNode(key, value, parent=node)

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self._delete(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError('Key is not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Key is not in tree')

    def _delete(self, node: TreeNode):
        # 待删除的节点是叶子节点
        if node.isLeaf():
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
        # 待删除的节点有两个节点
        elif node.hasBothChildren():
            nodeToRemove = node.findNextNode()
            nodeToRemove.spliceOut()
            node.key = nodeToRemove.key
            node.value = nodeToRemove.value
        # 待删除的节点仅有一个子节点
        else:
            # 如果待删除的节点是左节点
            if node.hasLeftChild():
                # 如果待删除节点是左节点，将待删除节点的左子节点对父节点的引用改为指向待删除节点的父节点，然后将父节点对待删除节点的引用改为指向待删除节点的左子节点
                if node.hasLeftChild():
                    node.left.parent = node.parent
                    node.parent.left = node.left
                # 如果待删除节点是右节点，将待删除节点的右子节点对父节点的引用改为指向待删除节点的父节点，然后将父节点对待删除节点的引用改为指向待删除节点的右子节点
                elif node.hasRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                # 如果待删除节点没有父节点，那肯定是根节点，调用 replace() 方法，替换根节点即可
                else:
                    node.replace(node.left.key, node.left.value, node.left.left, node.left.right)
            # 如果待删除的节点是右节点
            else:
                if node.hasLeftChild():
                    node.right.parent = node.parent
                    node.parent.left = node.right
                elif node.hasRightChild():
                    node.right.parent = node.parent
                    node.parent.right = node.right
                else:
                    node.replace(node.right.key, node.right.value, node.right.left, node.right.right)
