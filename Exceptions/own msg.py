def check(val):
    if val < 0:
        raise ValueError("Negative!")
    else:
        print("OK")

try:
    check(-1)
except ValueError as e:
    print("Error:", e)

try:
    check(5)
except ValueError as e:
    print("Error:", e)