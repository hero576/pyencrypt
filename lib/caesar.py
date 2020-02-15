class Caesar:
    """
    凯撒密码
    """

    def __init__(self):
        self.dict = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    def encode(self, context, offset=0):
        if not type(context) == str:
            return "Error context"

        context = context.upper()
        result = ''

        for i in context:
            if i not in self.dict:
                result += i
                continue

            index = self.dict.index(i)
            index = (index + offset) % len(self.dict)

            result += self.dict[index]
        return result

    def decode(self, context):
        for i in range(26):
            result = self.encode(context, i).lower()
            print('offset:{}\t{}'.format(i, result))


if __name__ == '__main__':
    c = Caesar()
    c.decode("EBIIL TLOIA")
    print(c.encode("hello WORLD", -3))
