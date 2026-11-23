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

            print(result, currentLetter, oldLetter)

            oldLetter = currentLetter


        return result


processor = Solution()

# print(processor.romanToInt('MMMDCCCXLIX'))  # Выведет: 3849
print(processor.romanToInt('MCMXCIV'))      # Выведет: 1994
