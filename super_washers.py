class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """

        dresses = sum(machines)
        n = len(machines)
        if dresses % n != 0:
            return (-1)
        
        moves = []
        s_left = 0
        ideal = dresses/n
        for i in range(len(machines)):
            m = machines[i]
            s = m - ideal
            s_right = (s_left + s)*-1
            if s_left == 0:
                moves.append(abs(s))
            elif (s_left > 0 and s_right > 0):
                moves.append(max([s_left,s_right]))
            elif (s_left < 0 and s_right < 0):
                moves.append(abs(s))
            else:
                moves.append(max([abs(s_left),abs(s_right)]))
            s_left = s_right*-1
        
        print(moves)
        return(max(moves))

            
            
        

#################################################################

# Test Case A:
print('Test Case A:')
test_a = Solution()
test_a.findMinMoves([10,16,2,8,3,6,7,12])

#Test Case B:
print('\nTest Case B:')
test_b = Solution()
test_b.findMinMoves([9,1,8,8,9])
