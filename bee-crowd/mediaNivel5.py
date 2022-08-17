notas = input().split(" ")

n1, n2, n3, n4 = notas

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

print("Media: %.1f" % media)

if media >= 7.0:
    print("Aluno aprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")

    exame = float(input())
    print("Nota do exame: %.1f" % exame)

    mediaFinal = (exame + media) / 2

    if mediaFinal >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: %.1f" % mediaFinal)
elif media < 5.0:
    print("Aluno reprovado.")
