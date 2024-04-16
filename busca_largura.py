from collections import deque

# Classe Local que representa um nó
class Local:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'local': vizinho})

# Função da busca em largura
def buscaEmLargura(inicio, objetivo):
    fila = deque()
    visitados = set()

    fila.append(inicio) # adiciona o nó inicial à fila
    visitados.add(inicio) # marca o nó inicial como visitado

    while fila:
        local = fila.popleft() # remove o primeiro nó da fila
        print(f"Visitando o local: {local.nome}")

        if local.nome == objetivo.nome: # se o nó é o objetivo, termina a busca
            print(f"Objetivo encontrado: {local.nome}")
            return

        # Adiciona os vizinhos do nó atual à fila na ordem em que foram adicionados ao nó
        for vizinho in local.vizinhos:
            local_vizinho = vizinho['local']
            if local_vizinho not in visitados: # se o vizinho ainda não foi visitado
                visitados.add(local_vizinho) # marca o vizinho como visitado
                fila.append(local_vizinho)

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

# Verificando se os locais foram criados corretamente
print("Locais criados:")
for local in [localArad, localZerind, localOradea, localSibiu, localTimisoara,
                localLugoj, localMehadia, localDobreta, localCraiova,
                localRimnicuVilcea, localFagaras, localPitesti, localBucharest,
                localGiurgiu, localUrziceni, localHirsova, localEforie,
                localVaslui, localIasi, localNeamt]:
    print(local.nome)

# Execução da busca em largura
print("\nBusca em largura:")
buscaEmLargura(localArad, localBucharest)
