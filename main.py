import openai
import time

with open('poemas_resultados.txt', 'w+') as poema_file:
    poema_file.write('')

openai.api_key = "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"

poemas = {}
prompts = [
    "Cuales elementos historicos se encuentran en este texto",
    "Cuales figuras literarias se encuentran en este texto",
    "Como se manifiestan los sentidos en este texto",
    "Cual es el papel de la naturaleza en este texto",
    "Como se manifiesta el tema de la raza en este texto",
    "Cuales valores y antivalores se mencionan en este texto",
    "Como relaciona el autor las personas y las cosas en este texto",
    "Importancia del genero epistolar en este texto"
    ]

cantidadPoemas = int(input("Cuantos poemas desea analizar: "))

for i in range(0, cantidadPoemas):
    poema_titulo = input("Ingrese el titulo del poema: ")
    poema = input("Ingrese el poema: ")
    poemas[i] = {
        "titulo": poema_titulo,
        "poema": poema
    }

print("Poemas:")
print(poemas)

timeBeforeCooldwn = 0

for i in range(0, len(poemas)):
    print(f'Index: {i}')
    with open('poemas_resultados.txt', "a", encoding="utf-8") as poema_resultados_file:
        poema_resultados_file.write(f'Poema: {poemas[i]["titulo"]}')
    
    for prompt in prompts:
        print(f'{prompt}: {poemas[i]["poema"]}')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f'{prompt}: {poemas[i]["poema"]}',
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
        )

        with open('poemas_resultados.txt', 'a', encoding="utf-8") as poema_resultados_file:
            poema_resultados_file.write(f'\n{prompt}\n {response.choices[0].text}\n')

        time.sleep(15)
