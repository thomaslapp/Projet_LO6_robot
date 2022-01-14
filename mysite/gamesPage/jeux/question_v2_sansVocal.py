import cozmo 
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

import sqlite3 as sl
import random


global aRepondu
global cube

global con
con = sl.connect('./BDD.db')

def cozmo_program(robot: cozmo.robot.Robot):

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


    #recuperer les ages disponnibles
    global con
    with con:
        data = con.execute("SELECT DISTINCT niveau FROM Questions")

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
    sql = "SELECT * FROM Questions WHERE niveau='" + age + "' ORDER BY RANDOM() LIMIT 1"
    with con:
        data = con.execute(sql)

    ligne = data.fetchone()

    parler(robot, "Theme de la question : " + ligne[1])
    #print("Theme de la question : " + ligne[1])
    parler(robot, "Question : " + ligne[2])
    #print(ligne[2])

    #recuperation des reponses, de la bonne reponse et de son numero apres le melange des réponses
    reponses =  ligne[3]
    reponses = reponses.split(';')

    nbReponse = len(reponses)
    if nbReponse==1:
        parler(robot, "Veuillez dire la réponse à l'oral")
    else:
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
        parler(robot, "réponse 1 rouge : " + reponse1)
        #print("réponse 1 rouge : " + reponse1)
        reponse2 = reponses[1]
        #print("réponse 2 vert : " + reponse2)
        parler(robot, "réponse 2 vert : " + reponse2)
        reponse3 = reponses[2]
        #print("réponse 3 bleu : " + reponse3)
        parler(robot, "réponse 3 bleu : " + reponse3)


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


cozmo.run_program(cozmo_program)
