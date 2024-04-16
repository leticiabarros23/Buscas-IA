import math

# Classe Local que representa um nó
class Local:
    def __init__(self, nome, distancia_objetivo):
        self.nome = nome
        self.distancia_objetivo = distancia_objetivo
        self.vizinhos = []

    def adicionar_vizinho(self, vizinho, distancia):
        self.vizinhos.append({'local': vizinho, 'custo': distancia})

# Função de busca A*
def busca_a_estrela(inicio, objetivo):
    abertos = [inicio] # Nós ainda não avaliados
    fechados = [] # Nós já avaliados
    caminho = {inicio.nome: {'custo': 0, 'pai': None}} # O custo para chegar ao local inicial é 0 e não tem pai

    # Função de custo total estimado
    def custo_total_estimado(local):
        return local.distancia_objetivo + caminho[local.nome]['custo']

    while abertos:
        # Encontrando o local com o menor custo total estimado
        local_atual = min(abertos, key=lambda local: custo_total_estimado(local))

        if local_atual == objetivo:
            caminho_final = []
            while local_atual:
                caminho_final.insert(0, local_atual.nome)
                local_atual = caminho[local_atual.nome]['pai']
            return caminho_final

        # Removendo o local atual da lista de nós abertos
        abertos.remove(local_atual)
        fechados.append(local_atual)

        for vizinho in local_atual.vizinhos:
            if vizinho['local'] not in fechados: # Se o vizinho ainda não foi avaliado
                custo_atualizado = caminho[local_atual.nome]['custo'] + vizinho['custo']

                # Se o vizinho ainda não está na lista de nós abertos, ou se o novo custo é menor
                if vizinho['local'] not in abertos or custo_atualizado < caminho[vizinho['local'].nome]['custo']:
                    caminho[vizinho['local'].nome] = {'custo': custo_atualizado, 'pai': local_atual} # Atualiza o custo e o pai do vizinho
                    if vizinho['local'] not in abertos:
                        abertos.append(vizinho['local']) # Adiciona o vizinho à lista de nós abertos
    return None



# Criação do grafo
local_arad = Local("Arad", 366)
local_zerind = Local("Zerind", 374)
local_oradea = Local("Oradea", 380)
local_sibiu = Local("Sibiu", 253)
local_timisoara = Local("Timisoara", 329)
local_lugoj = Local("Lugoj", 244)
local_mehadia = Local("Mehadia", 241)
local_dobreta = Local("Dobreta", 242)
local_craiova = Local("Craiova", 160)
local_rimnicu_vilcea = Local("Rimnicu Vilcea", 193)
local_fagaras = Local("Fagaras", 178)
local_pitesti = Local("Pitesti", 98)
local_bucharest = Local("Bucharest", 0)
local_giurgiu = Local("Giurgiu", 77)
local_urziceni = Local("Urziceni", 80)
local_hirsova = Local("Hirsova", 151)
local_eforie = Local("Eforie", 161)
local_vaslui = Local("Vaslui", 199)
local_iasi = Local("Iasi", 226)
local_neamt = Local("Neamt", 234)



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

# Execução da busca A*
resultado = busca_a_estrela(local_arad, local_bucharest)

if resultado is not None:
    print("Caminho encontrado:")
    print(resultado)
else:
    print("Caminho não encontrado.")
