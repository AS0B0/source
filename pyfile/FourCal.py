class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def setdata(self, first, second): # 메서드
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

# FourCal을 상속 받음
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            result = self.first / self.second
            return result
