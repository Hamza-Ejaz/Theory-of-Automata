class CFG:
    def __init__(self):
        self.i = 0
        self.word = ""

    def validate(self, word):
        self.word = word
        if self.S():
            result = (self.i == len(word)-1)  # minus one to remove $ endmarker
            self.reset()
            return result
        return False

    def reset(self):
        self.i = 0
        self.word = ""

    def char(self):
        return self.word[self.i]

    def S(self):
        if self.X() and self.Y() and self.Z():
            return True
        return False

    def X(self):
        if self.char() == 'a':
            self.i += 1
            if self.X():
                return True
        elif self.char() == 'b':
            self.i += 1
            return True
        return False

    def Y(self):
        if self.char() == 'b':
            self.i += 1
            if self.Y():
                return True
        elif self.char() == 'c':
            self.i += 1
            return True
        return False

    def Z(self):
        if self.char() == 'c':
            self.i += 1
            if self.Z():
                return True
        else:
            return True
        return False


a = CFG()
print(a.validate('bc$'))
print(a.validate('abc$'))
print(a.validate('ac$'))
print(a.validate('aabbbcc$'))
