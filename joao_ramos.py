# a) O dicionário tem vai devolver 'X' --> absissa e 'Y' --> ordenada 

#Construtor
# vetor: real,real -> vetor

def cria_vetor(x,y):
    return {'x': x, 'y':y}

#seletores
#abissa: vetor ---> real
#ordenada: vetor ---> real
def seleciona_absissa(d):
    return d['x']

def seleciona_ordenada(d):
    return d['y']

#reconhecedores
#e_vetor : universal --> logico
#vetor_nulo : vetor --> logico

def e_vetor(d):
    return isinstance(d,dict) and isinstance(seleciona_absissa(d), float) and isinstance(seleciona_ordenada(d), float) and len(d) == 2 and'x' in d and 'y' in d

       
    
def vetor_nulo(d):
    return seleciona_absissa(d) == 0 and seleciona_ordenada(d) == 0
    

    
def produto(d1,d2):
    return seleciona_absissad(d1)*seleciona_absissa(d2)+seleciona_ordenada(d1)*seleciona_ordenada(d2)







    


