#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from random import choice, randint




def gera_nome():
    nomes = [
    "Alice", "Miguel", "Sophia", "Arthur", "Helena", "Bernardo", "Valentina", "Heitor", "Laura", "Davi", "Isabella", "Lorenzo", "Manuela", "Théo", "Júlia", "Pedro", "Heloísa", "Gabriel", "Luiza", "Enzo", "Maria", "Matheus", "Lorena", "Lucas", "Lívia", "Benjamin", "Giovanna", "Nicolas", "Maria", "Guilherme", "Beatriz", "Rafael", "Maria", "Joaquim", "Cecília", "Samuel", "Eloá", "Enzo", "Lara", "João", "Maria", "Henrique", "Isadora", "Gustavo", "Mariana", "Murilo", "Emanuelly", "Pedro", "Ana", "Pietro", "Ana", "Lucca", "Ana", "Felipe", "Melissa", "João", "Yasmin", "Isaac", "Maria", "Benício", "Isabelly", "Daniel", "Lavínia", "Anthony", "Esther", "Leonardo", "Sarah", "Davi", "Elisa", "Bryan", "Antonella", "Eduardo", "Rafaela", "João", "Maria", "Victor", "Liz", "João", "Marina", "Cauã", "Nicole", "Antônio", "Maitê", "Vicente", "Isis", "Caleb", "Alícia", "Gael", "Luna", "Bento", "Rebeca", "Caio", "Agatha", "Emanuel", "Letícia", "Vinícius", "Maria", "João", "Gabriela", "Davi", "Ana", "Noah", "Catarina", "João", "Clara", "João", "Ana", "Luiz", "Vitória", "Francisco", "Olívia", "Kaique", "Maria", "Otávio", "Emilly", "Augusto", "Maria", "Levi", "Milena", "Yuri", "Maria", "Enrico", "Bianca", "Thiago", "Larissa", "Ian", "Mirella", "Victor", "Maria", "Thomas", "Allana", "Henry", "Ana", "Luiz", "Clarice", "Ryan", "Pietra", "Arthur", "Maria", "Davi", "Maya", "Nathan", "Laís", "Pedro", "Ayla", "Davi", "Ana", "Raul", "Eduarda", "Pedro", "Mariah", "Luiz", "Stella", "Luan", "Ana", "Erick", "Gabrielly", "Martin", "Sophie", "Bruno", "Carolina", "Rodrigo", "Maria", "Luiz", "Maria", "Arthur", "Maria", "Breno", "Fernanda", "Kauê", "Malu", "Enzo", "Analu", "Fernando", "Amanda", "Arthur", "Aurora", "Luiz", "Maria", "Carlos", "Louise", "Tomás", "Heloise", "Lucas", "Ana", "André", "Ana", "José", "Ana", "Yago", "Joana", "Danilo", "Luana", "Anthony", "Antônia", "Ruan", "Isabel", "Miguel", "Bruna", "Oliver"
    ]
    return choice(nomes)

def gera_data():
    ano = randint(1990, 2100)
    mes = randint(1, 12)
    if mes == 2:
        dia = randint(1, 29)
    elif (mes%2) == 2:
        dia = randint(1, 30)
    else:
        dia = randint(1, 31)

    data = f"{str(ano)}-{str(mes)}-{str(dia)}"
    return data

def gera_raca_caes():
    racas = [
        "Afegão Hound", "Affenpinscher", "Airedale Terrier", "Akita", "American Staffordshire Terrier", "Basenji", "Basset Hound", "Beagle", "Beagle Harrier", "Bearded Collie", "Bedlington Terrier", "Bichon Frisé", "Bloodhound", "Bobtail", "Boiadeiro Australiano", "Boiadeiro Bernês", "Border Collie", "Border Terrier", "Borzoi", "Boston Terrier", "Boxer", "Buldogue Francês", "Buldogue Inglês", "Bull Terrier", "Bulmastife", "Cairn Terrier", "Cane Corso", "Cão de Água", "Cão de Crista", "Cavalier King Charles", "Chesapeake Bay Retriever", "Chihuahua", "Chow Chow", "Cocker Spaniel Americano", "Cocker Spaniel Inglês", "Collie", "Coton de Tuléar", "Dachshund", "Dálmata", "Dandie Dinmont Terrier", "Doberman", "Dogo Argentino", "Dogue Alemão", "Fila Brasileiro", "Fox Terrier (Pelo", "Foxhound Inglês", "Galgo Escocês", "Galgo Irlandês", "Golden Retriever", "Grande Boiadeiro Suiço", "Greyhound", "Grifo da Bélgica", "Husky Siberiano", "Jack Russell Terrier", "King Charles", "Komondor", "Labradoodle", "Labrador Retriever", "Lakeland Terrier", "Leonberger", "Lhasa Apso", "Lulu da Pomerânia", "Malamute do Alasca", "Maltês", "Mastife", "Mastim Napolitano", "Mastim Tibetano", "Norfolk Terrier", "Norwich Terrier", "Papillon", "Pastor Alemão", "Pastor Australiano", "Pinscher Miniatura", "Poodle", "Pug", "Rottweiler", "Sem Raça Definida", "ShihTzu", "Silky Terrier", "Skye Terrier", "Staffordshire Bull Terrier", "Terra Nova", "Terrier Escocês", "Tosa", "Weimaraner", "Welsh Corgi (Cardigan", "Welsh Corgi (Pembroke", "West Highland White", "Whippet", "Xoloitzcuintli", "Yorkshire Terrier"
    ]
    return choice(racas)

