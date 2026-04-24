with open("contatos.txt", "w") as contatos: #with chama o arquivo e fecha ele ao final do código.
    while True:
        nome = input("Nome: ")
        if not nome:
            break
        telefone = input("telefone: ")
        contatos.write(f"{nome}\t{telefone}\n")

with open("contatos.txt", "r") as contatos:
   for linha in contatos:
      nome, telefone = linha.strip("\n").split("\t")
      print(f"Nome: {nome}, telefone: {telefone}")
