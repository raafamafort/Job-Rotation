num = int(input("Informa um número: "))
F = [0, 1]
c = 0
while F[-1] < num:
    F.append(F[c] + F[c+1])
    c += 1
if num in F:
    print(f"O número {num} pertence a sequencia de Fibonacci")
else:
    print(f"O número {num} NÃO pertence a sequencia de Fibonacci")