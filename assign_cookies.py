class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        s_ind = 0
        fed = 0
        for k in range(len(g)):
            greed = g[k]
            while s_ind <= len(s) - 1:
                size = s[s_ind]
                if greed <= size:
                    fed += 1
                    s_ind += 1
                    break
                s_ind += 1
        
        print('Number of kids with a cookie: ' + str(fed))
        return(fed)
    
##################################################
# Test Case A:
print('Test A:')
test_a = Solution()
test_a.findContentChildren([1,2,3],[3])

# Test Case B:
print('\nTest B:')
test_b = Solution()
test_b.findContentChildren([2,5,6,7,8,1,4,3],[3,6,8,3,2,5])