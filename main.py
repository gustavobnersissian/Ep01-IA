import random
class quadrado():
    def __init__(self, pai=None, posicao=None):
        self.pai = pai
        self.posicao = posicao

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.posicao == other.posicao


def a_estrela(terreno, inicio, fim):

    # Cria o nó de início e de fim
    inicio_do_no = quadrado(None, inicio)
    inicio_do_no.g = inicio_do_no.h = inicio_do_no.f = 0
    fim_do_no = quadrado(None, fim)
    fim_do_no.g = fim_do_no.h = fim_do_no.f = 0

    # Inicializa a lista aberta e a lista fechada
    lista_aberta = []
    lista_fechada = []

    # Adiciona o nó inicial
    lista_aberta.append(inicio_do_no)

    # Entra em loop até encontrar o fim (terminar a lista aberta)
    while len(lista_aberta) > 0:

        # Pega o nó atual
        no_atual = lista_aberta[0]
        atual_index = 0
        for index, item in enumerate(lista_aberta):
            if item.f < no_atual.f:
                no_atual = item
                atual_index = index

        # Retira o nó atual da lista aberta e adiciona na lista fechada
        lista_aberta.pop(atual_index)
        lista_fechada.append(no_atual)

        # Encontra o objetivo
        if no_atual == fim_do_no:
            caminho = []
            atual = no_atual
            while atual is not None:
                caminho.append(atual.posicao)
                atual = atual.pai
            return caminho[::-1] # Return reversed caminho

        # Gera os filhos (children)
        children = []
        # Quadrados adjacentes (laterais e diagonais)
        for nova_posicao in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: 
            # Pega a posição dos nós
            posicao_do_no = (no_atual.posicao[0] + nova_posicao[0], no_atual.posicao[1] + nova_posicao[1])

            # Verifica se está no alcance do mapa
            if posicao_do_no[0] > (len(terreno) - 1) or posicao_do_no[0] < 0 or posicao_do_no[1] > (len(terreno[len(terreno)-1]) -1) or posicao_do_no[1] < 0:
                continue

            # Verifica se é possível percorrer o caminho
            if terreno[posicao_do_no[0]][posicao_do_no[1]] == 999:
                continue

            # Cria um novo nó
            novo_no = quadrado(no_atual, posicao_do_no)

            # Adiciona o novo nó
            children.append(novo_no)

        # Abre um looping percorrendo os filhos (children)
        for child in children:

            # Verifica se o filho está na lista fechada
            for closed_child in lista_fechada:
                if child == closed_child:
                    continue

            # Cria os valores de f, g e h 
            # G = distancia nó atual e nó inicial
            # H = distancia estimada do nó atual e nó final
            # F = custo total
            child.g = no_atual.g + mapa[no_atual.posicao[0]][no_atual.posicao[1]]
            child.h = ((fim_do_no.posicao[0] - child.posicao[0])) + ((fim_do_no.posicao[1] - child.posicao[1]))
            child.f = child.g + child.h
            
            # Verifica se o filho já está na lista aberta
            for no_aberto in lista_aberta:
                if child == no_aberto and child.g > no_aberto.g:
                    continue

            # Caso o filho não esteja na lista aberta, adiciona o filho à ela
            lista_aberta.append(child)


listaNum = [1,3,6,999] #terrenos do mapa

l = 5 #variavel da quantidade de linhas do mapa
c = 5 #variavel da quantidade de colunas do mapa

#criando a matriz do mapa
linha = [0] * (c+2)
mapa = [l] * (l+2)
for i in range(l+2):
    linha = []
    for j in range(c+2):
        linha.append(999)
    mapa[i] = linha

#preenchendo o mapa com os terrenos (aleatoriamente)
for i in range(1,l+1):
    for j in range(1,c+1):
        mapa[i][j] = random.choice(listaNum)

mapa[1][1] = 0 #definindo ponto inicial com valor 0
mapa[l][c] = 0 #definindo ponto final com valor 0

#funcao que mostra na tela o mapa
def mostraMapa():
    for i in range(0,l+2):
        for j in range(0,c+2):
            print(f'[{mapa[i][j]:^5}]', end='')
        print()
    print('\n')

def main():
    mostraMapa()
    inicio = (1, 1)
    fim = (l, c)

    caminho = a_estrela(mapa, inicio, fim)
    print(caminho)
    print()


if __name__ == '__main__':
    main()