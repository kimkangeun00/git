for gugudan in range(2, 10):
    print("# %2d단 #" % gugudan, end=" ")
print()

for i in range(1, 10):
    for gugudan in range(2, 10):
        print("%2dX%2d=%2d" % (gugudan, i, gugudan * i), end=" ")
    print()
    