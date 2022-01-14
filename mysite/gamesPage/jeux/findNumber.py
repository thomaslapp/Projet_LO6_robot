import cozmo
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
import random
import time

global aTrouver
global min
global max
global currentNumber

def cozmo_program(robot: cozmo.robot.Robot):

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
    #print('Pense à un nombre entre 0 et 100')
    #print('Je vais essayer de le trouver')
    #print('Si je dit un nombre trop petit, appuis sur le cube rouge')
    #print('Si je dit un nombre trop grand, appuis sur le cube bleu')
    #print('Si je suis correct tape sur le vert !!!')

    parler(robot, 'Pense à un nombre entre 0 et 100, je vais essayer de le trouver')
    parler(robot, 'Tape sur le cube correspondant')
    parler(robot, 'Rouge trop petit')
    parler(robot, 'Vert correct')
    parler(robot, 'Bleu trop grand')

    global min
    min = 0
    global max
    max = 100
    global aTrouver
    aTrouver = 0
    global currentNumber
    currentNumber = random.randint(min, max + 1)
    handler = robot.add_event_handler(cozmo.objects.EvtObjectTapped, on_cube_tapped)
    global cube
    cube = -1
    parler(robot, str(currentNumber))
    while aTrouver==0:
        while cube==-1:
            pass
        if cube == 0:
            print('rouge')
            max = currentNumber - 1
            currentNumber = random.randint(min, max)
            print(currentNumber)
            parler(robot, str(currentNumber))
        if cube==1:
            print('vert')
            aTrouver = 1
        if cube==2:
            print('bleu')
            min = currentNumber + 1
            currentNumber = random.randint(min, max)
            print(currentNumber)
            parler(robot, str(currentNumber))

        cube = -1


    parler(robot, "J'ai trouvé")
    robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabHappy).wait_for_completed()

def on_cube_tapped( event, *, obj, tap_count, tap_duration, **kw):
    global cube
    cube = obj.cube_id - 1

def parler(robot: cozmo.robot.Robot, p_text ):
	robot.say_text(p_text).wait_for_completed()

cozmo.run_program(cozmo_program)

