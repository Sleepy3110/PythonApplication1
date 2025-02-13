﻿while True:
    try:
        a = int(input("Введите длину первого катета: "))
        b = int(input("Введите длину второго катета: "))

        if a <= 0 or b <= 0:
         raise ValueError("Длина катета должна быть положительным числом.")

        c = round(math.sqrt(a**2 + b**2), 2)
        P = a + b + c
        S = round(a * b / 2, 2)
        print("При указанных длинах катетов, которые равны ", a, " и ", b, " гипотенуза равна ",c)
        print("Периметр прямоугольного треугольника P равен", P)
        print("Площадь прямоугольного треугольника S равна", S)
        break

    except ValueError:
        print("Ошибка: Введенное значение не является целым числом. Пожалуйста, попробуйте снова.")
    continue