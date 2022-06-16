from collections import Counter

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

"""
Text analyzér
-------------

Modul si vyžádá nejprve přihlašovací údaje. Pokud je uživatel uložený, 
může vybrat číslo textu (1-3) a modul mu zobrazí tyto informace:
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov pouze s malými písmeny,
- počet číslic,
- součet všech číselných hodnot,
- nejdelší slovo,
- nejčastější slovo,
- histogram.
"""

uzivatele = {"bob": "123",
             "ann": "pass123",
             "mike": "password123",
             "liz": "pass123"}

oddelovac = "-" * 35
mezera = " " * 6

username = input("Uživatelské jméno: ")
if username in uzivatele.keys():
    password = input("Heslo: ")
else:
    print("Neregistrovaný uživatel")
    quit()
print(oddelovac)

if uzivatele.get(username) == password:
    print(f"Vítej v aplikaci, {username}. K analýze máš na výber ze 3 textů.")
    Text_no = input("Zadej číslo mezi 1-3: ")
else:
    print("Heslo je špatné")
    quit()

print(oddelovac)

if Text_no.isnumeric():
    if 1 <= int(Text_no) <= 3:
        print(f"Statistiky")
    else:
        print("Zadané číslo není v rozmezí 1-3.")
        Text_no = input("Zadej číslo mezi 1-3: ")
else:
    print("Zadaná hodnota není číslo.")
    Text_no = input("Zadej číslo mezi 1-3: ")

Txt_index = (int(Text_no) - 1)

TEXTS[Txt_index] = TEXTS[Txt_index].replace(f"('.', ',', '-')", " ")


Pocet_slov = len(TEXTS[Txt_index].split())
print(f"Ve vybraném textu je {Pocet_slov} slov")
lowercase = len([slovo for slovo in TEXTS[Txt_index].split() if slovo.islower()])
# title = sum(map(str.istitle, TEXTS[Txt_index].split()))
title = len([slovo for slovo in TEXTS[Txt_index].split() if slovo.istitle()])
digit = [int(cislo) for cislo in TEXTS[Txt_index].split() if cislo.isnumeric()]
most_occur = Counter(TEXTS[Txt_index].split()).most_common(1)
max_word= max(TEXTS[Txt_index].split(), key= len)

uppercase = 0
uppercasehelp = False
format_string = "slovo zložené" if uppercase <2 else "slov zložených"
another_format= (f"jsou {title} slova") if 1< title <5 else (f"je {title} slov")

for words in TEXTS[Txt_index].split():
    if words.isupper():
        for character in words:
            if character.isdigit():
                uppercasehelp = False
                break
            else:
                uppercasehelp = True
        if uppercasehelp:
            uppercase += 1
            print(words)

suma = 0
for word in TEXTS[Txt_index].split():
    if word.isdigit():
        suma += int(word)

print(
    (f"Ve vybraném textu je {uppercase} {format_string}  pouze z velkých písmen."),
    (f"Ve vybraném textu jsou číslice: {digit}."),
    (f"Součet číslic je {suma}."),
    (f"Ve vybraném textu  {another_format} s počátečním velkým písmenem."),
    (f"Ve vybraném textu je {lowercase} slov složených pouze z malých písmen."),
    (f"Nejčastejší slovo {most_occur}."),
    (f"Nejdelší slovo: {max_word}"),
    (oddelovac),
    (f"Delka slova {mezera} frekvence slova"),
    (oddelovac),
    sep="\n"
)


words = TEXTS[Txt_index].split()

lengths = [len(word) for word in words]
max_length = max(lengths)
tallies = [0 for x in range(max_length + 1)]

for length in lengths:
    tallies[length] += 1

total_words = len(words)
for length in range(len(tallies)):
    if tallies[length] != 0:
        freq = tallies[length]
        values= "*" * freq
        print(f"{length:3} {values:17} {freq:10d}")
