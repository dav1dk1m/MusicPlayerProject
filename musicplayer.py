import pygame
import tkinter as tkr 

musicplayer = tkr.Tk()

musicplayer.title("Music Player")

musicplayer.geometry(450*350)

directory = askdirectory()

os.chdir(directory)

songlist = os.listdir()

playist = tkr.Listbox(musicplayer , font = "Cambria 14 bold", bg = "cyan2", selectmode = tkr.SINGLE)

for item in songlist:
    pos=0
    playist.insert(pos, item)
    pos= pos+1

    pygame.init()
    pygame.mixer.init()