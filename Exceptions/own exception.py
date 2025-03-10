class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

def check(val):
    if val < 0:
        raise MyError("Negative value!")
    print("OK")

try:
    check(-1)
except MyError as e:
    print("Error:", e.msg)

check(1)