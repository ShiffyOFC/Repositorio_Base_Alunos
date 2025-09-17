arquivo_escolhido=input("Nome do arquivo que deseja selecionar: ")

numbers=[0]

try:
    with open(arquivo_escolhido, 'r') as arquivo:
        for linha in arquivo:
            try:
                number=float(linha.strip())
                numbers.append(number)
            except ValueError:
                print(f"Na linha '{linha.strip()}' não é um número válido. Foi ignorado\n")
            soma=sum(numbers)
            dolar_real=soma*5.43
            print("Números lidos do arquivo", arquivo_escolhido, ":", numbers, "\n")
            print("Soma total do dinheiro(Em dolar):", soma, "\n")
            print("Soma total do dinheiro(Convertido em Reais):", dolar_real, "\n\n") # 11318,82
        else:
            print(f"Nenhum número válido encontrado.\n")
except FileNotFoundError:
    print(f"Erro:", arquivo_escolhido,"não existe, ou não foi encontrado.\n")
except Exception as e:
    print(f"Ocorreu um erro:", e, "\n") 