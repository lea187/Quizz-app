welcome = "Bienvenue sur mon Quiz! "
print(welcome)

playing = input ("Je te donne le nom d'un personnage et tu dois retrouver le nom de la série. Veux-tu y jouer ? ")
if playing.lower() != "oui" and playing.lower() != "ok" :
    quit()

print("Ok, c'est parti ! :)")

reponse = input("Owen Hunt : ")
if reponse.lower() == "grey's anatomy": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("rajesh Koothrapoli : ")
if reponse.lower() == "the big bang theory": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("samwell tarly : ")
if reponse.lower() == "game of thrones": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("Kady Kyle : ")
if reponse.lower() == "ma famille d'abord": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("eddie thomas : ")
if reponse.lower() == "phénomène raven": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("stevie : ")
if reponse.lower() == "malcolm": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("London Tipton : ")
if reponse.lower() == "la vie de palace de zack et cody": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("Eddie Britt : ")
if reponse.lower() == "desperate housewives": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("Peyton : ")
if reponse.lower() == "les frères scott": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

reponse = input("Lana Lang : ")
if reponse.lower() == "smallville": print("Bonne réponse !")
else: print("Mauvaise réponse ! ") 

