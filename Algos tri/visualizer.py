import array
from tkinter import *
from webbrowser import get
import algorithms
import time
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pygame


dimensions = [1024, 512]
vitesse = 200
if vitesse==0:
    vitesses="Temps réel"
else:
 vitesses="Décalage de " + str(vitesse) + "ms"

algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort(), "InsertionSort": algorithms.InsertionSort(), "MergeSort": algorithms.MergeSort(), "QuickSort": algorithms.QuickSort()}

#liste les algorithmes disponibles
if len(sys.argv) > 1:
    if sys.argv[1] == "list":
        for key in algorithms.keys(): print(key, end=" ")
        print("")
        sys.exit(0)


pygame.init()


display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("#C4C5BF"))


#fermeture de la fenetre
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            pygame.quit();
            sys.exit;

            

#avancement visuel du tri

def update(algorithm, swap1, swap2, display=display):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Tri Graphique     Algorithme : {}     Temps: {:.3f}   Vitesse : {}   Statut: En cours de tri...".format(algorithm.name, time.time() - algorithm.start_time,vitesses))
    time.sleep(0.001*vitesse)
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        
        colour = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            colour = (0,255,0)
        elif swap2 == algorithm.array[i]:
            colour = (255,0,0)
        pygame.draw.rect(display, colour, (i*k,dimensions[1]-algorithm.array[i],k,algorithm.array[i]))
        
        
    check_events()
    pygame.display.update()

#garde la fenetre ouverte
def keep_open(algorithm, display, time):
    pygame.display.set_caption("Tri Graphique     Algorithme: {}     Temps: {:.3f}  Vitesse : {}    Statut: Tri complété ".format(algorithm.name, time,vitesses))
    
    while True:
        check_events()
        pygame.display.update()

def main(args):
    
        try:
           
            algorithm = algorithms[args[1]]

      
            try:

               
              
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                
            except:
                pass
        except:
            
            pass

main(sys.argv)