# def soma (a,b):
#     return a+b

def cadastrar_template():
    while True:
        nome = input("Digite o nome do template: ")
        cor = input("Digite a cor do template: ")
        tema = input("Digite o tema do template: ")

        print("\nTemplate cadastrado com sucesso!")
        print(nome, ",", cor, ",", tema)

        resposta = input("\nDeseja cadastrar outro template? (S/N): ")
        if resposta != "s":
            break


def adjust_letter_spacing(text, spacing):
    adjusted_text = " "
    for char in text:
        adjusted_text += char + " " * spacing
    return adjusted_text

# Exemplo de uso:
texto_original = "Bem vindo ao canva."
espacamento_desejado = 2
texto_ajustado = adjust_letter_spacing(texto_original, espacamento_desejado)

print("Texto original:")
print(texto_original)

print("\nTexto com espaçamento ajustado:")
print(texto_ajustado)

cadastrar_template()