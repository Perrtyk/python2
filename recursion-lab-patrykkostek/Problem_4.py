# Patryk Kostek
# Lab 2 Problem 3
def towerOfHanoi(n, a, b, c):
    """
    :param n: Number of plates in the game.
    :param a: Stick a
    :param b: Stick b
    :param c: Stick c
    :return: end
    """
    if n == 1:
        print ("Move disk 1 from", a, "to", c)
        return
    towerOfHanoi(n - 1, a, c, b)
    print("Move disk", n, "from", a, "to", c)
    towerOfHanoi(n - 1, b, a, c)


def main(plates):
    towerOfHanoi(plates, "A", "B", "C")


if __name__ == '__main__':
    print('Welcome to Tower of Hanoi\n')
    disks = input('How many disks would you like to start with: ')
    main(int(disks))

# This problem was a lot more challenging but after reviewing multiple resources I gained the understanding to solve it.
# This problem has a base case of 1, with the last action being moving the disk 1 from stick a to c as this is the final
# step to solve this problem, not matter how many plates are being played. From there, we apply 2 more steps and continue
# the recursion until the solution is found given the plates in the game. This was very challenging but manageable to find
# a solution.