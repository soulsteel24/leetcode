class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # result = [[0 for _ in range(n)]for _ in range(n)]

        # for i in range(n):
        #     for j in range(n):
        #         result[j][n-1-i] = matrix[i][j]
        # return result

        n = len(matrix)

        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n):
            matrix[i].reverse()