print("Seja Bem-Vindo ao MyDisney")
# ... (seu código de cadastro e login continua igual aqui) ...

# 1. Transformando o Catálogo em dicionários para aceitar contadores
Catálogo = [
    {"Titulo": "O Compasso do Vento", "curtidas": 0},
    {"Titulo": "Sob o Luar de Safira", "curtidas": 0},
    {"Titulo": "Ecos de um Amor Distante", "curtidas": 0},
    {"Titulo": "Código Infinito", "curtidas": 0},
    {"Titulo": "Crônicas de uma Terra Esquecida", "curtidas": 0},
    {"Titulo": "Cartas para um Destino Incerto", "curtidas": 0},
    {"Titulo": "Operação: Namorado de Mentirinha", "curtidas": 0},
    {"Titulo": "Adultos (Mais ou Menos)", "curtidas": 0},
    {"Titulo": "O Clube dos Desajustados", "curtidas": 0},
    {"Titulo": "A Garota no Lago", "curtidas": 0},
    {"Titulo": "A Sociedade Literária e a Torta de Casca de Batata", "curtidas": 0},
    {"Titulo": "O Paciente Silencioso", "curtidas": 0}
]

Busca = input("\nBusque aqui o título do filme: ").strip()

Encontrado = False

# 2. Percorrendo a lista para achar o filme pelo título
for filme in Catálogo:
    # Usamos .lower() para que a busca não diferencie maiúsculas de minúsculas
    if Busca.lower() == filme["Titulo"].lower():
        Encontrado = True
        print(f"\nFilme encontrado: {filme['Titulo']}")
        print(f"Curtidas atuais: {filme['curtidas']}")
        
        # 3. Sistema de Interação
        reacao = input("\nDigite 'L' para Curtir ou 'D' para Descurtir: ").upper()
        
        if reacao == 'L':
            filme["curtidas"] += 1
            print("✅ Você curtiu o filme!")
        elif reacao == 'D':
            # Diminui apenas se for maior que zero
            if filme["curtidas"] > 0:
                filme["curtidas"] -= 1
                print("⚠️ Você removeu a curtida.")
            else:
                print("ℹ️ O filme já tem 0 curtidas.")
        
        print(f"Novo total de curtidas: {filme['curtidas']}")
        break # Para o loop após encontrar o filme

if not Encontrado:
    print("Filme não encontrado!")