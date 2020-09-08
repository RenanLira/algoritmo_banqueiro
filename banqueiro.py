


class banqueiro:
    def __init__(self, re, rd, mc, mr):
        self.recursos_existentes = re.split(' ')
        self.recursos_disponiveis = rd.split(' ')
        self.matriz_corrente = mc
        self.matriz_requisicoes = mr

        
    def procurar(self):
        indice = 0
        for requisicoes in self.matriz_requisicoes:
            check = 0
            cont = 0
            for p in requisicoes:
                if p <= int(self.recursos_disponiveis[cont]):
                    check += 1
                cont+=1

            indice += 1

            if check == len(requisicoes):
                return requisicoes, indice

        return 'deadlock'


    def excluir_requisicoes(self, requisicao):
        for i in self.matriz_requisicoes:
            if i == requisicao:
                self.matriz_requisicoes.remove(i)

        return self.matriz_requisicoes


    def adicionar_disponiveis(self, indice):
        adc = self.matriz_corrente[indice-1]

        for i in range(len(self.recursos_disponiveis)):
            soma = int(self.recursos_disponiveis[i]) + adc[i]
            self.recursos_disponiveis[i] = soma

        return self.recursos_disponiveis






projeto = banqueiro('4 3 2 1', '2 1 0 0', [[0, 0, 1, 0], [2, 0, 0, 1], [0, 1, 2, 0]], [[2, 0, 0, 1], [1, 0, 1, 0], [2, 1, 0, 0]])


for i in range(3):
    rodar, indice = projeto.procurar()
    print(rodar)
    print(projeto.adicionar_disponiveis(indice))
    print(projeto.excluir_requisicoes(rodar))

