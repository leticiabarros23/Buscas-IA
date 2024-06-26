# Classe Local que representa um nó
class Local:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'local': vizinho})

# Função da busca em profundidade
def buscaEmProfundidade(inicio, objetivo):
    pilha = [] 
    visitados = set()

    pilha.append(inicio) # adiciona o nó inicial à pilha
    visitados.add(inicio) # marca o nó inicial como visitado

    while pilha:
        local = pilha.pop() # remove o último nó da pilha
        print(f"Visitando o local: {local.nome}")

        if local.nome == objetivo.nome: # se o nó é o objetivo, termina a busca
            print(f"Objetivo encontrado: {local.nome}")
            return

        # Adiciona os vizinhos do nó atual à pilha
        for vizinho in reversed(local.vizinhos): # inverte a ordem dos vizinhos para simular a pilha
            local_vizinho = vizinho['local']
            if local_vizinho not in visitados: # se o vizinho ainda não foi visitado
                pilha.append(local_vizinho)
                visitados.add(local_vizinho) # marca o vizinho como visitado

    print("Caminho não encontrado!")
    return None

# Criação do grafo
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
localArad.adicionarVizinho(localSibiu)
localArad.adicionarVizinho(localTimisoara)
localArad.adicionarVizinho(localZerind)

localZerind.adicionarVizinho(localArad)
localZerind.adicionarVizinho(localOradea)

localOradea.adicionarVizinho(localZerind)
localOradea.adicionarVizinho(localSibiu)

localSibiu.adicionarVizinho(localArad)
localSibiu.adicionarVizinho(localFagaras)
localSibiu.adicionarVizinho(localOradea)
localSibiu.adicionarVizinho(localRimnicuVilcea)

localTimisoara.adicionarVizinho(localArad)
localTimisoara.adicionarVizinho(localLugoj)

localLugoj.adicionarVizinho(localTimisoara)
localLugoj.adicionarVizinho(localMehadia)

localMehadia.adicionarVizinho(localLugoj)
localMehadia.adicionarVizinho(localDobreta)

localDobreta.adicionarVizinho(localMehadia)
localDobreta.adicionarVizinho(localCraiova)

localCraiova.adicionarVizinho(localDobreta)
localCraiova.adicionarVizinho(localPitesti)
localCraiova.adicionarVizinho(localRimnicuVilcea)

localRimnicuVilcea.adicionarVizinho(localSibiu)
localRimnicuVilcea.adicionarVizinho(localPitesti)
localRimnicuVilcea.adicionarVizinho(localCraiova)

localFagaras.adicionarVizinho(localSibiu)
localFagaras.adicionarVizinho(localBucharest)

localPitesti.adicionarVizinho(localRimnicuVilcea)
localPitesti.adicionarVizinho(localCraiova)
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

# Busca em profundidade
buscaEmProfundidade(localArad, localBucharest)
