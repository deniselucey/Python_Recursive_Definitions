#Recursive towers of hanoi function

def hanoi(n, fr, to, spare):

    def print_move(fr, to):
        print ("- Move top ring in %s tower to the %s tower" % (fr, to))

    if n == 1:
        print_move(fr, to)

    else:
        hanoi(n-1, fr, spare, to)
        hanoi(1, fr, to, spare)
        hanoi(n-1, spare, to, fr)

hanoi(2, "Middle", "Left", "Right")