def get_height():
    height = 0
    while True:
        try:
            height = int(input("Height: "))
            if (height < 1 or height > 8):
                raise ValueError("Input is out of range.")
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break
    return height


height = get_height()
revised_height = height + 1

for i in range(1, revised_height):
    for k in range(1, revised_height - i):
        print(" ", end='')
    for j in range(1, i + 1):
        print("#", end='')
    print("  ", end='')
    for y in range(1, i + 1):
        print("#", end='')
    print("")
