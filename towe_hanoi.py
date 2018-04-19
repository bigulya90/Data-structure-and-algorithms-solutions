def moveTowe(height, fromPole, toPole, withPole):
    if height >=1:
        moveTowe(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTowe(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("moving disk from",fp,"to",tp)



print moveTowe(4, "a", "b", "c")


