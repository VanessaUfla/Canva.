
import canva

while True:
    nome = input("Digite o nome do template: ")
    cor = input("Digite a cor do template: ")
    tema = input("Digite o tema do template: ")

    print("\nTemplate cadastrado com sucesso!")
    print(nome, ",", cor, ",", tema)

    canva.cadastrar_template(nome, cor, tema)

    resposta = input("\nDeseja cadastrar outro template? (S/N): ")
    if resposta == "N":
            break

    print(canva.templates)
