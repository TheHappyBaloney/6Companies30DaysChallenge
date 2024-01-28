# 273. Integer to English Words

class Solution:
    def __init__(self):
        
        self.ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine', ' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
        self.tens = ['', ' Ten', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
        self.thousands = ['', ' Thousand', ' Million', ' Billion']
    
    def helper(self, n: int) -> str:
        if n < 20:
            return self.ones[n]
        elif n < 100:
            return self.tens[n // 10] + self.helper(n % 10)
        elif n < 1000:
            return self.helper(n // 100) + ' Hundred' + self.helper(n % 100)
        else:
            for i in range(3, 0, -1):
                if n >= 1000 ** i:
                    return self.helper(n // (1000 ** i)) + self.thousands[i] + self.helper(n % (1000 ** i))
        return ''
    
    def numberToWords(self, num: int) -> str:
        #edge case
        if num == 0:
            return 'Zero'
        return self.helper(num).lstrip()
