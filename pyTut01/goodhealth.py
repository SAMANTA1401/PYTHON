# Healthy programmer
# 9am - 5pm
# water - water.mp3
# eyes - eyes.mp3
# physical acxtivty
# pygame
# rules

from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("Underwater-sound.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 20

    while True:
        if time()- init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('Underwater-sound.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at ")

        if time()- init_eyes > eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('Underwater-sound.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at ")

        if time()- init_exercise > exsecs:
            print("Physical activity time. Enter 'donephy' to stop the alarm.")
            musiconloop('Underwater-sound.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical activity done at ")
