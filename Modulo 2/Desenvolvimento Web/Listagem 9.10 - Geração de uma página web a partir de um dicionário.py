filmes={
    "drama": ["Ainda Estou Aqui","O Poderoso Chefão", "Ela", "À Espera de um Milagre", "A Hora da Estrela"],
    "comédia": ["Tempos Modernos","American Pie","Dr. Dolittle", "Um espião e meio", "Está chovendo hamburguer"],
    "policial": ["O Exterminador do Futuro","O Procurado","Velozes e Furiosos", "Operações especiais", "Taxi"],
    "guerra": ["Rambo","1917","Até o Último Homem", "Coração de Ferro", "Platoon"],
    "anime": ["Demon Slayer:MugenTrain", "Naruto:The Last", "Jujutsu Kaisen 0", "Frieren", "One Punch Man"],
    "terror":["It, A coisa", "Anabelle", "Freira", "A Hora do Mal", "Casa Monstro"],
    "ação":["Jumanji", "Matrix", "Batman vs Superman", "Duro de Matar", "Hitman"],
    "super herói":["Titans", "Shazam", "Power Rangers", "The Batman", "Homem Aranha de volta ao lar"],
    "séries":["Flash", "Jovens Titãs em ação", "Round six", "Legends of Tomorrow"]
}
página=open("filmes.html","w", encoding="utf-8")
página.write("""
<!DOCTYPE html>
    <html lang="pt-BR">
        <head>
        <meta charset="utf-8">
        <title>Filmes</title>
            <style>
                
                body {
                    margin: 0;
                    padding: 0;
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background-color: #141414;
                    color: #fff;
                }

                h1 {
                    font-size: 24px;
                    margin: 40px 20px 10px;
                    color: #e50914;
                    border-bottom: 2px solid #e50914;
                    padding-bottom: 5px;
                    text-transform: uppercase;
                }

                .filme-grid {
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
                    gap: 15px;
                    padding: 0 20px 40px;
                }

                .filme-card {
                    background-color: #222;
                    padding: 10px;
                    border-radius: 8px;
                    transition: transform 0.3s ease;
                }

                .filme-card:hover {
                    transform: scale(1.05);
                    background-color: #333;
                }

                .filme-card h2 {
                    font-size: 16px;
                    margin: 0;
                    color: #fff;
                }

                @media (max-width: 600px) {
                    h1 {
                        font-size: 20px;
                    }

                .filme-card h2 {
                    font-size: 14px;
                }
            </style>
        </head>
        <body> 
""")
for c, v in filmes.items():
    página.write("<h1>%s</h1>" % c)
    for e in v:
        página.write("<h2>%s</h2>" % e)
página.write("""
</body>
</html>
""")
página.close()