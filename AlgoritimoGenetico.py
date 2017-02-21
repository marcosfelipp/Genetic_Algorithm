import random
import math

population_size = 100
numero_genes = 44
geracoes = 20
individuos = []


def melhor_na_populacao():
    maior = 0
    for i in range(0,population_size):
        if(individuos[i][1] > maior):
            maior = individuos[i][1]
    print(maior)

def mutacao(individuo):
    """
    Recebe um indivíduo como parâmetro e faz a mutação dele(troca de gene) de acordo com a taxa de mutação
    que no caso usaremos 5%. Em outras palavras, em 5% das vezes um indivpiduo vai sofrer mutação em algúm
    de seus genes.
    :param individuo:
    :return:
    """
    for gene in range(0,numero_genes):
        teste = random.randrange(0,100)
        if teste < 5 :
            #troca bit(gene)
            if individuos[individuo][0][gene] == 1:
                individuos[individuo][0][gene] = 0
            else :
                individuos[individuo][0][gene] ='1'

def f_seis(x,y):
    """
    O objetivo de todo o Algorítimo é encontrar o maior valor para essa função.
    :param x:
    :param y:
    :return:
    """
    resposta = 0.5 - (pow(math.sin(math.sqrt(pow(x, 2) + pow(y, 2))), 2)-0.5)/(pow((1+0.001 *((pow(x, 2) + pow(y, 2)))), 2))
    return resposta

def aptidao():
    """
    Função que mede a aptidão de cada indivíduo com base na função que queremos maximizar.
    Primeiro é feita uma parametrização ou seja, transformamos a string de 0's e 1's que representa um
    indivíduo em um inteiro (converte-se binário para a base 10).
    Nesse caso cada indivíduo representa dois números inteiros, x e y, que são os coeficientes da nossa
    função f6()
    :return:
    """
    for individuo in range(0, len(individuos)):
        x = 0
        y = 0
        #Converssão para base 10:
        for gene in range(((numero_genes // 2) - 1), 0, -1):
            if (individuos[individuo][0][gene]) == 1:
                x += 2 ** gene
            if (individuos[individuo][0][gene+(numero_genes//2)]) == 1:
                y += 2**gene
        #Parametrização:
        x = ((x * 200) / (pow(2, 22) - 1)) - 100
        y = ((y * 200) / (pow(2, 22) - 1)) - 100
        #Aplicar função no indivíduo para calculo da aptidão:
        individuos[individuo][1] = f_seis(x,y)
        #print(x, y,individuos[individuo][1])

def inicializaPopulacao():
    """
    Função que cria uma população inicial. Cada indivíduo é representado por uma string de 0's e 1's
    aleatórios.
    :return:
    """
    for individuo in range(0, population_size):
        stringIndividuo = []
        for gene in range(0, numero_genes):
            stringIndividuo.append(random.randrange(0, 2))
        listaIndividuo = [stringIndividuo, 0]
        individuos.append(listaIndividuo)

inicializaPopulacao()
for i in range(0, geracoes):
    aptidao()
    for individuo in range(0,population_size):
        mutacao(individuo)
    melhor_na_populacao()