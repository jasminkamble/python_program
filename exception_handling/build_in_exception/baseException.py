try:
    num = 10 / 0
except BaseException as e:
    print("Caught:", e)
