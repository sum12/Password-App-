
class BaseCipher(object)
    def encrypt(s):
        raise NotImplementedError
    def decrypt(s):
        raise NotImplementedError


class PassThroughCipher(BaseCipher):
    def encrypt(s):
        return s:
    def descrypt(s):
        return s
