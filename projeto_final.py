# joao ramos 80915

from random import random
# os tupulos com os digitos iniciais do iin
AE = ('34','37');
DCI = ('309', '36', '38', '39');
DC = ('65',);
M = ('5018', '5020', '5038');
MC = ('50', '51', '52', '53', '54', '19');
VE = ('4026', '426', '4405', '4508');
V = ('4024', '4532', '4556');

def comeca_por(cad1,cad2):
    """Esta funcao recebe duas strings. Compara a cad1 com a cad1. Se elas forem iguais, devolve True"""
    if len(cad2) > len(cad1):  #transformo o numero numa string para conseguir comparar
        return False
    else:
        cad1 = cad1[0:len(cad2)] #edita a string de forma a que fique com o msm numero de caracteres q a outra string, mantendo a sua informacao
        if cad1 == cad2:
            return True
        else:
            return False
def comeca_por_um(cad,t_cads):
    """Esta funcao recebe uma string e um tupulo. Compara as iniciais de uma string com os numeros de um tupulo. Se forem iguais, devolve True """
    for i in range(len(t_cads)): #o indice percorre o cumprimento to tupulo
        if cad[0:len(t_cads[i])]==t_cads[i]:  #restrince cad ao tamanho de caracteres do indice no tupulo que esta a percorrer e compara cad com o numero no tupulo
            return True
    return False
        
def calc_soma(num):
    """Esta funcao recebe uma string e devolve um numero. Calcula o algoritmo de lunh todo. Trabalho com strings para que se o numero comecar por 0, o algoritmo nao o ignore. No final devolve a soma de todos os algarismos conforme o algoritmo"""
    num2 =''
    num3=0
    for i in range(len(str(num))-1,-1,-1): #este ciclo permite inverter o numero
        num2=num2+num[i]
    for i in range(len(num2)):
        if i%2==0: # verifica quais sao as posicoes impares
            if (eval(num2[i])*2)>9:
                num3=num3+(eval(num2[i])*2-9) #quando o numero multiplicado e maior que 9, subrai 9
            else:
                num3=num3+(eval(num2[i])*2)
        else:
            num3=num3+eval(num2[i])
    return num3       

def luhn_verifica(num):
    """Esta funcao recebe uma string e devolve True or False. Verifica se o numero realmente segue o algoritmo de luhn"""
    num=eval(num) #passo a string para numero para puder efetuar calculos
    x = num%10 
    num= num//10 
    num_temp =calc_soma(str(num)) + x #o numero temporario quarda o resultado da soma do algoritmo de luhnh com o digito menos significante guardado no inicio
    if num_temp%10 == 0: #se o resto da divisao por 10 for 0, entao o algoritmo de luhn esta correto
        return True
    else:
        return False

def valida_iin(num):
    """esta funcao recebe uma string e devolve outra string. Utilizo a funcao comeca_por_um para comparar o resultado entre a string dada e os iin dos varios tupulos. Se for verdade, devolve a rede emissora"""
    if comeca_por_um(num,AE) == True and len(num) == 15:
        return 'American Express'
    elif comeca_por_um(num,DCI) == True and len(num) == 14:
        return 'Diners Club International'
    elif comeca_por_um(num,DC) == True and len(num) == 16:
        return 'Discover Card'
    elif comeca_por_um(num,M) == True and (len(num) == 13 or len(num) == 19):
        return 'Maestro'
    elif comeca_por_um(num,MC) == True and len(num) == 16:
        return 'Master Card'
    elif comeca_por_um(num,VE) == True and len(num) == 16:
        return 'Visa Electron'
    elif comeca_por_um(num,V) == True and (len(num) == 13 or len(num) == 16):
        return 'Visa'
    else:
        return ''
        
def categoria(num):
    """Esta funcao recebe uma string, e conforme o primeiro numero da string, devolve a categoria em forma de string por exemplo: se o primeiro numero da string for 1, devolve companhias aereas. E assim sucessivamente"""
    a = num[0]
    if a == '1':
        return 'Companhias aereas'
    elif a == '2':
        return 'Companhias aereas e outras tarefas futuras da industria'
    elif a == '3':
        return 'Viagens e entretenimento e bancario / financeiro'
    elif a == '4' or a == '5':
        return 'Servicos bancarios e financeiros'
    elif a == '6':
        return 'Merchandising e bancario / financeiro'
    elif a == '7':
        return 'Petroleo e outras atribuicoes futuras da industria'
    elif a == '8':
        return 'Saude, telecomunicacoes e outras atribuicoes futuras da industria'
    elif a == '9':
        return 'Atribuicao nacional'
    else:
        return 'categoria incorreta'
        
def verifica_cc(num):
    """recebe um numero e se o cartao for valido devolve a categoria e a rede emissora. Caso contrario devolve: cartao invalido """
    if luhn_verifica(str(num)) and valida_iin(str(num)) != '':
        return (categoria(str(num)), valida_iin(str(num)))
    else:
        return 'cartao invalido'
    


def digito_verificacao(string):
    """A funcao calcula do ultimo digito. O digito que depois de calculada a soma na funcao calc_soma, nos devolve o numero necessario para que o resto da divisao por 10 seja igual a 0. """
    numero=int(calc_soma(string))    
    last=numero%10 #a variavel 'last' representa o ultimo algarismo da soma
    if last==0: #como a soma da 0, nao e preciso calcular o digiro de verificacao, logo apenas se acrescenta um 0 em forma de string
        return str(0)
    else:
        return str(10-last) # subtraindo o ultimo algarismo a 10, da o numero que temos que acrescentar para que a soma de o numero certo

def random_numero(t,num):
    """Introduz-se duas variaveis nesta funcao. O numero inial (escolhido aleatoriamente) e o numero de caracteres que o numero deve ter"""
    while len(str(num)) <= t:
        num = num*10 + round(random()*9) #os numeros sao escolhidos aleatoriamente e colucados na posicao correta
        
    return num*10 + eval(digito_verificacao(str(num))) #devolve um numero


def gera_num_cc(rd):
    """Nesta funcao introduz-se a abreviatura da rede emissora que queremos gerar um cartao. A funcao escolhe aleatoriamente um dos possiveis numeros iniciais. Essas informacoes estao armazenadas em tupulos. Para cada rede emissora existe um tamanho especifico de caracteres. Esta funcao devolve essa informacao a defenicao random_numero """
    if rd == 'AE':
        num = eval(AE[round(random())])
        return random_numero(13,num)  
    elif rd == 'DCI':
        num = eval(DCI[round(random()*3)])
        return random_numero(12,num)
    elif rd == 'DC':
        num = eval(DC[0])
        return random_numero(14,num)
    elif rd == 'MC':
        num = eval(MC[round(random()*2)])
        return random_numero(14,num)
    elif rd == 'VE':
            num = eval(VE[round(random()*3)])
            return random_numero(14,num)            
    elif rd == 'M': #esta rede emissora tem dois tamanhos diferentes para as cadeias de caracteres
            num = eval(M[round(random()*2)])
            a = round(random()) #eu escolho o numero de forma aleatoria, arredondando o resultado. Sendo apenas possivel 0 ou 1
            if a == 0:
                return random_numero(11,num)
            else:
                return random_numero(17,num)
    elif rd == 'V': #esta rede emissora tem dois tamanhos diferentes para as cadeias de caracteres
            num = eval(V[round(random()*2)])
            a = round(random()) #eu escolho o numero de forma aleatoria, arredondando o resultado. Sendo apenas possivel 0 ou 1
            if a == 0:
                return random_numero(11,num)
            else:
                return random_numero(14,num)