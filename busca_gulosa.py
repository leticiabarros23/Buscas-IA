# Classe Local que representa um nó
class Local:
    def __init__(self, nome, distanciaObjetivo):
        self.nome = nome
        self.distanciaObjetivo = distanciaObjetivo
        self.vizinhos = []

    def adicionarVizinho(self, vizinho):
        self.vizinhos.append({'local': vizinho})

# Função de busca gulosa
def buscaGulosa(inicio, objetivo):
    atual = inicio
    caminho = [inicio.nome]  # Inicia o caminho com o local inicial

    while atual != objetivo:
        menorDistancia = float('inf')  # Inicializa com infinito para garantir que a primeira cidade visitada será a mais próxima do objetivo
        proximaCidade = None

        for vizinho in atual.vizinhos:  # Itera sobre os vizinhos do local atual
            if vizinho['local'].distanciaObjetivo < menorDistancia:
                menorDistancia = vizinho['local'].distanciaObjetivo
                proximaCidade = vizinho['local']

        if proximaCidade is None:
            return None

        atual = proximaCidade
        caminho.append(atual.nome)

    return caminho

# Criação do grafo
localArad = Local("Arad", 366)
localZerind = Local("Zerind", 374)
localOradea = Local("Oradea", 380)
localSibiu = Local("Sibiu", 253)
localTimisoara = Local("Timisoara", 329)
localLugoj = Local("Lugoj", 244)
localMehadia = Local("Mehadia", 241)
localDobreta = Local("Dobreta", 242)
localCraiova = Local("Craiova", 160)
localRimnicuVilcea = Local("Rimnicu Vilcea", 193)
localFagaras = Local("Fagaras", 178)
localPitesti = Local("Pitesti", 98)
localBucharest = Local("Bucharest", 0)
localGiurgiu = Local("Giurgiu", 77)
localUrziceni = Local("Urziceni", 80)
localHirsova = Local("Hirsova", 151)
localEforie = Local("Eforie", 161)
localVaslui = Local("Vaslui", 199)
localIasi = Local("Iasi", 226)
localNeamt = Local("Neamt", 234)

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

# Execução da busca gulosa
resultado = buscaGulosa(localArad, localBucharest)
if resultado is not None:
    print("Caminho encontrado:", ' -> '.join(resultado))
else:
    print("Caminho não encontrado!")
