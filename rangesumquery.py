class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.total = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        self.total[0][0] = matrix[0][0]

        for j in range(1, len(matrix[0])):
            self.total[0][j] = self.total[0][j-1] + matrix[0][j]

        for i in range(1, len(matrix)):
            self.total[i][0] = self.total[i-1][0] + matrix[i][0]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.total[i][j] = self.total[i-1][j] + self.total[i][j-1] - self.total[i-1][j-1] + matrix[i][j]




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        print self.total

        if row1 == 0 and col1 == 0:
            return self.total[row2][col2]

        if row1 == 0 and col1 > 0:
            return self.total[row2][col2] - self.total[row1][col1-1]

        if row1 > 0 and col1 == 0:
            return self.total[row2][col2] - self.total[row1-1][col2]


        return self.total[row2][col2] - self.total[row1-1][col2] - self.total[row2][col1-1] + self.total[row1-1][col1-1]





        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)

so = NumMatrix([[7,7,0],[-4,-7,7],[-4,0,-2],[-8,-5,6]])

print so.sumRegion(1,0, 2, 2)