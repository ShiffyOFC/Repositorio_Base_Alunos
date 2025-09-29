from bs4 import BeautifulSoup
import requests
def raspagem_de_dados_2():
    url=input("Seu site: ")
    resposta= requests.get(url)
    conteudo_html=resposta.content
    soup= BeautifulSoup(conteudo_html,
                    'html.parser')
    links=soup.find_all('h1')
    links=soup.find_all('h2')
    for link in links:
        print("Texto: {%s}, URL: {%s}"
        % (link.text, link.get('href')))
raspagem_de_dados_2()