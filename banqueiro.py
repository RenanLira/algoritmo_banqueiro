
class Banqueiro:
    def __init__(self, re, rd, mc, mr):
        self.recursos_existentes = re.split(' ')
        self.recursos_disponiveis = list(map(lambda x: int(x), rd.split(' ')))
        self.matriz_corrente = mc
        self.matriz_requisicoes = mr

    def exec(self):
        for i in range(len(self.matriz_requisicoes)):
            indice = projeto.procurar()
            if indice == -1:
                print('deadlock')
                break

            print(indice)
            print('disponiveis ', projeto.adicionar_disponiveis(indice))
            print ('processos ', projeto.excluir_requisicoes(indice))


    def procurar(self):
        indice = 0
        for requisicoes in self.matriz_requisicoes:
            check = 0
            count = 0
            for p in requisicoes:
                if p <= int(self.recursos_disponiveis[count]) + self.matriz_corrente[indice][count]:
                    check += 1
                count += 1

            if check == len(requisicoes):
                return indice

            indice += 1

        return -1


    def excluir_requisicoes(self, indice):
        del self.matriz_requisicoes[indice]
        del self.matriz_corrente[indice]

        return self.matriz_requisicoes


    def adicionar_disponiveis(self, indice):
        adc = self.matriz_corrente[indice]

        for i in range(len(self.recursos_disponiveis)):
            self.recursos_disponiveis[i] += adc[i]

        return self.recursos_disponiveis


if __name__ == "__main__":
    obj = {
        'recursos exis': '4 2 3 1',
        'recursos disp': '2 1 0 0',
        'matriz corrente': 
        [[0, 0, 1, 0],
                         [2, 0, 0, 1],
                         [0, 1, 2, 0]],
        'matriz requisicoes': 
        [[2, 0, 0, 1],
                         [1, 0, 1, 0],
                         [2, 1, 0, 0]]
        
    }
    projeto = Banqueiro(*obj.values())

    
    projeto.exec()
