# def soma (a,b):
#     return a+b

templates = []

def cadastrar_template(n, c, t):
    template ={}
    if not n:
         return False
    template["nome"] = n
    template["cor"] = c
    template["tema"] = t
    templates.append(template)
    return True

def adjust_letter_spacing(text, spacing):
    adjusted_text = " "
    for char in text:
        adjusted_text += char + " " * spacing
    return adjusted_text

# Exemplo de uso:
texto_original = "Bem vindo ao canva."
espacamento_desejado = 2
texto_ajustado = adjust_letter_spacing(texto_original, espacamento_desejado)

# print("Texto original:")
# print(texto_original)

# print("\nTexto com espaçamento ajustado:")
# print(texto_ajustado)



