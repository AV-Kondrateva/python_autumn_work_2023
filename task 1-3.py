x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
a = (x+y)
b = (x-y)
c = (x*y)
d = (x/y)
e = (x//y)
if(a > b and a > c and a > d and a < e):
    print(f"вторым по величине является результат сложения чисел, равный {a}")
if (a > b and a > c and a > e and a < d):
    print(f"вторым по величине является результат сложения чисел, равный {a}")
if (a > b and a > e and a > d and a < c):
    print(f"вторым по величине является результат сложения чисел, равный {a}")
if (a > c and a > d and a > e and a < b):
    print(f"вторым по величине является результат сложения чисел, равный {a}")
if (b > a and b > c and b > d and b < e):
    print(f"вторым по величине является результат вычитания чисел, равный {b}")
if (b > a and b > c and b > e and b < d):
    print(f"вторым по величине является результат вычитания чисел, равный {b}")
if (b > a and b > e and b > d and b < c):
    print(f"вторым по величине является результат вычитания чисел, равный {b}")
if (b > c and b > d and b > e and b < a):
    print(f"вторым по величине является результат вычитания чисел, равный {b}")
if (c > a and c > b and c > d and c < e):
    print(f"вторым по величине является результат умножения чисел, равный {c}")
if (c > a and c > b and c > e and c < d):
    print(f"вторым по величине является результат умножения чисел, равный {c}")
if (c > a and c > e and c > d and c < b):
    print(f"вторым по величине является результат умножения чисел, равный {c}")
if (c > b and c > d and c > e and c < a):
    print(f"вторым по величине является результат умножения чисел, равный {c}")
if (d > a and d > b and d > c and d < e):
    print(f"вторым по величине является результат деления с остатком чисел, равный {d}")
if (d > a and d > b and d > e and d < c):
    print(f"вторым по величине является результат деления с остатком чисел, равный {d}")
if (d > a and d > e and d > c and d < b):
    print(f"вторым по величине является результат деления с остатком чисел, равный {d}")
if (d > b and d > e and d > c and d < a):
    print(f"вторым по величине является результат деления с остатком чисел, равный {d}")
if (e > a and e > b and e > c and e < d):
    print(f"вторым по величине является результат целочисленного деления чисел, равный {e}")
if (e > a and e > b and e > d and e < c):
    print(f"вторым по величине является результат целочисленного деления чисел, равный {e}")
if (e > a and e > d and e > c and e < b):
    print(f"вторым по величине является результат целочисленного деления чисел, равный {e}")
if (e > b and e > c and e > d and e < a):
    print(f"вторым по величине является результат целочисленного деления чисел, равный {e}")
