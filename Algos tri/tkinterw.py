from tkinter import * 
import visualizer  
import sys

def create():
    root.destroy()
    sys.argv.append("SelectionSort")
    visualizer.main(sys.argv)

def create1():
    root.destroy()
    sys.argv.append("BubbleSort")
    visualizer.main(sys.argv)

def create2():
    root.destroy()
    sys.argv.append("InsertionSort")
    visualizer.main(sys.argv)

def create3():
    root.destroy()
    sys.argv.append("MergeSort")
    visualizer.main(sys.argv)

def create4():
    root.destroy()
    sys.argv.append("QuickSort")
    visualizer.main(sys.argv)

root = Tk()
root.geometry('200x200')  

btn = Button(root, text="Tri par selection", command = create)
btn1 = Button(root, text="Tri par bulle", command = create1)
btn2 = Button(root, text="Tri par insertion", command = create2)
btn3 = Button(root, text="Tri par merge", command = create3)
btn4 = Button(root, text="Quick", command = create4)

btn.pack(pady = 5) 
btn1.pack(pady = 5) 
btn2.pack(pady = 5) 
btn3.pack(pady = 5) 
btn4.pack(pady = 5) 
root.mainloop()