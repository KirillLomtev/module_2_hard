def find_password(n):
    result = ""
    for a in range(1, n):
        for b in range(a + 1, n + 1):
            if n % (a + b) == 0:
                result += str(a) + str(b)
    return result
n = int(input("Введите число от 3 до 20: "))
print("Пароль:", find_password(n))