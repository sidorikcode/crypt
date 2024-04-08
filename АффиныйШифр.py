from functools import partial

class BidirectionalAlphabetDictionary:
    def __init__(self, string):
        self.__char_for_num = {}
        self.__num_for_char = {}

        for num, char in enumerate(string):
            self.__char_for_num[num] = char
            self.__num_for_char[char] = num

    def get_char(self, num):
        return self.__char_for_num.get(num)

    def get_num(self, char):
        return self.__num_for_char.get(char)


class ExtendedEuclidAlgorithm:
    def __init__(self, number_1, number_2):
        init_a = max(number_1, number_2)
        init_b = min(number_1, number_2)

        result = self.__main_method(init_a, init_b)
        self.d = result[0]
        self.y2 = result[1]

    def __main_method(self, init_a, init_b):
        q = None
        r = None
        y = None
        a = init_a
        b = init_b
        y2 = 0
        y1 = 1

        while b != 0:
            q = a // b
            r = a % b
            y = y2 - (q * y1)
            a = b
            b = r
            y2 = y1
            y1 = y
        
        if y2 < 0:
            y2 += init_a
        return (a, y2)
    
    # MARK: - Public methods

    def get_revert_a(self):
        if self.d > 1:
            return None
        else:
            return self.y2
    
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ .,?!():;-+*\/\"'"
class AffineCipher: 
    def __init__(self, a, b, alphabet = ALPHABET):
        self.__m = len(alphabet)
        self.__a = self.__check_a(a, self.__m)
        self.__b = b % self.__m
        self.__bidirectional_alphabet_dict = BidirectionalAlphabetDictionary(alphabet)

    def __check_a(self, a, m):
        _a = a % m
        result_euclid_algorinm = ExtendedEuclidAlgorithm(_a, m)
        d = result_euclid_algorinm.d
        while d != 1:
            _a += 1
            _a = _a % m
            d = ExtendedEuclidAlgorithm(_a, m).d
        
        return _a
    
    def __encrypt_char(self, char, a, b):
        num = self.__bidirectional_alphabet_dict.get_num(char)

        if num is not None:
            new_num = ((a * num) + b) % self.__m
            return self.__bidirectional_alphabet_dict.get_char(new_num)
        else:
            return char
        
    def __decrypt_char(self, char, revert_a, b):
        num = self.__bidirectional_alphabet_dict.get_num(char)

        if num is not None:
            new_num = ((num - b) * revert_a) % self.__m
            return self.__bidirectional_alphabet_dict.get_char(new_num)
        else:
            return char
        
    # MARK: - Public methods
        
    def encrypt(self, message):
        return "".join(map(partial(self.__encrypt_char, a=self.__a, b=self.__b), message))
    
    def decrypt(self, encrypted_message):
        result_euclid_algorinm = ExtendedEuclidAlgorithm(self.__a, self.__m)
        revert_a = result_euclid_algorinm.get_revert_a()
        if revert_a is not None:
            return "".join(map(partial(self.__decrypt_char, revert_a=revert_a, b=self.__b), encrypted_message))
        else:
            raise Exception("Ошибка: нет обратного значения!!!!!")
    

# MARK: - Example

print("Начало работы")
affine_cipher = AffineCipher(11, 30)
original_massage = "Ночной ёж!"

print("\nОткрытый текст")
print(original_massage)

encrypt_massage = affine_cipher.encrypt(original_massage)
print("\nШифротекст")
print(encrypt_massage)

dercypt_massage = affine_cipher.decrypt(encrypt_massage)
print("\nРасшифрованный шифротекст")
print(dercypt_massage)