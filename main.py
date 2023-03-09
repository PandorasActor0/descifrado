import pandas as pd
path_file = 'LetterFrequency.xlsx'
col_types = {"Letter": str, "Count": int}
hoja = "Hoja1"
df = pd.read_excel(path_file, sheet_name=hoja, dtype=col_types)
Letteringles = list(df['Letter'])
print(Letteringles)
with open('mensaje.txt') as archivo:
    mensaje = archivo.read()
    print(" mensaje cifrado: " + mensaje)

letras_dic = {}  # Guarda repetición de letras

for letra in mensaje:  # Por cada letra
    if letra in letras_dic:  # Si ya estaba en el dic() significa que se repite
        letras_dic[letra] += 1  # Continua el conteo
    else:
        letras_dic[letra] = 1  # Si la letra no esta en el diccionario, la agrega

letras_dic.pop(" ")
mensaje2 = mensaje

dicc = {}
for g in range(22):
    a = max(letras_dic.values())
    b = list(letras_dic.values())
    c = list(letras_dic.keys())
    for x in range(len(b)):
        if b[x] == a:
            d = c[x]

    mensaje2 = mensaje2.replace(d, Letteringles[g])

    letras_dic.pop(d)
    dicc[d] = Letteringles[g]
    print(dicc)
print(mensaje)
dicc[' '] = ' '
salida = ""
for l in mensaje:
    salida += dicc[l]

print(salida)









