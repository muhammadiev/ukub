# import random
# from logic import *
#
# def generate_question(mode):
#     if mode == "2_ekub":
#         a, b = random.randint(10, 9999), random.randint(10, 9999)
#         return f"EKUB({a}, {b}) = ?", ekub(a, b)
#
#     if mode == "2_ekuk":
#         a, b = random.randint(10, 9999), random.randint(10, 9999)
#         return f"EKUK({a}, {b}) = ?", ekuk(a, b)
#
#     if mode == "3_ekub":
#         a, b, c = random.randint(10, 9999), random.randint(10, 9999), random.randint(10, 9999)
#         return f"EKUB({a}, {b}, {c}) = ?", ekub3(a, b, c)
#
#     if mode == "3_ekuk":
#         a, b, c = random.randint(10, 999), random.randint(10, 999), random.randint(10, 999)
#         return f"EKUK({a}, {b}, {c}) = ?", ekuk3(a, b, c)
#
#     if mode == "nbs":
#         n = random.randint(10, 999)
#         return f"{n} sonining natural bo‘luvchilari soni (NBS) qancha?", nbs(n)
#
#     if mode == "ubs":
#         a, b = random.randint(10, 999), random.randint(10, 999)
#         return f"{a} va {b} sonlarining umumiy bo‘luvchilari soni (UBS) qancha?", ubs(a, b)
#
#     if mode == "nby":
#         n = random.randint(10, 999)
#         return f"{n} sonining bo‘luvchilari yig‘indisi (NBY) qancha?", nby(n)
#
#     if mode == "aralash":
#         mode = random.choice(["2_ekub", "2_ekuk", "3_ekub", "3_ekuk", "nbs", "ubs", "nby"])
#         return generate_question(mode)


import random
from logic import *

def generate_question(mode):
    if mode == "2_ekub":
        while True:
            a, b = random.randint(10, 9999), random.randint(10, 9999)
            result = ekub(a, b)
            if result > 1:
                return f"EKUB({a}, {b}) = ?", result

    if mode == "2_ekuk":
        while True:
            a, b = random.randint(10, 9999), random.randint(10, 9999)
            result = ekuk(a, b)
            # Skip trivial cases like EKUK = a*b (coprime)
            if result != a * b:
                return f"EKUK({a}, {b}) = ?", result

    if mode == "3_ekub":
        while True:
            a, b, c = random.randint(10, 9999), random.randint(10, 9999), random.randint(10, 9999)
            result = ekub3(a, b, c)
            if result > 1:
                return f"EKUB({a}, {b}, {c}) = ?", result

    if mode == "3_ekuk":
        while True:
            a, b, c = random.randint(10, 999), random.randint(10, 999), random.randint(10, 999)
            result = ekuk3(a, b, c)
            if result != a * b * c:
                return f"EKUK({a}, {b}, {c}) = ?", result

    if mode == "nbs":
        n = random.randint(10, 999)
        return f"{n} sonining natural bo‘luvchilari soni (NBS) qancha?", nbs(n)

    if mode == "ubs":
        while True:
            a, b = random.randint(10, 999), random.randint(10, 999)
            result = ubs(a, b)
            if result > 1:  # Avoid UBS=1 cases
                return f"{a} va {b} sonlarining umumiy bo‘luvchilari soni (UBS) qancha?", result

    if mode == "nby":
        n = random.randint(10, 999)
        return f"{n} sonining bo‘luvchilari yig‘indisi (NBY) qancha?", nby(n)

    if mode == "aralash":
        mode = random.choice(["2_ekub", "2_ekuk", "3_ekub", "3_ekuk", "nbs", "ubs", "nby"])
        return generate_question(mode)
