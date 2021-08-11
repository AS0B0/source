# ex1, 2)

class Calculator:
    def __init__(self):
        self.value = 0
    def add(self, val):
        self.value += val

class upgradeCalculator(Calculator):
    def __init__(self):
        self.value = 0
    def minus(self, val):
        self.value -= val

class MaxLimitCalculator(Calculator):
	def add(self, val):
	    self.value += val
	    if self.value > 100:
	        self.value = 100

cal = MaxLimitCalculator()
cal.add(60)
cal.add(50)

print(cal.value)
