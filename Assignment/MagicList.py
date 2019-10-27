class MagicList:
    def __init__(self):
        self.data = [0]

    def findMin(self):
        M = self.data
        ''' you need to find and return the smallest
            element in MagicList M.
            Write your code after this comment.
        '''
        if len(M) > 1:
            return M[1]
        else:
            return None

    def insert(self, E):
        M = self.data
        ''' you need to insert E in MagicList M, so that
            properties of the MagicList are satisfied. 
            Return M after inserting E into M.
            Write your code after this comment.
        '''
        M.append(E)
        i = len(M) - 1
        while i > 1:
            j = int(i / 2)
            if M[j] > M[i]:
                M[j], M[i] = M[i], M[j]
                i = j
            else:
                break
        return M

    def deleteMin(self):
        M = self.data
        ''' you need to delete the minimum element in
            MagicList M, so that properties of the MagicList
            are satisfied. Return M after deleting the 
            minimum element.
            Write your code after this comment.
        '''
        if len(M) > 1:
            M[1], M[-1] = M[-1], M[1]
            del M[-1]
            i = 1
            while 2 * i < len(M):
                j = 2 * i
                if j + 1 < len(M):
                    if M[i] > M[j] or M[i] > M[j + 1]:
                        if M[j] <= M[j + 1]:
                            M[i], M[j] = M[j], M[i]
                            i = j
                        else:
                            M[i], M[j + 1] = M[j + 1], M[i]
                            i = j + 1
                    else:
                        return M
                else:
                    if M[i] > M[j]:
                        M[i], M[j] = M[j], M[i]
                        i = j
                    else:
                        return M


def K_sum(L, K):
    ''' you need to find the sum of smallest K elements
        of L using a MagicList. Return the sum.
        Write your code after this comment.
    '''
    M = MagicList()
    for i in L:
        M.insert(i)
    sum = 0
    for i in range(K):
        sum = sum + M.findMin()
        M.deleteMin()
    return sum


if __name__ == "__main__":
    '''Here are a few test cases'''

    '''insert and findMin'''
    M = MagicList()
    M.insert(4)
    M.insert(3)
    M.insert(5)
    x = M.findMin()
    if x == 3:
        print("testcase 1 : Passed")
    else:
        print("testcase 1 : Failed")

    '''deleteMin and findMin'''
    M.deleteMin()
    x = M.findMin()
    if x == 4:
        print("testcase 2 : Passed")
    else:
        print("testcase 2 : Failed")

    '''k-sum'''
    L = [2, 5, 8, 3, 6, 1, 0, 9, 4]
    K = 4
    x = K_sum(L, K)
    if x == 6:
        print("testcase 3 : Passed")
    else:
        print("testcase 3 : Failed")
