import random
from gtts import gTTS
from time import sleep
import vlc
import keyboard as kb
import threading

paused = False
killed = False
record = 'Hello.mp3'
def play(text):
    word = gTTS(str(text), lang='en', slow=False)
    word.save(record)
    p = vlc.MediaPlayer(record)
    p.play()
try:
    play('Hello')
    speed = int(input('Pls enter the speed of narration in sec: '))
except:
    print('Type numbers, will you?')
    play('Type a number, dum-dum')
    sleep(2)
    exit()

lst = [0]
num = 0
while num in lst:
    num = random.randint(1, 90)
    if num not in lst:
        lst.append(num)
    if len(lst) == 91:
        break
lst = lst[1:]

def player():
    
    global killed
    global paused

    for a in lst:

        if paused:
            while True:
                
                if kb.is_pressed('z'):  
                    print('killing')
                    play('stopping')
                    paused = False
                    killed = True
                    break

                sleep(0.2)

                if kb.is_pressed('space') and paused:
                    sleep(0.1)
                    paused = False
                    print('UnPaused')
                    play('play')
                    break
        elif not killed:
            sleep(speed)
            if not paused and not killed:
                print(a)
                play(a)
            
        if killed:
            exit()
            break
        
def terminator():
    global killed
    global paused

    while True:
        sleep(0.1)
        if kb.is_pressed('z') and not killed and not paused:
            killed = True
            print('killing')
            word = gTTS('Stopping', lang='en', slow=False)
            word.save(record)
            p = vlc.MediaPlayer(record)
            p.play()
            break

        if not paused and kb.is_pressed('space') and not killed:
            print('paused')
            paused = True
            word = gTTS('paused', lang='en', slow=False)
            word.save(record)
            p = vlc.MediaPlayer(record)
            p.play()
            

t1 = threading.Thread(target=player)
t2 = threading.Thread(target=terminator)
t1.start()
t2.start()