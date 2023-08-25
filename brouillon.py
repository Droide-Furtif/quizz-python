import random
import sqlite3

'''
sql = "SELECT * FROM questions WHERE difficulte = 3"
cursor.execute(sql)
q_list = cursor.fetchall()



conn = sqlite3.connect("quizz.db")
cursor = conn.cursor()

file = "C:/Users/Mathis/Desktop/questions.txt"
with open(file, 'r', encoding='utf-8') as f:
    id = 1
    i = 0
    for line in f:
        if line[0] in "abcd":
            cursor.execute(f"INSERT INTO reponses (intitule_rep, question_id, juste)"
                           f" VALUES (?, ?, ?)", (line[3:-1:], id, 0))
            print(line[3:-1])
            i += 1
            if i == 4:
                i = 0
                id += 1

conn.commit()
'''
# create a table
'''
cursor.execute("""CREATE TABLE Questions
                  (intitule TEXT, niveau INTEGER,
                   points INTEGER, temps INTEGER)
               """)

# insert a record into the books table in the library database
cursor.execute("""INSERT INTO books
                  VALUES ('Python 101', 'Mike Driscoll', '9/01/2020',
                          'Mouse Vs Python', 'epub')"""
               )
# save data
conn.commit()

# delete ROW 
DELETE FROM Questions WHERE rowid=3
# delete table
DROP TABLE nom

# select 
command = "SELECT * FROM Questions WHERE niveau=3"
'''
'''
cursor.execute("SELECT * FROM Questions")
questions_list = cursor.fetchall()
random_question = questions_list[random.randint(0,2)]

cursor.execute(f"SELECT * FROM Reponses WHERE question_id = {random_question[0]}")
reponses_liste = cursor.fetchall()

diff = 0
if random_question[2] == 1:
    diff = "Noob"
elif random_question[2] == 2:
    diff = "Gamer"
else:
    diff = "Hardcore"

print(f"{diff}: {random_question[1]}")
for i in range(4):
    print(f"Réponse {i+1}: {reponses_liste[i][1]}")

#sql = "INSERT INTO Reponses (texte, question_id) VALUES ("
#values = f"'réponse {r}.{j}', {r})"

#cursor.execute(sql+values)
#conn.commit()
'''

'''
for row in cursor.execute("SELECT question_id, * FROM Questions ORDER BY question_id"):
    print(row)

print("\n\nRéponses: \n")
for row in cursor.execute("SELECT reponse_id, * FROM Reponses ORDER BY reponse_id"):
    print(row)



'''