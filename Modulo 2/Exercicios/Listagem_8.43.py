import types

diz_o_dicionario={"a":1,
                  "b":2,
                  "c":3}
diz_a_lista=[1+1,2,2+2,4,4+4,8,8+8,16]

programar_é_legal= True

def a():
    return

def diz_o_tipo(a):
    tipo=type(a)
    if tipo==str:
        return("String")
    elif tipo==list:
        return("Lista")
    elif tipo==dict:
        return("Dicionário")
    elif tipo==int:
        return("Número inteiro")
    elif tipo==float:
        return("Número decimal")
    elif tipo==types.FunctionType:
        return("Função")
    elif tipo==types.BuiltinFunctionType:
        return("Função interna")
    else:
        return(str(tipo))
    
print("É um/a: ", diz_o_tipo("Alo")) # 1 Exibe: String
print("É um/a: ", diz_o_tipo(print)) # 2 Exibe: Função interna
print("É um/a: ", diz_o_tipo(diz_o_dicionario)) # 3 Exibe: Dicionário
print("É um/a: ", diz_o_tipo(diz_a_lista)) # 4 Exibe: Lista  
print("É um/a: ", diz_o_tipo(diz_o_tipo)) # 5 Exibe: Função
print("É um/a: ", diz_o_tipo(605+4)) # 6 Exibe: Número inteiro
print("É um/a: ", diz_o_tipo(6.8+0.1)) # 7 Exibe: Número decimal
print("É um/a: ", diz_o_tipo(programar_é_legal)) # 8 Exibe: <class 'bool'>
print("É um/a: ", diz_o_tipo((13,44,13,3145,624))) # 9 Exibe: <class 'tuple'>
print("É um/a: ", diz_o_tipo(a())) # 10 Exibe: <class 'NoneType'>