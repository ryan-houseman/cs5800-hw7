class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort balloons based on the right endpoint of the balloon
        balloons = sorted(points, key=lambda x: x[1])

        arrows = 0
        cur_right = float('inf')*-1
        for i in range(len(balloons)):
            left = balloons[i][0]
            right = balloons[i][1]
            if left > cur_right:
                arrows += 1
                cur_right = right
        print('Minimum Number of Arrows Required: ' + str(arrows))
        return(arrows)
    
###############################################################
# Test Case A:
print('Test Case A:')
test_a = Solution()
test_a.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])

# Test Case B:
print('\nTest Case B:')
test_b = Solution()
test_b.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
