class Morse:
    def __init__(self):
        self.dict = {
            'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.',
            'G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..',
            'M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.',
            'S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-',
            'Y': '-.--','Z': '--..','1': '.----','2': '..---','3': '...--',
            '4': '....-','5': '.....','6': '-....','7': '--...','8': '---..',
            '9': '----.','0': '-----','?': '..--..','/': '-..-.','()': '-.--.-',
            '-': '-....-','.': '.-.-.-',
        }
        self.dict_convert = {}
        for k, v in self.dict.items():
            self.dict_convert[v] = k

    def encode(self, context, sep=' '):
        if not type(context) == str:
            return "Error context"
        context = context.upper()

        result = ''
        for i in context:
            if i not in self.dict:
                result += i + sep
                continue
            result += self.dict[i] + sep
        return result.strip()

    def decode(self, context, sep=' '):
        if not type(context) == str:
            return "Error context"

        content = context.split(sep)
        result = ''
        for i in content:
            if i not in self.dict_convert:
                if not i:
                    continue
                result += '#'
                continue
            result += self.dict_convert[i]
        return result


if __name__ == '__main__':
    m = Morse()
    print(m.decode('.. ... .... .. --.. .- .. -.. .- - ..'))
    print(m.encode('ishizaidati'))