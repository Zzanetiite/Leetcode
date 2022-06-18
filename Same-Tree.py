'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input:
p = [1,2,3]
q = [1,2,3]
Output: true

Example 2:
Input:
p = [1,2]
q = [1,"null",2]
Output: false

Example 3:
Input:
p = [1,2,1]
q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
'''
p = [1,2,1]
q = [1,1,2]

#Trees are the same if every node in the list has the same value.

def isSameTree(p, q) :
    '''
    #If different length they are not the same
    if len(p) != len(q) :
        return False
    #Check each index for both. If not the same - return False
    for i in range(len(p)):
        if p[i] != q[i] :
            return False
    #Else : True
    return True
    '''

#Answer from Leetcode - Trees are not lists as I used them.
#Trees have different formulas.

    # p and q are both None
    if not p and not q:
        return True

    # one of p and q is None
    if not q or not p:
        return False
    if p.val != q.val:
        return False

    return self.isSameTree(p.right, q.right) and \
           self.isSameTree(p.left, q.left)
