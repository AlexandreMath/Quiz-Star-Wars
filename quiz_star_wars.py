# -*- coding: latin-1 -*-
#importation des modules externe
import json

#une fonction qui affiche le message
def message(question, choix):
    return "{} La réponse est : {}".format(question, choix)	

#fonction qui affiche les resultats à la fin
def resultats(reussi, echec):
    return "Bonne réponse: {},  Mauvaise réponse: {}".format(reussi,echec)	
	
	
#fonction principal
def main_function():
    #Déclaration des variable global
    reussi = 0
    echec = 0
    quiz_value = 0
    questions = []
    choice = []
    responses = []
    
    #Recuperation des données du JSON
    with open("questions.json") as f:
        data = json.load(f)
        for entry in data:
           questions.append(entry["question"])
           choice.append(entry["choix"])
           responses.append(entry["reponse"])
        #Boucle - longeur de la liste data
        while quiz_value < len(data):
            #afiche le message
            print(message(questions[quiz_value],choice[quiz_value]))
            
            #demande à l'utilisateur d'entrer une réponse
            user_answer = input('Entrez le numéro de la réponse qui vous semble correct')
        
            #verification si cette reponse est bonne,
            if responses[quiz_value] == user_answer:
                reussi+=1
            else:
                echec+=1
            #misse à jour de la valeur
            quiz_value +=1
    return resultats(reussi, echec)
print(main_function())
