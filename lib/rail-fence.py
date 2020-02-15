class RailFence:
    """
    栅栏密码
    """

    @staticmethod
    def encode(context, offset):
        if not type(context) == str:
            return "Error context"
        if offset <= 1 or offset >= len(context):
            return context
        context = context.upper().replace(' ', '')
        length = int(len(context) / offset) + 1
        content = []
        for i in range(length):
            item = context[i * offset:i * offset + offset]
            content.append(item)
        result = ''
        for index in range(offset):
            result += ''.join([i[index] for i in content if len(i) > index])
        return result.lower()

    @staticmethod
    def decode(context, offset):
        if not type(context) == str:
            return "Error context"
        if offset <= 1 or offset >= len(context):
            return context
        context = context.upper().replace(' ', '')
        length = int(len(context) / offset) if len(context) % offset == 0 else int(len(context) / offset) + 1
        content = []
        for i in range(offset):
            item = context[i * length:i * length + length]
            content.append(item)
        result = ''
        for index in range(length):
            result += ''.join([i[index] for i in content if len(i) > index])
        return result.lower()

    def guess(self,context):
        for i in range(len(context)):
            print('{} {} '.format(i,self.decode(context,i)))

if __name__ == '__main__':
    r = RailFence()
    print(r.encode('you are beautiful', 2))
    print(r.decode('TEESCPEHRIAIHR', 2))
    print(r.decode('yurbatfloaeeuiu', 2))
    r.guess('BNAEZONUCBIIEH')