def basic(a):
    suma = 1
    steps = 0
    while a > 10:
        steps += 1
        print(a)
        for digit in str(a):
            suma *= int(digit)
            a = suma
        suma = 1
    print("Steps:\t" + str(steps))


def findbiggest(a):
    b = int(a/10)
    originala = a
    maxstep = 0
    maxnumb = 0
    while b < originala + 1:
        a = b
        suma = 1
        steps = 0
        while a > 10:
            steps += 1
            print(a)
            for digit in str(a):
                suma *= int(digit)
                a = suma
            suma = 1
        if maxstep < steps:
            maxstep = steps
            maxnumb = b
        print("Number:\t" + str(b) + "\t" + "Steps:\t" + str(steps))
        b += 1
    print("\n\n"+"Biggest number:\t" + str(maxnumb) +"\t"+ "Steps:\t" + str(maxstep))


findbiggest(10000000)
