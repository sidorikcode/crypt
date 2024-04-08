class BidirectionalAlphabetDictionary:
    def __init__(self, alphabet1, alphabet2):
        self.__char_for_encrypt = {}
        self.__char_for_decrypt = {}
        if len(alphabet1) != len(alphabet2):
            raise Exception("Ошибка: алфавиты разной длинны!!!!!")
        

        for num, char in enumerate(alphabet1):
            char2 = alphabet2[num]

            self.__char_for_encrypt[char] = char2
            self.__char_for_decrypt[char2] = char

    def get_char_for_encrypt(self, char):
        return self.__char_for_encrypt.get(char, char)

    def get_char_for_decrypt(self, char):
        return self.__char_for_decrypt.get(char, char)
    

ALPHABET1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя "
ALPHABET2 = "лджщ шгзоаюьчйътцыпхрсуикфмбнвэея"

class SimpleSubstitutionCipher:
    def __init__(self, alphabet1=ALPHABET1, alphabet2=ALPHABET2):
        self.__bidirectional_dict = BidirectionalAlphabetDictionary(alphabet1, alphabet2)

    def encrypt(self, message):
        return ''.join(self.__bidirectional_dict.get_char_for_encrypt(char) for char in message.lower())
        
    def decrypt(self, encrypted_message):
        return ''.join(self.__bidirectional_dict.get_char_for_decrypt(char) for char in encrypted_message.lower())       



# MARK: - Example
    
print("Начало работы")
cipher = SimpleSubstitutionCipher()
original_message = "Ночной ёж!"

print("\nОткрытый текст")
print(original_message)

encrypted_message = cipher.encrypt(original_message)
print("\nШифротекст")
print(encrypted_message)


decrypted_message = cipher.decrypt(encrypted_message)
print("\nРасшифрованный шифротекст")
print(decrypted_message)