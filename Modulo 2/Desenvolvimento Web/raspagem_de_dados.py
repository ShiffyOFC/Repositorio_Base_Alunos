from bs4 import BeautifulSoup
import requests

url = 'https://www.youtube.com'
resposta= requests.get(url)
conteudo_html=resposta.content

soup= BeautifulSoup(conteudo_html,
                    'html.parser')

links=soup.find_all('a')

for link in links:
    print("Texto: {%s}, URL: {%s}"
    % (link.text, link.get('href')))

"""Texto: {}, URL: {/}
Texto: {}, URL: {/}
Texto: {Sobre}, URL: {https://www.youtube.com/about/}     
Texto: {Imprensa}, URL: {https://www.youtube.com/about/press/}
Texto: {Direitos autorais}, URL: {https://www.youtube.com/about/copyright/}
Texto: {Entre em contato}, URL: {/t/contact_us/}
Texto: {Criadores de conteúdo}, URL: {https://www.youtube.com/creators/}
Texto: {Publicidade}, URL: {https://www.youtube.com/ads/} 
Texto: {Desenvolvedores}, URL: {https://developers.google.com/youtube}
Texto: {Termos}, URL: {/t/terms}
Texto: {Privacidade}, URL: {/t/privacy}
Texto: {Política e segurança}, URL: {https://www.youtube.com/about/policies/}
Texto: {Como funciona o YouTube}, URL: {https://www.youtube.com/howyoutubeworks?utm_campaign=ytgen&utm_source=ythp&utm_medium=LeftNav&utm_content=txt&u=https%3A%2F%2Fwww.youtube.com%2Fhowyoutubeworks%3Futm_source%3Dythp%26utm_medium%3DLeftNav%26utm_campaign%3Dytgen}
Texto: {Testar os novos recursos}, URL: {/new}"""