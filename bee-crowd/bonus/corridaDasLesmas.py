while True:
    try:
        qtdLesmas = int(input())
        velLesmas = input().split()
        maisVeloz = 0

        for i in range(qtdLesmas):
            if int(velLesmas[i]) > maisVeloz:
                maisVeloz = int(velLesmas[i])

        if maisVeloz < 10:
            nivel = 1
        elif maisVeloz >= 10 and maisVeloz < 20:
            nivel = 2
        else:
            nivel = 3
        print(nivel)

    except EOFError:
        break
