class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key=lambda x: x[-1])
        arrow_pos = points[0][1]
        r = 1

        for i in range(1, len(points)):
            if not points[i][0] <= arrow_pos <= points[i][1]:
                r += 1
                arrow_pos = points[i][1]

        return r


sol = Solution()

points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(sol.findMinArrowShots(points))
