import random
class BaseCipher(object):
    def encrypt(s):
        raise NotImplementedError
    def decrypt(s):
        raise NotImplementedError

class PassThroughCipher(BaseCipher):
    def __init__(self):
        self.r = []
    def encrypt(self,s):
        t = ''
        for line in s:
            for l in line:
                if l == '':
                    t = t + chr(32)
                else:
                    x = random.randint(33,126)
                    t = t + chr(ord(l) + x)
                    self.r.append(x)          
        return t
    def decrypt(self,s):
        t = ''
        for line in s:
            for l in line:
                if l == '':
                    t = t + chr(32)
                else:
                    t = t + chr(ord(l) - self.r[0])
                    print self.r
                    self.r = self.r[1:]
        return t
            

a = PassThroughCipher()
x = raw_input()
i = a.encrypt(x)
j = a.decrypt(i)
