   # (r leitura
   # w escrever
   # a escrever preservando o que já tinha
   # b binario para imagens e etc
   # + atualização de leitura e escrita)
"""arquivo=open("Números_Legais.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()""" #Exibe números
                # criados na pasta
                # anterior (arquivos.py)
ímpares=open("ímpares.txt", "w")
pares=open("pares.txt", "w")
for n in range (0,100):
    if n % 2==0:
        pares.write("%d\n" % n)
    else:
        ímpares.write("%d\n" % n)
ímpares.close()
pares.close()