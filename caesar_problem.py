
class CeasarProblem:
    def __init__(self, name, step):
        # name = input("Enter you'r word: ")
        # step = int(input("Enter step: "))

        if type(name) != str:
            print("You should give a <class 'string'> not {}.".format(type(name)))
            return

        if type(step) != int:
            print("You should give a <class 'integer'> not {}.".format(type(step)))
            return

        self.name = name
        self.step = step

    def encoder(self):
        encode_name = ""
        for letter in  self.name :
            list_of_alphabet = [
                'a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y',
                'z']

            try:
                index = list_of_alphabet.index(letter.lower())
                encode_letter = list_of_alphabet[index + self.step]
                encode_name += encode_letter
                

            except:
                index = list_of_alphabet.index(letter.lower())
                encode_letter = list_of_alphabet[index + self.step - 26]
                encode_name += encode_letter
                
        return encode_name

    def decoder(self):
        decode_name = ""
        encode_name = self.encoder()

        for letter in  encode_name:
            list_of_alphabet = [
                'a','b','c','d','e',
                'f','g','h','i','j',
                'k','l','m','n','o',
                'p','q','r','s','t',
                'u','v','w','x','y',
                'z']

            try:
                index = list_of_alphabet.index(letter.lower())
                decode_letter = list_of_alphabet[index - self.step]
                decode_name += decode_letter
                

            except:
                index = list_of_alphabet.index(letter.lower())
                decode_letter = list_of_alphabet[index - self.step + 26]
                decode_name += decode_letter

        
        return decode_name

    def ceasar_name(self):

        primary_name = self.name
        encode_name = self.encoder()
        decode_name = self.decoder()

        print("primary name : ", primary_name)
        print("encode name : ", encode_name)
        print("decode name : ", decode_name)
        
        return