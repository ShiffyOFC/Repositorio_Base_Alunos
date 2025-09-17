def lê_texto():
    try:
        with open(input("nome do arquivo: ") ,"r") as fs1:
            dados=fs1.read()
            print(type(dados))
        with open("cópia_0.txt" ,"w") as fs2:
            fs2.write(dados)
        with open("cópia_1.txt" ,"w") as fs2:
            fs2.write(dados)
        with open("cópia_2.txt" ,"w") as fs2:
            fs2.write(dados)            
    except FileNotFoundError as e:
        print('Arquivo não existe! -_-|||', e)
    except IOError as e:
        print('Deu algo errado @_@') 
    print("OK! ~_~")
lê_texto()