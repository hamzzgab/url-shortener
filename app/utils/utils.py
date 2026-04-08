class Base62:
    __CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    @staticmethod
    def encoder(self, _id, base=62):
        if _id < 0:
            raise ValueError("Value less than 0")
        if _id < base:
            return self.__CHARS[_id]
        return self.encoder(_id // base, base) + self.__CHARS[_id % base]

    @staticmethod
    def decoder(self, code, base=62):
        res, length = 0, len(code)
        for i, val in enumerate(code):
            power = (length - i - 1)
            res += self.__CHARS.find(val) * base ** power
        return res
