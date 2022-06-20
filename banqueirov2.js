

class Banqueiro{
    constructor(re, rd, mc=[], mr=[]){
        this.recursos_existentes = re.split(' ')
        this.recursos_disponiveis = rd.split(' ')
        this.matriz_corrente = mc
        this.matriz_requisicoes = mr
    }

    procura(){
        const resultado = this.matriz_requisicoes.map((v) => {

            let l = v.map((v,i) => v <= this.recursos_disponiveis[i])

            return l.sort()

        })

        return resultado.findIndex(v => v[0] == true)
    }

}


const banqueiro = new Banqueiro('4 3 2 1', '2 1 0 0',
[[0, 0, 1, 0],
 [2, 0, 0, 1],
 [0, 1, 2, 0]],
[[2, 0, 0, 1],
 [1, 0, 1, 0],
 [2, 1, 0, 0]])

console.log(banqueiro.procura())