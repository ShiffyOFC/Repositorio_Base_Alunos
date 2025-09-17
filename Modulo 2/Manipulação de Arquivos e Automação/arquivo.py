# open() | Abrir arquivos que precisamos
#        com o nome da pasta e outros.

arquivo=open("Números_Legais.txt", "w")
for linha in range(1,26):
    arquivo.write("%d\n" % linha)
arquivo.close() #como está pasta não existe,
                # Será criada uma pasta 
                # Com as condições 
                # E mesmo nome.            