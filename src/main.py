import re


print('hello world');
print('you HERE');

x = 10; # int (целое число)
x = "asd"; # теперь str (строка)'

# print(x);

a = 732312313
b = 3
# print(a // b); # 2 (целочисленное деление)

# print(a % b) # 1 (остаток)

is_admin = True

if is_admin:
    print("Добро пожаловать!")


s = "AppSec"
# print("Sec" in s)

name = "Анна"
# print(f"Пользователь {name} вошёл")


payload = {"limit": "10", "admin": "true"} # пришло как строки
limit = int(payload.get("limit", 10))
admin = payload.get("admin", "true").lower() == "true"

# print(limit, admin)

class Solution:


    def romanToInt(self, s: str) -> int:
        allDate = {
                "I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000,
            }

        result = 0
        oldLetter = 0;
        currentLetter = 0;
        for letter in s:
            currentLetter = allDate[letter]

            if currentLetter > oldLetter:
                # Отменяем прошлое прибавление oldLetter и вычитаем его
                result += currentLetter - 2 * oldLetter
                
            else:
                result += currentLetter


            oldLetter = currentLetter


        return result


processor = Solution()

# print(processor.romanToInt('MMMDCCCXLIX'))  # Выведет: 3849
print(processor.romanToInt('MCMXCIV'))      # Выведет: 1994



password_chars = [
    {
        'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72,
        'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80,
        'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88,
        'Y': 89, 'Z': 90
    },
    {
        'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104,
        'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112,
        'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120,
        'y': 121, 'z': 122
    },
    {
        '0': 48, '1': 49, '2': 50, '3': 51, '4': 52,
        '5': 53, '6': 54, '7': 55, '8': 56, '9': 57
    },
    {
        '!': 33, '@': 64, '#': 35, '$': 36,
        '%': 37, '^': 94, '&': 38, '*': 42
    }
]

