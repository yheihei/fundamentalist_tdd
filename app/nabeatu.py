class Nabeatu:
    def __init__(self, num):
        if type(num) != int:
            raise ValueError("数字を入れてください")
        if num <= 0:
            raise ValueError("1以上の数値を入れてください")
        self.num = num

    def call(self):
        if self.num % 3 == 0:
            return f"{self.num}(バカ)"
        if  "3" in str(self.num):
            return f"{self.num}(バカ)"
        return self.num
