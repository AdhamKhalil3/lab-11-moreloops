def move(f, t):
    print("move disc from {} to {}".format(f, t))
def Hanoi(n, f, h, t):

    if n == 0:
        pass
    else:
        Hanoi(n - 1, f, t, h)
        move(f, t)
        Hanoi(n - 1, h, f, t)

Hanoi(4, "A", "B", "C")


