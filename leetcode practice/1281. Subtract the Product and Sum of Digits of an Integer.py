'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.


Example 1:

Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21
'''


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        summ = 0
        product = 1

        for i in num:
            i = int(i)
            summ += i
            product *= i

        return product - summ

#ALTERNATIVE SOLUTION

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Product = 1
        Sum = 0

        for i in list(map(int, str(n))):
            Product *= i
            Sum += i

        return Product - Sum