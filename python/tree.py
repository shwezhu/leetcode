from collections import deque


class Solution257:
    def travel_node(self, node, path, res):
        path.append(node.val)
        if not node.left and not node.right:
            res.append('->'.join([str(val) for val in path]))
            return

        if node.left:
            self.travel_node(node.left, path, res)
            path.pop()
        if node.right:
            self.travel_node(node.right, path, res)
            path.pop()

    def binaryTreePaths(self, root):
        res = []
        path = []
        if not root:
            return res

        self.travel_node(root, path, res)
        return res


class Solution110(object):
    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    def isBalanced(self, root):
        return self.getHeight(root) != -1


class Solution222(object):
    def count(self, node):
        if not node:
            return 0
        left = self.count(node.left)
        right = self.count(node.right)
        return left + right + 1

    def countNodes(self, root):
        return self.count(root)


def countNodes222(root):
    if not root:
        return 0

    queue = deque()
    queue.append(root)
    num_nodes = 0
    while queue:
        num_nodes += 1
        node_ = queue.popleft()
        if node_.left:
            queue.append(node_.left)
        if node_.right:
            queue.append(node_.right)
    return num_nodes


class Solution111:
    def getDepth(self, node):
        if not node:
            return 0
        if not node.left:
            return 1 + self.getDepth(node.right)
        if not node.right:
            return 1 + self.getDepth(node.left)
        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))

    def minDepth(self, root):
        return self.getDepth(root)


def minDepth111(root):
    if not root:
        return 0
    queue = deque()
    min_d = 0
    queue.append(root)

    while queue:
        for _ in range(len(queue)):
            node_ = queue.popleft()
            if not node_.left and not node_.right:
                return min_d + 1
            if node_.left:
                queue.append(node_.left)
            if node_.right:
                queue.append(node_.right)
        min_d += 1
    return min_d


class Solution104:
    def getDepth(self, node_):
        if not node_:
            return 0
        left_height = self.getDepth(node_.left)
        right_height = self.getDepth(node_.right)
        return 1 + max(left_height, right_height)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getDepth(root)


def maxDepth104(root):
    if not root:
        return 0

    q = deque()
    d = 0
    q.append(root)
    while q:
        for i in range(len(q)):
            node_ = q.popleft()
            if node_.left:
                q.append(node_.left)
            if node_.right:
                q.append(node_.right)
        d += 1
    return d


class Solution1:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val
                and self.isMirror(left.right, right.left)
                and self.isMirror(left.left, right.right))

    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)


def invertTree(root):
    if root is None:
        return None

    queue = deque()
    queue.append(root)
    while queue:
        # invert
        node_ = queue.popleft()
        temp_node = node_.left
        node_.left = node_.right
        node_.right = temp_node

        if node_.left:
            queue.append(node_.left)
        if node_.right:
            queue.append(node_.right)
    return root


def postorderTraversal(root):
    def traverse(res_, node):
        if node is None:
            return
        traverse(res_, node.left)
        traverse(res_, node.right)
        res_.append(node.val)

    res = []
    traverse(res, root)
    return res


def preorderTraversal(root):
    def traverse(res_, node):
        if node is None:
            return
        res_.append(node.val)
        traverse(res_, node.left)
        traverse(res_, node.right)

    res = []
    traverse(res, root)
    return res


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right