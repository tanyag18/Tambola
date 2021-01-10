import random
from gtts import gTTS
import vlc
from time import sleep
import keyboard as kb

def play(name, filename):
    word = gTTS(str(name), lang = 'en', slow = False)
    word.save(filename)
    p = vlc.MediaPlayer(filename)
    p.play()
    
a = random.randint(1, 90)
lst = []
speed = 2
for _ in range(90):
    n = 0
    while a in lst:
        a = random.randint(1,90)
    print(a)
    play(a, 'Hello.mp3')
    lst.append(a)
    while n <= speed:
        n += 0.01
        sleep(0.01)
        if kb.is_pressed('space'):
            print('paused')
            play('paused', 'Hello.mp3')
            temp = input('Enter a num to change speed or type exit to quit. ')
            if temp.strip() == 'exit':
                exit()
            elif len(temp.strip()) == 0:
                continue
            elif len(temp.strip()) != 0:
                try:
                    speed = int(temp)
                except ValueError:
                    print('Enter only a number, dum-dum')