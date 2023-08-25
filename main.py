import sqlite3
import random
import time

# connexion à la DB
conn = sqlite3.connect('quizz.db')
cursor = conn.cursor()

# demande difficulte
diff = 0
while str(diff) not in "123":
    diff = input("Choisissez une difficulté (1,2 ou 3)")

# récuperation de toute les question selon difficulté
cursor.execute(f"SELECT * FROM questions WHERE difficulte = {diff}")
liste_question = cursor.fetchall()

for i in range(10):
    # choisit une question au hasard et l'enlève de la liste
    random_question = liste_question[random.randint(1, len(liste_question)-1)]
    liste_question.remove(random_question)

    # récuperation des 4 réponses qui vont avec question
    cursor.execute(f"SELECT * FROM reponses WHERE question_id = {random_question[0]}")
    liste_reponses = cursor.fetchall()
    bonne_reponse = 0

    # affichage question+réponses
    print(random_question[1])
    for j in range(4):
        print(f"{j+1}: {liste_reponses[j][1]}")
        if liste_reponses[j][2] == 1:
            bonne_reponse = j

    # input user
    user_reponse = input("Votre réponse: ")
    if user_reponse.lower() == 'quit':
        break

    # vérification bonne ou mauvaise réponse et affichage
    if int(user_reponse) == bonne_reponse+1:
        print("Bonne réponse !")
    else:
        print(f"Faux! La bonne réponse est la N°{bonne_reponse+1} : ", end="")
        print(f"'{liste_reponses[bonne_reponse][1]}'", end="\n")


    # timer de 2s avant la prochaine question
    time.sleep(2)
