import cozmo 
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

import sqlite3 as sl
import random


import threading
import speech_recognition as sr

global reponseOral
reponseOral=''

global aRepondu
global cube

global con
con = sl.connect('../bdd/BDD.db')

###Biblioteque pour le vocal : pyaudio, SpeechRecognition(je crois que)
###pyaudio : https://pypi.org/project/PyAudio/
###Je suis sur windows, j'ai eu beaucoup de probleme pour installer cette biblioteque, la solution qui à marcher pour moi est : https://stackoverflow.com/a/57731053
###SpeechRecognition : https://pypi.org/project/SpeechRecognition/
###Pour que le vocal marche il faut la biblioteque python pyaudio, et (je ne suis pas sur que c'est la seul biblioteque neccessaire)
###Il faut aussi que l'ordinateur soit connecté à internet

###Remarque : Problème le vocal utilisé est celui de mon ordinateur, par celui du téléphone/tablette ce qui n'est pas exactement ce que l'on veut pour la suite

def cozmo_program(robot: cozmo.robot.Robot):

    #recuperer les ages disponnibles
    global con
    with con:
        data = con.execute("SELECT DISTINCT niveau FROM Questions ORDER BY niveau")

    parler(robot, "Donnez votre âge")
    print("Les ages disponible")
    
    ageDispo = []
    for row in data:
        ageDispo.append(str(row[0]))
        print(row[0])
    age = input('entrer l\'age de la question : ')
    #tant que l'age est pas dans la liste
    while age not in ageDispo :
        parler(robot, " Veuillez entrer un age dans la liste")
        age = input('entrer l\'age de la question : ')

    #recup une question
    #Pour avoir une question avec la réponse a l'oral, prendre la requete avec comme matiere math, et un age de 7 ans pour avoir plus de chance
    sql = "SELECT * FROM Questions WHERE niveau='" + age + "' and matiere='Mathématiques' ORDER BY RANDOM() LIMIT 1"
    #sql = "SELECT * FROM Questions WHERE niveau='" + age + "' ORDER BY RANDOM() LIMIT 1"

    with con:
        data = con.execute(sql)

    ligne = data.fetchone()

    parler(robot, "Thème de la question : " + ligne[1])
    #print("Theme de la question : " + ligne[1])
    parler(robot, "Question : " + ligne[2])
    #print(ligne[2])

    #recuperation des reponses, de la bonne reponse et de son numero apres le melange des réponses
    reponses =  ligne[3]
    reponses = reponses.split(';')

    nbReponse = len(reponses)
    if nbReponse==1:
        parler(robot, "Veuillez dire la réponse à l'oral")
        thread = threading.Thread(target=listen,args=[robot])
        thread.start()
        thread.join()
        print("apres fonction")
        global reponseOral
        print(reponseOral)
        aValide = 0
        while aValide==0:
            currentReponseOral = reponseOral
            parler(robot, "Avez vous bien dit : " + str(currentReponseOral) + ", oui, non, je vous ecoute")
            thread = threading.Thread(target=listen,args=[robot])
            thread.start()
            thread.join()
            print(reponseOral)
            if reponseOral=="oui":
                aValide = 1
                if str(currentReponseOral)==ligne[3]:
                    #print("bonne reponse !!!")
                    parler(robot, "bonne reponse !!!")
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()
                else:
                    parler(robot, "Faux, la bonne réponse étais : " + ligne[3])
                    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabLose).wait_for_completed()
            else:
                parler(robot, "Redonner votre réponse")
                thread = threading.Thread(target=listen,args=[robot])
                thread.start()
                thread.join()
                print(reponseOral)

    else:
        #initialisation des cubes
        cube1 = robot.world.get_light_cube(LightCube1Id)
        cube2 = robot.world.get_light_cube(LightCube2Id)
        cube3 = robot.world.get_light_cube(LightCube3Id)
        if cube1:
            cube1.set_lights(cozmo.lights.red_light)
        else:
            print('You might need a new cube battery https://www.kinvert.com/replace-cube-battery-cozmo-vector/')
        if cube2:
            cube2.set_lights(cozmo.lights.green_light)
        else:
            print('You might need a new cube battery https://www.kinvert.com/replace-cube-battery-cozmo-vector/')
        if cube3:
            cube3.set_lights(cozmo.lights.blue_light)
        else:
            print('You might need a new cube battery https://www.kinvert.com/replace-cube-battery-cozmo-vector/')

        bonneReponse = reponses[0]
        random.shuffle(reponses)
        #print(reponses)
        bonneReponseNumber = -1
        i = 0
        for reponse in reponses:
            i = i + 1
            if reponse==bonneReponse:
                bonneReponseNumber = i

        reponse1 = reponses[0]
        parler(robot, "réponse rouge : " + reponse1)
        #print("réponse 1 rouge : " + reponse1)
        reponse2 = reponses[1]
        #print("réponse 2 vert : " + reponse2)
        parler(robot, "réponse vert : " + reponse2)
        reponse3 = reponses[2]
        #print("réponse 3 bleu : " + reponse3)
        parler(robot, "réponse bleu : " + reponse3)


        handler = robot.add_event_handler(cozmo.objects.EvtObjectTapped, on_cube_tapped)

        global aRepondu
        aRepondu = 0
        while aRepondu==0:
            pass
        global cube
        print(str(cube))
        print(bonneReponseNumber)
        if cube==bonneReponseNumber:
            #print("bonne reponse !!!")
            parler(robot, "bonne reponse !!!")
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()
        else:
            parler(robot, "Faux, la bonne réponse étais : " + bonneReponse)
            robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabLose).wait_for_completed()

            #print("Faux, la bonne réponse étais : " + bonneReponse)



def on_cube_tapped( event, *, obj, tap_count, tap_duration, **kw):
    global cube
    cube = obj.cube_id

    global aRepondu
    aRepondu = 1

def parler(robot: cozmo.robot.Robot, p_text ):
	robot.say_text(p_text).wait_for_completed()

def listen(robot: cozmo.robot.Robot):
    recognizer = sr.Recognizer()

    '''SETUP MIC'''
    with sr.Microphone() as source:

        recognizer.pause_threshold = 0.8
        recognizer.dynamic_energy_threshold = False #was True
        recognizer.adjust_for_ambient_noise(source)
        recognized = None

        print("Ecoute pour 5 secondes")

        '''LISTENING'''
        try:
            audio = recognizer.listen(source, timeout = 5)
        except sr.WaitTimeoutError:
            print("Timeout...")
            return

        print("Done Listening: recognizing...")

        '''RECOGNIZING'''
        try:
            '''for testing purposes, we're just using the default API key
            to use another API key, change key=None to your API key'''
            recognized = recognizer.recognize_google(audio, key=None, language='fr').lower() #GOOGLE
            #recognized = recognizer.recognize_wit(audio, key=WIT_AI_KEY_EN) #WIT
            #recognized = recognizer.recognize_sphinx(audio, language=lang_ext).lower() #SPINX
            print("You said: " + recognized)
            global reponseOral
            reponseOral = recognized
            print("enregistrement dans variable")

            

        except sr.UnknownValueError or LookupError:
            print("Speech Recognition service could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service, check your web connection; {0}".format(e))
    print("Fin de la fonction")



cozmo.run_program(cozmo_program)
