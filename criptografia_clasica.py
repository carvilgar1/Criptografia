from math import gcd


def y(a,b,x,n): return (a*x + b) % n
def x(a,b,y,n): 
    (mcd, u, v)= algoritmo_extendido_euclides(a,n)
    if mcd != 1:
        raise Exception('El valor {0} no tiene inverso en Z{1}'.format(a,n))
    return (y - b) * u % n

ABECEDARIO = [  ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'Ç', '0', '1', '2',
                '3', '4', '5', '6', '7', '8', '9', '@', '(', ')', '{', '}', '<', '>', '=', '+',
                '-', '*', '/', '%', '&', '$', '~', ',', ';', '.', ':', '¿', '?', '¡', '!', '’']

def euclides(a,b):
    while b != 0:
        a,b = b, a % b
    return a

def algoritmo_extendido_euclides(a,b):
    '''
    Devuelve una tupla donde:
    - tupla[0] = mcd(a,b).
    - tupla[1] = coeficiente de Bezout que multiplica a. Si mcd(a,b) = 1 entonces este valor es el inverso de a en Zb.
    - tupla[2] = coeficiente de Bezout que multiplica b.
    '''
    g0, g1, u0, u1, v0, v1 = b, a, 1, 0, 0, 1

    while g1 != 0:
        y = g0//g1
        g0, g1, u0, u1, v0, v1 = g1, g0%g1, u1, u0 - y*u1, v1, (v0 - y*v1)%b
    return g0,v0,u0

def cifrar_caracter(a,b,caracter,abecedario = ABECEDARIO):
    return abecedario[y(a,b,abecedario.index(caracter),len(abecedario))]

def descifrar_caracter(a,b,caracter,abecedario = ABECEDARIO):
    return abecedario[x(a,b,abecedario.index(caracter),len(abecedario))]

def cifrar_texto_criptosistema_afin(a,b,texto):
    return ''.join([cifrar_caracter(a,b,caracter) for caracter in texto])

def descifrar_texto_criptosistema_afin(a,b,texto):
    return ''.join([descifrar_caracter(a,b,caracter) for caracter in texto])

def cifrar_texto_criptosistema_desplazamiento(k,texto):
    return ''.join([cifrar_caracter(1,k,caracter) for caracter in texto])

def descifrar_texto_criptosistema_desplazamiento(k,texto):
    return ''.join([descifrar_caracter(1,k,caracter) for caracter in texto])