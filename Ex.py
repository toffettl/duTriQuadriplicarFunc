num = input("Escolha um número: ")
num = int(num)

def criarMulticador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criarMulticador(2)
triplicar = criarMulticador(3)
quadruplicar = criarMulticador(4)

print(duplicar(num), triplicar(num), quadruplicar(num))

