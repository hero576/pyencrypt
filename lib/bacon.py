class Bacon:
    """
    培根密码
    """

    def __init__(self):
        self.dict = {}
        self.dict_convert = {}
        for i, key in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            value = ('%05d' % int(str(bin(i)).replace('0b', ''))).replace('0', 'A').replace('1', 'B')
            self.dict[key] = value
            self.dict_convert[value] = key
        print(self.dict)
        print(self.dict_convert)

    def encode(self, context):
        if not type(context) == str:
            return "Error context"
        context = context.upper()
        result = ''
        for i in context:
            if i not in self.dict:
                result += i
                continue
            result += self.dict[i]
        return result

    def decode(self, context):
        if not type(context) == str:
            return "Error context"
        context = context.upper()
        if not (len(context) % 5 == 0):
            context = context[:-(context % 5)]
        length = int(len(context) / 5)
        result = ''
        for i in range(length):
            if context[i * 5:i * 5 + 5] not in self.dict_convert:
                result += ''
                continue
            result += self.dict_convert[context[i * 5:i * 5 + 5]]
        return result


if __name__ == '__main__':
    b = Bacon()
    print(b.encode('MICAILILARHIRHEMLE'))
    print(b.decode('ABBAAABAAAAAABAAAAAAABAAAABABBABAAAABABBAAAAABAAABAABBBABAAABAAABAABBBAABAAABBAAABABBAABAA'))
