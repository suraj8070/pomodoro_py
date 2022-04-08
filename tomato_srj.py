#_____________________________________________
# README.md
# This is an attempt to imitate tomato-timer
# created on 08 April 2022 by suraj8070 !!
#
# Type the below command in a terminal 
# to install package that provides beep sound
#
# sudo apt install sox
#
#References:
# for timer:-> https://stackoverflow.com/questions/18406165/creating-a-timer-in-python 
# for beep sound :-> https://askubuntu.com/questions/19906/beep-in-shell-script-not-working
#______________________________________________

#importing desired modules
import os
import time

#function to make beep
def beep_it():
    #loop the audio
    numb        = 3     # number of pulses in a beep.
    numbee      = 3     # number of beeps.
    duration    = 0.20  # seconds
    freq        = 3000  # Hz
    volume      = 0.15   # volume percentage.
    for j in range(numbee):
        for i in range(numb):
            os.system('play -nq -t alsa synth {} sine {} vol {}'.format(duration, freq, volume))
            #os.system('play -nq -t alsa synth {} sine {}' .format(duration, freq))
            time.sleep(0.5)
        time.sleep(1.5)
#function for timer
def tomato_timer(tlen):
    mins = 0
    # Loop until we reach 25 minutes running
    while mins != tlen:
        #print(">>>>>>>>>>>>>>>>>>>>> {} minute".format(mins))
        # Sleep for a minute
        time.sleep(60)
        # Increment the minute total
        mins += 1
        print(">>>>>>>>>>>>>>>>>>>>> {} minute".format(mins))
    beep_it()

# main code
inp = input("Type either start or break ?> ")
if inp == "start":
    tlen = 25   # in minutes
    print("Starting Tomato of {} minutes".format(tlen))
    tomato_timer(tlen)
elif inp == "break":
    tlen = 5    # in minutes
    print("Starting Break of {} minutes".format(tlen))
    tomato_timer(tlen)
else:
    quit()
os.system('clear')
quit()
