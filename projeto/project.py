print ("Seja Bem-Vindo ao MyDisney")

def inicio():
cadastros = []

try:
    with open("cadastro.txt") as cadastro:
        for linha in cadastro:
            cadastro.append()

Nome = input("Digite seu nome: ")
Email = input("Digite seu email: ")
Senha = input("Crie uma senha (De 5 a 8 caracteres): ")
cadastros.append(f"{Nome}\t{Email}\t{Senha}\n")
        
with open(cadastro.txt, "w") as cadastro:
        for usuario in cadastro:
            cadastro.write(usuario)
            print(f"Seja Bem Vindo {Nome}!") 

if usuario in cadastro:
    print("Você já está cadastrado! Faça seu Login.")      
        
    while True:
            Nome = input("Digite seu nome: ")
            if not nome:
             break
            Email = input("Digite seu email: ")
            Senha = input("Crie uma senha (De 5 a 8 caracteres): ")
            cadastro.write(f"{nome}\t{Email}\t{Senha}\n")

with open("contatos.txt", "r") as contatos:
   for linha in contatos:
      nome, telefone = linha.strip("\n").split("\t")
      print(f"Nome: {nome}, telefone: {telefone}")

print("Menu de buscas")
Busca = input("Busque aqui: ").strip()
print(Busca)

