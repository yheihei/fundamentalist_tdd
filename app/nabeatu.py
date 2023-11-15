class Nabeatu:
    def __init__(self, num):
        self.num = num

    def call(self):
        if self.num % 3 == 0:
            return f"{self.num}(バカ)"
        return self.num
