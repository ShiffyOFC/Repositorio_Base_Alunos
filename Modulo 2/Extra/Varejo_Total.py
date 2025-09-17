arquivo_escolhido=input("Nome do arquivo que deseja selecionar: ")

numbers=[]

try:
    with open(arquivo_escolhido, 'r') as arquivo:
        for linha in arquivo:
            try:
                number=float(linha.strip())
                numbers.append(number)
            except ValueError:
                print(f"Na linha '{linha.strip()}' não é um número válido. Foi ignorado")
            soma=sum(numbers)
            print("Números lidos do arquivo", arquivo_escolhido, ":", numbers)
            print("Soma total dos números:", soma)
        else:
            print(f"Nenhum número válido encontrado.")
except FileNotFoundError:
    print(f"Erro:", arquivo_escolhido,"não existe, ou não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro:", e)