def gera_especies_animais(id=0):
    if id == 0:
        especies= [
            "Felino",
            "Canino",
            "Roedor",
            "Réptil",
            "Passaro"
        ]
        return choice(especies)
    else:
        especies= [
            "Felino",
            "Canino",
            "Roedor",
            "Réptil",
            "Passaro"
        ]

        return especies[id]

def gera_telefone():
    parte0 = randint(1, 100)
    parte1 = randint(10000, 99999)
    parte2 = randint(1000, 9999)

    telefone = f"({str(parte0)}) {str(parte1)}-{str(parte2)}"

    return telefone

def gera_id_raca():
    racas = [
        "Afegão Hound", "Affenpinscher", "Airedale Terrier", "Akita", "American Staffordshire Terrier", "Basenji", "Basset Hound", "Beagle", "Beagle Harrier", "Bearded Collie", "Bedlington Terrier", "Bichon Frisé", "Bloodhound", "Bobtail", "Boiadeiro Australiano", "Boiadeiro Bernês", "Border Collie", "Border Terrier", "Borzoi", "Boston Terrier", "Boxer", "Buldogue Francês", "Buldogue Inglês", "Bull Terrier", "Bulmastife", "Cairn Terrier", "Cane Corso", "Cão de Água", "Cão de Crista", "Cavalier King Charles", "Chesapeake Bay Retriever", "Chihuahua", "Chow Chow", "Cocker Spaniel Americano", "Cocker Spaniel Inglês", "Collie", "Coton de Tuléar", "Dachshund", "Dálmata", "Dandie Dinmont Terrier", "Doberman", "Dogo Argentino", "Dogue Alemão", "Fila Brasileiro", "Fox Terrier (Pelo", "Foxhound Inglês", "Galgo Escocês", "Galgo Irlandês", "Golden Retriever", "Grande Boiadeiro Suiço", "Greyhound", "Grifo da Bélgica", "Husky Siberiano", "Jack Russell Terrier", "King Charles", "Komondor", "Labradoodle", "Labrador Retriever", "Lakeland Terrier", "Leonberger", "Lhasa Apso", "Lulu da Pomerânia", "Malamute do Alasca", "Maltês", "Mastife", "Mastim Napolitano", "Mastim Tibetano", "Norfolk Terrier", "Norwich Terrier", "Papillon", "Pastor Alemão", "Pastor Australiano", "Pinscher Miniatura", "Poodle", "Pug", "Rottweiler", "Sem Raça Definida", "ShihTzu", "Silky Terrier", "Skye Terrier", "Staffordshire Bull Terrier", "Terra Nova", "Terrier Escocês", "Tosa", "Weimaraner", "Welsh Corgi (Cardigan", "Welsh Corgi (Pembroke", "West Highland White", "Whippet", "Xoloitzcuintli", "Yorkshire Terrier"
    ]
    return randint(0, len(racas))

def gera_sql_raca(arquivo, id):
    arquivo.write(f"insert into racas(racas, idracas)"
          f"values('{gera_raca_caes()}', {id});\n")


def gera_sql_animal_caes(arquivo, id):
    arquivo.write(f"insert into animal(nome, datanascimento, dtulttrat, idracas, idespecie, idanimal)"
          f"values('{gera_nome()}', '{gera_data()}', null, {gera_id_raca()}, 2, {id});\n")

def gera_sql_especies(arquivo, id):
    arquivo.write(f"insert into especies(especie, idespecie)"
          f"values('{gera_especies_animais(id)}',  {id+1});\n")

def gera_sql_pessoas(arquivo, id):
    

arquivo = open("insere.sql", "w", encoding="utf8")

for i in range(5):
    gera_sql_especies(arquivo, i)

arquivo.write(f"/*{'#'*100}*/\n")

for i in range(15, 200):
    gera_sql_raca(arquivo, i)

arquivo.write(f"/*{'#'*100}*/\n")


for i in range(15, 200):
    gera_sql_animal_caes(arquivo, i)

arquivo.write(f"/*{'#'*100}*/\n")

for i in range(15, 200):
    gera_sql_pessoas(arquivo, i)

arquivo.write(f"/*{'#'*100}*/\n")


