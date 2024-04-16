import math

# Classe Local que representa um nó
class Local:
    def __init__(self, nome):
        self.nome = nome
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos.append({'local': vizinho, 'custo': distancia})

# Função de busca de custo uniforme
def busca_custo_uniforme(origem, objetivo):
    fronteira = [{'local': origem, 'caminho': [origem], 'custo': 0}]
    explorados = set()

    while fronteira:
        fronteira.sort(key=lambda x: x['custo']) # Ordena a fronteira com base no custo acumulado

        local_atual = fronteira.pop(0) # Escolhe o nó com menor custo e remove da fronteira
        local = local_atual['local']
        caminho = local_atual['caminho']
        custo = local_atual['custo']

        if local == objetivo:
            return {'caminho': caminho, 'custo': custo}

        explorados.add(local)

        for vizinho in local.vizinhos:
            local_vizinho = vizinho['local']
            custo_vizinho = vizinho['custo']
            if local_vizinho not in explorados:
                novo_caminho = caminho + [local_vizinho] # Caminho acumulado até o momento
                novo_custo = custo + custo_vizinho # Custo acumulado até o momento
                fronteira.append({'local': local_vizinho, 'caminho': novo_caminho, 'custo': novo_custo})

    return None

# Criação do grafo e adição dos vizinhos
local_arad = Local("Arad")
local_zerind = Local("Zerind")
local_oradea = Local("Oradea")
local_sibiu = Local("Sibiu")
local_timisoara = Local("Timisoara")
local_lugoj = Local("Lugoj")
local_mehadia = Local("Mehadia")
local_dobreta = Local("Dobreta")
local_craiova = Local("Craiova")
local_rimnicu_vilcea = Local("Rimnicu Vilcea")
local_fagaras = Local("Fagaras")
local_pitesti = Local("Pitesti")
local_bucharest = Local("Bucharest")
local_giurgiu = Local("Giurgiu")
local_urziceni = Local("Urziceni")
local_hirsova = Local("Hirsova")
local_eforie = Local("Eforie")
local_vaslui = Local("Vaslui")
local_iasi = Local("Iasi")
local_neamt = Local("Neamt")

# Adicionando os vizinhos
local_arad.adicionar_vizinho(local_sibiu, 140)
local_arad.adicionar_vizinho(local_timisoara, 118)
local_arad.adicionar_vizinho(local_zerind, 75)

local_zerind.adicionar_vizinho(local_arad, 75)
local_zerind.adicionar_vizinho(local_oradea, 71)

local_oradea.adicionar_vizinho(local_zerind, 71)
local_oradea.adicionar_vizinho(local_sibiu, 151)

local_sibiu.adicionar_vizinho(local_arad, 140)
local_sibiu.adicionar_vizinho(local_fagaras, 99)
local_sibiu.adicionar_vizinho(local_oradea, 151)
local_sibiu.adicionar_vizinho(local_rimnicu_vilcea, 80)

local_timisoara.adicionar_vizinho(local_arad, 118)
local_timisoara.adicionar_vizinho(local_lugoj, 111)

local_lugoj.adicionar_vizinho(local_timisoara, 111)
local_lugoj.adicionar_vizinho(local_mehadia, 70)

local_mehadia.adicionar_vizinho(local_lugoj, 70)
local_mehadia.adicionar_vizinho(local_dobreta, 75)

local_dobreta.adicionar_vizinho(local_mehadia, 75)
local_dobreta.adicionar_vizinho(local_craiova, 120)

local_craiova.adicionar_vizinho(local_dobreta, 120)
local_craiova.adicionar_vizinho(local_pitesti, 138)
local_craiova.adicionar_vizinho(local_rimnicu_vilcea, 146)

local_rimnicu_vilcea.adicionar_vizinho(local_sibiu, 80)
local_rimnicu_vilcea.adicionar_vizinho(local_pitesti, 97)
local_rimnicu_vilcea.adicionar_vizinho(local_craiova, 146)

local_fagaras.adicionar_vizinho(local_sibiu, 99)
local_fagaras.adicionar_vizinho(local_bucharest, 211)

local_pitesti.adicionar_vizinho(local_rimnicu_vilcea, 97)
local_pitesti.adicionar_vizinho(local_craiova, 138)
local_pitesti.adicionar_vizinho(local_bucharest, 101)

local_bucharest.adicionar_vizinho(local_fagaras, 211)
local_bucharest.adicionar_vizinho(local_pitesti, 101)
local_bucharest.adicionar_vizinho(local_giurgiu, 90)
local_bucharest.adicionar_vizinho(local_urziceni, 85)

local_giurgiu.adicionar_vizinho(local_bucharest, 90)

local_urziceni.adicionar_vizinho(local_bucharest, 85)
local_urziceni.adicionar_vizinho(local_hirsova, 98)
local_urziceni.adicionar_vizinho(local_vaslui, 142)

local_hirsova.adicionar_vizinho(local_urziceni, 98)
local_hirsova.adicionar_vizinho(local_eforie, 86)

local_eforie.adicionar_vizinho(local_hirsova, 86)

local_vaslui.adicionar_vizinho(local_urziceni, 142)
local_vaslui.adicionar_vizinho(local_iasi, 92)

local_iasi.adicionar_vizinho(local_vaslui, 92)
local_iasi.adicionar_vizinho(local_neamt, 87)

local_neamt.adicionar_vizinho(local_iasi, 87)

# Execução da busca de custo uniforme
resultado = busca_custo_uniforme(local_sibiu, local_bucharest)

if resultado is not None:
    caminho = [local.nome for local in resultado['caminho']]
    print("Menor caminho:", caminho)
    print("Custo total:", resultado['custo'])
else:
    print("Desculpe, mas não foi possível encontrar um caminho.")
