print ("Seja Bem-Vindo ao MyDisney")
print ("Cadastre - se aqui: ")

Nome = input("Digite seu nome: ")
Email = input("Digite seu email: ")
Senha = input("Crie uma senha (De 5 a 8 caracteres): ")

Cadastro = []
Usuário = {
    Nome : "Nome", 
    Email : "Email",
    Senha : "Senha"  
}

Cadastro.append(Usuário)
print("O usuário foi Cadastrado!")

print ("Faça aqui seu login: ")

Login = input("Nome de usuário ou email: ")
Senha = input("Senha de sua escolha: ")

print (Login)
print (Senha)

print ("Estamos contentes de recebe-lo aqui! Desejamos que você tenha uma ótima experiência!")

print("Menu de buscas")
Busca = input("Busque aqui: ").strip()
print(Busca)

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

Encontrado = False

for filme in Catálogo:
    if Busca == filme["Titulo"].lower():
        Encontrado = True
        print(f"Aqui está: {filme["Titulo"]}")
        print(f"Avaliação atual: {filme["curtidas"]}")
        
        favoritos = input("Coloque '👍' para curtir e '👎' descurtir  ")
        
        if favoritos == "👍":
            filme ["curtidas"] += 1 
            print("Filme curtido com sucesso!")
        
        elif favoritos == "👎":
            if filme["curtidas"] > 0:
                filme ["curtidas"] -= 1 
                print("Esse filme foi removido da lista de curtidos!")

        print(f"Total de curtidas: {filme['curtidas']}")

if not Encontrado:
    print ("Filme não encontrado!")