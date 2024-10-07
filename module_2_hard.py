a = int(input("Введите число от 3 до 20: "))
while True:
    if a < 3 or a > 20:
        print("Вы ввели неверное число, попробуйте еще раз:")
        a = int(input("Введите число от 3 до 20: "))
        continue
    break

str_ = ''
list_ = [a]

for i in range (3, a // 2 + 1):
    if a % i == 0:
        list_.append(i)

list_ = sorted(list_)

print(list_)

for i in range(1, 10):
    for j in list_:
        if i < j - i:
            str_ += str(i) + str(j - i)

print(str_)
