from lib.caesar import Caesar


class Virginia:
    """
    维吉尼亚密码
    """

    def __init__(self):
        self.dict = {}
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        for i in range(len(alphabet)):
            self.dict[alphabet[i]] = i
        self.caesar = Caesar()

    def parse(self, context, salt, mode):
        if not type(context) == str and not type(salt) == str:
            return "Error context"
        context = context.upper()
        salt = salt.upper()

        if salt == '':
            return context

        n = int(len(context) / len(salt)) + 1
        salt = (salt * n)[:len(context)]

        result = ''
        index = 0
        for i in context:
            if mode == 'encode':
                offset = self.dict[salt[index]]
            else:
                offset = len(self.dict) - self.dict[salt[index]]

            result += self.caesar.encode(i, offset)
            if i in self.caesar.dict:
                index += 1

        return result.lower()

    def decode(self, context, salt):
        return self.parse(context, salt, 'decode')

    def encode(self, context, salt):
        return self.parse(context, salt, 'encode')


if __name__ == '__main__':
    v = Virginia()
    print(v.decode('DBMJOHQZXBQ', 'WJNY'))
