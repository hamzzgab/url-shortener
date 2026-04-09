class Base62:
    __CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encoder(self, url_id, base=62):
        if url_id < 0:
            raise ValueError("Value less than 0")
        if url_id < base:
            return self.__CHARS[url_id]
        return self.encoder(url_id // base, base) + self.__CHARS[url_id % base]

    def decoder(self, code, base=62):
        res, length = 0, len(code)
        for i, val in enumerate(code):
            power = (length - i - 1)
            res += self.__CHARS.find(val) * base ** power
        return res
