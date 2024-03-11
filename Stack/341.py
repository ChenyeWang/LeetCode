# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be judged as correct.

from collections import deque

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flatten = deque(nestedList)
    
    def next(self) -> int:
        return self.flatten.popleft()
            
    def hasNext(self) -> bool:
        res = None
        while res == None and len(self.flatten) > 0:
            if self.flatten[0].isInteger():
                return True
            else:
                lst = self.flatten.popleft().getList()
                for ni in reversed(lst):
                    self.flatten.appendleft(ni)
        return False