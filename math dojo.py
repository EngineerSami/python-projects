class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self

md = MathDojo()

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x) 

result1 = md.add(10).subtract(5).add(3, 7).subtract(2, 1).result
print(result1) 

result2 = md.add(100).subtract(50, 25).add(10).result
print(result2) 