Catálogo = [ "A Cinco Passos de Você: Stella passa muito tempo no hospital devido a uma fibrose cística. Lá, ela conhece Will, que sofre da mesma doença. Eles são obrigados a manter distância, mas mesmo assim se apaixonam.",
"Hometown cha-cha-cha: Uma dentista da cidade grande abre um consultório em um vilarejo litorâneo e conhece um faz-tudo que é o extremo oposto dela.",
"Grey's Anatomy: A série médica de enorme sucesso foca em um grupo de jovens médicos do Hospital Grace Mercy West, de Seattle, que começaram a carreira na própria instituição como residentes. Um dos jovens médicos que dá nome ao show, Meredith Grey, é filha de um famoso cirurgião. Meredith luta para manter as relações com seus colegas, especialmente o chefe do centro cirúrgico, Richard Webber, devido ao relacionamento que já existia entre os dois: Webber teve um caso com a mãe de Meredith na época em que ela era jovem.",
"Código da Vinci: Um assassinato no museu do Louvre em Paris e pistas enigmáticas em alguns dos quadros mais famosos de Leonardo da Vinci levam à descoberta de um mistério religioso. Por mais de dois mil anos, uma sociedade secreta guarda informações que, se descobertas, poderiam comprometer o cristianismo. Robert Langdon, um professor especialista em simbologia e história, se envolve na investigação.", 
"Cinderela: Esta versão do clássico conto de fadas conta a história do sonho que se torna realidade por meio de inesquecíveis canções e personagens encantadores como ratinhos, a madrasta e a fada madrinha.",
"Meu Querido John: Um soldado em serviço e uma universitária se apaixonam, mas são forçados a viver separados por anos. Por meio de cartas, mantêm viva sua conexão à distância, enquanto enfrentam desafios que testam seu amor e transformam inesperadamente seu futuro.",
"Cartas para Julieta: Em visita à cidade italiana de Verona com seu noivo ocupado, uma jovem chamada Sophie visita um muro onde os desiludidos deixam cartas para a trágica heroína de Shakespeare, Julieta Capuleto. Ao encontrar uma dessas cartas, de 1957, a jovem decide escrever à autora, Claire. Inspirada pela atitude de Sophie, Claire decide procurar por seu antigo amor.",
"Gente Grande: A morte do treinador de basquete de infância de velhos amigos reúne a turma no mesmo lugar que celebraram um campeonato anos atrás. Os amigos, acompanhados de suas esposas e filhos, descobrem que idade não significa o mesmo que maturidade.",
"Te Peguei!: Desde a primeira série na escola, um grupo de cinco amigos tem um hábito curioso que realiza pelo menos uma vez ao ano: brincar enlouquecidamente de pega-pega, correndo em uma competição alucinante para ser o último homem de pé ao final da brincadeira, arriscando seus empregos e relacionamentos. Neste ano, que coincide com o casamento do jogador invicto da trupe, eles tentam de tudo para derrubá-lo nesse momento de vulnerabilidade.", 
"A Dama e o Vagabundo: Este clássico animado da Disney mostra uma cadela mimada chamada Lady e o término de sua vida confortável quando seus donos têm um bebê. Depois de algumas circunstâncias tensas, Lady encontra-se solta na rua, fazendo amizade. Ela torna-se protegida do vira-lata durão Tramp e um romance começa a florescer entre os dois cães.",
"Operação Big-Hero: O grande robô inflável está sempre a postos para cuidar de Hiro Hamada. Quando algo devastador assola a cidade, o menino prodígio, seus amigos e o robô formam um grupo de heróis para combater o mal.",
"A Bela e a Fera: Moradora de uma pequena aldeia francesa, Bela tem o pai capturado pela Fera e decide entregar sua vida ao estranho ser em troca da liberdade do progenitor. No castelo, ela conhece objetos mágicos e descobre que a Fera é na verdade um príncipe que precisa de amor para voltar à forma humana.", 
"Up - Altas aventuras: Carl Fredricksen é um vendedor de balões que, aos 78 anos, está prestes a perder a casa em que sempre viveu com sua esposa, a falecida Ellie. Após um incidente, Carl é considerado uma ameaça pública e forçado a ser internado. Para evitar que isto aconteça, ele põe balões em sua casa, fazendo com que ela levante voo. Carl quer viajar para uma floresta na América do Sul, onde ele e Ellie sempre desejaram morar, mas descobre que um problema embarcou junto: Russell, um menino de 8 anos.",
"Homem-Aranha 1: Ao ser picado por uma aranha geneticamente modificada em uma demonstração científica, o jovem nerd Peter Parker ganha superpoderes. Inicialmente, ele pretende usá-los para ganhar dinheiro, adotando o nome de Homem-Aranha e se apresentando em lutas de exibição. Porém, ao presenciar o assassinato de seu tio Ben e sentir-se culpado, Peter decide não mais usar seus poderes para proveito próprio e sim para enfrentar o mal, tendo como seu primeiro grande desafio o psicótico Duende Verde.",
"Venom: O jornalista investigativo Eddie Brock é possuído por uma forma alienígena simbionte, ganhando poderes-sobre humanos. Perverso, sombrio e alimentado pela raiva, Venom tenta controlar os novos e perigosos poderes inebriantes de Eddie.",
"A Nova Onda do Imperador: O jovem e arrogante Imperador Kuzco é transformado em uma lhama por sua poderosa mentora chamada Yzma. Perdido na floresta, a única chance de Kuzco recuperar seu trono é com a ajuda de Pacha, um humilde camponês. Juntos, eles precisam enfrentar a bruxa Yzma antes de concluir sua jornada."]

dicionario [
    {"Titulo": "A Cinco Passos de Você", "curtidas": 0},
    {"Titulo": "Hometown cha-cha-cha", "curtidas": 0},
    {"Titulo": "Grey's Anatomy", "curtidas": 0},
    {"Titulo": "Código Infinito", "curtidas": 0},
    {"Titulo": "Cinderela", "curtidas": 0},
    {"Titulo": "Meu Querido John", "curtidas": 0},
    {"Titulo": "Cartas para Julieta", "curtidas": 0},
    {"Titulo": "Gente Grande", "curtidas": 0},
    {"Titulo": "Te Peguei!", "curtidas": 0},
    {"Titulo": "A Dama e o Vagabundo", "curtidas": 0},
    {"Titulo": "Operação Big-Hero", "curtidas": 0},
    {"Titulo": "A Bela e a Fera", "curtidas": 0}
    {"Titulo": "Up - Altas aventuras", "curtidas": 0}
    {"Titulo": "Homem-Aranha", "curtidas": 0}
    {"Titulo": "Venom", "curtidas": 0}
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