# Classe Local que representa um nó
class Local:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'local': vizinho})

# Função de busca em profundidade limitada
def buscaEmProfundidadeLimitada(inicio, objetivo, limiteProfundidade):
    pilha = []
    visitados = set()

    pilha.append({'no': inicio, 'profundidade': 0})
    visitados.add(inicio)

    while pilha:
        atual = pilha.pop()

        no = atual['no']
        profundidade = atual['profundidade']

        print(f"Visitando o local: {no.nome}")

        if no.nome == objetivo.nome:
            print(f"Objetivo encontrado: {no.nome}")
            return True

        if profundidade >= limiteProfundidade:
            continue

        for vizinho in reversed(no.vizinhos):
            local_vizinho = vizinho['local']
            if local_vizinho not in visitados:
                pilha.append({'no': local_vizinho, 'profundidade': profundidade + 1})
                visitados.add(local_vizinho)

    return False

# Função de busca em profundidade iterativa
def buscaProfundidadeIterativa(inicio, objetivo):
    limiteProfundidade = 0

    while True:
        print(f"Tentando com limite de profundidade: {limiteProfundidade}")

        encontrado = buscaEmProfundidadeLimitada(inicio, objetivo, limiteProfundidade)

        if encontrado:
            print(f"Objetivo encontrado com limite de profundidade {limiteProfundidade}")
            return True
        else:
            print(f"Objetivo não encontrado com limite de profundidade {limiteProfundidade}")
            limiteProfundidade += 1

# Grafo
localArad = Local("Arad")
localZerind = Local("Zerind")
localOradea = Local("Oradea")
localSibiu = Local("Sibiu")
localTimisoara = Local("Timisoara")
localLugoj = Local("Lugoj")
localMehadia = Local("Mehadia")
localDobreta = Local("Dobreta")
localCraiova = Local("Craiova")
localRimnicuVilcea = Local("Rimnicu Vilcea")
localFagaras = Local("Fagaras")
localPitesti = Local("Pitesti")
localBucharest = Local("Bucharest")
localGiurgiu = Local("Giurgiu")
localUrziceni = Local("Urziceni")
localHirsova = Local("Hirsova")
localEforie = Local("Eforie")
localVaslui = Local("Vaslui")
localIasi = Local("Iasi")
localNeamt = Local("Neamt")

# Adicionando os vizinhos
localArad.adicionarVizinho(localTimisoara)
localArad.adicionarVizinho(localSibiu)
localArad.adicionarVizinho(localZerind)

localZerind.adicionarVizinho(localArad)
localZerind.adicionarVizinho(localOradea)

localOradea.adicionarVizinho(localSibiu)
localOradea.adicionarVizinho(localZerind)

localSibiu.adicionarVizinho(localArad)
localSibiu.adicionarVizinho(localRimnicuVilcea)
localSibiu.adicionarVizinho(localFagaras)
localSibiu.adicionarVizinho(localOradea)

localTimisoara.adicionarVizinho(localArad)
localTimisoara.adicionarVizinho(localLugoj)

localLugoj.adicionarVizinho(localMehadia)
localLugoj.adicionarVizinho(localTimisoara)

localMehadia.adicionarVizinho(localDobreta)
localMehadia.adicionarVizinho(localLugoj)

localDobreta.adicionarVizinho(localCraiova)
localDobreta.adicionarVizinho(localMehadia)

localCraiova.adicionarVizinho(localDobreta)
localCraiova.adicionarVizinho(localPitesti)
localCraiova.adicionarVizinho(localRimnicuVilcea)

localRimnicuVilcea.adicionarVizinho(localSibiu)
localRimnicuVilcea.adicionarVizinho(localPitesti)
localRimnicuVilcea.adicionarVizinho(localCraiova)

localFagaras.adicionarVizinho(localSibiu)
localFagaras.adicionarVizinho(localBucharest)

localPitesti.adicionarVizinho(localCraiova)
localPitesti.adicionarVizinho(localRimnicuVilcea)
localPitesti.adicionarVizinho(localBucharest)

localBucharest.adicionarVizinho(localFagaras)
localBucharest.adicionarVizinho(localPitesti)
localBucharest.adicionarVizinho(localGiurgiu)
localBucharest.adicionarVizinho(localUrziceni)

localGiurgiu.adicionarVizinho(localBucharest)

localUrziceni.adicionarVizinho(localBucharest)
localUrziceni.adicionarVizinho(localHirsova)
localUrziceni.adicionarVizinho(localVaslui)

localHirsova.adicionarVizinho(localUrziceni)
localHirsova.adicionarVizinho(localEforie)

localEforie.adicionarVizinho(localHirsova)

localVaslui.adicionarVizinho(localUrziceni)
localVaslui.adicionarVizinho(localIasi)

localIasi.adicionarVizinho(localVaslui)
localIasi.adicionarVizinho(localNeamt)

localNeamt.adicionarVizinho(localIasi)

resultado = buscaProfundidadeIterativa(localArad, localBucharest)

if resultado:
    print("Caminho encontrado!")
else:
    print("Caminho não encontrado!")
