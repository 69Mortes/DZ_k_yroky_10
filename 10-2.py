# 2. Дано целое число n и находится в диапазоне от 1 до 99,
    # # число определяющее возраст человека в годах.
    # # Для этого числа необходимо напечатать фразу "мне n (лет/года/год)".
n1 = range(1, 100)  # число в диапазоне от 1 до 100.
print("Здравствуйте")  # обычное приветствие
let = int(input(" Введите ваш возраст :"))  # ввод значения
# будет год:
# '1', '21', '31', '41', '51', '61', '71', '81', '91'
if let == 1: # если введеное число равно 1, то
    print("вам ", let, "год")
if let > 20 and let <22:
    print("вам ", let, "год")
if let > 30 and let <32:
    print("вам ", let, "год")
if let > 40 and let <42:
    print("вам ", let, "год")
if let > 50 and let <52:
    print("вам ", let, "год")
if let > 50 and let <62:
    print("вам ", let, "год")
if let > 60 and let <72:
    print("вам ", let, "год")
if let > 70 and let <82:
    print("вам ", let, "год")
if let > 80 and let <92:
    print("вам ", let, "год")
# будет года:
# 2-4, 22-24, 32-34, 42-44, 52-54, 62-64, 72-74, 82-84, 92-94.
if let > 1 and let < 5:
    print('Вам', let, "года")
if let > 21 and let < 25:
    print('Вам', let, "года")
if let > 31 and let < 35:
    print('Вам', let, "года")
if let > 41 and let < 45:
    print('Вам', let, "года")
if let > 51 and let < 55:
    print('Вам', let, "года")
if let > 61 and let < 65:
    print('Вам', let, "года")
if let > 71 and let < 75:
    print('Вам', let, "года")
if let > 81 and let < 85:
    print('Вам', let, "года")
if let > 91 and let < 95:
    print('Вам', let, "года")
# будет лет:
# 5-20, 25-30, 35-40, 45-50, 55-60, 65-70, 75-80, 85-90, 95-100.
if let > 4 and let < 21:
    print('Вам', let, "лет")
if let > 24 and let < 31:
    print('Вам', let, "лет")
if let > 34 and let < 41:
    print('Вам', let, "лет")
if let > 44 and let < 51:
    print('Вам', let, "лет")
if let > 54 and let < 61:
    print('Вам', let, "лет")
if let > 64 and let < 71:
    print('Вам', let, "лет")
if let > 74 and let < 81:
    print('Вам', let, "лет")
if let > 84 and let < 91:
    print('Вам', let, "лет")
if let > 94 and let < 101:
    print('Вам', let, "лет")