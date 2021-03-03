"""
多项式计算
"""
class MaxSubseqSum():
    def MaxSubseqSum1(self, n):
        ThisSum = MaxSum = 0
        list A[] = (1, 2, 3, 4, 5, 6, 7, 8)
        for x in range(0, n-1):
            for y in range(0, n-1):
                ThisSum = 0
                for z in range():
                    ThisSum += A[z]
                if ThisSum > MaxSum:
                    MaxSum = ThisSum
        return MaxSum
