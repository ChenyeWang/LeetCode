# You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

# If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

# Note that the nodes have no values and that we only use the node numbers in this problem.

from ast import List
from collections import deque

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find the root (who is not a left child or a right child of any node)
        notChild = set([i for i in range(n)])
        for lc in leftChild:
            if lc != -1 and lc in notChild: notChild.remove(lc)
        for rc in rightChild:
            if rc != -1 and rc in notChild: notChild.remove(rc)
        # only start BFS when we find one root
        if len(notChild) == 1:
            visited = set()
            q = deque([notChild.pop()])
            while q:
                i = q.popleft()
                if i in visited: return False
                visited.add(i)
                if leftChild[i] != -1:
                    q.append(leftChild[i])
                if rightChild[i] != -1:
                    q.append(rightChild[i])
            return len(visited) == n
        else:
            return False