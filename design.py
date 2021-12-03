from tkinter import * 
from random import* 
myWindow = Tk()
screen = Canvas(myWindow, width=800, height=600, background="sky blue" )  #Or any other colour
screen.pack()

#GRASS
grass = 400
screen.create_rectangle (0, grass, 800, 600, fill = "dark goldenrod")
grasscolours = ("green4", "DarkOliveGreen1", "lawngreen", "green3", )
for n in range (10000):
  d = randint(0,800)
  t = randint(grass-5 ,600)
  dlean = randint(-5,15)
  tlean = randint(5,20)
  colour = choice(grasscolours)
  screen.create_line(d, t, d+dlean, t+tlean, fill = colour)

#BUILDING
screen.create_rectangle (100,225,700, 450, outline="black", width = 3,fill="lavender")

#WINDOWS
screen.create_rectangle (150, 260, 200, 330, outline ="black" , width = 2.5,  fill = "white")
screen.create_line(175, 260, 175, 330, fill = "black", width = 2)
screen.create_line (150, 295, 200,295 , fill = "black", width = 2)
screen.create_rectangle (225, 260, 275, 330, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line(250, 260, 250, 330, fill = "black", width = 2)
screen.create_line (225, 295, 275,295 , fill = "black", width = 2)
screen.create_rectangle (225, 375, 275, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (250, 375, 250, 440, fill = "black", width = 2)
screen.create_line (225, 410, 275, 410, fill = "black", width = 2)
screen.create_rectangle (150, 375, 200, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (175, 375, 175, 440, fill = "black", width = 2)
screen.create_line (150, 410, 200, 410, fill = "black", width = 2)
screen.create_rectangle (315, 260, 360, 330, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (337, 260, 337, 330, fill = "black", width = 2)
screen.create_line (315, 295, 360, 295, fill = "black", width = 2)
screen.create_rectangle (315, 375, 360, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (337, 375, 337, 440, fill = "black", width = 2)
screen.create_line (315, 410, 360, 410, fill = "black", width = 2)
screen.create_rectangle (380, 260, 425, 330, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (402, 260, 402, 330, fill = "black", width = 2)
screen.create_line (380, 295, 425, 295, fill = "black", width = 2)
screen.create_rectangle (380, 375, 425, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (337, 375, 337, 440, fill = "black", width = 2)
screen.create_line (380, 410, 425, 410, fill = "black", width = 2)
screen.create_rectangle (450, 260, 490, 330, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (470, 260, 470, 330, fill = "black", width = 2)
screen.create_line (450, 295, 490, 295, fill = "black", width = 2)
screen.create_rectangle (450, 375, 490, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (470, 375, 470, 440, fill = "black", width = 2)
screen.create_line (450, 410, 490, 410, fill = "black", width = 2)
screen.create_rectangle (535, 260, 585, 330, outline ="black" , width = 2.5,  fill = "white")
screen.create_line(560, 260, 560, 330, fill = "black", width = 2)
screen.create_line (535, 295, 585,295 , fill = "black", width = 2)
screen.create_rectangle (610, 260, 660, 330, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line(635, 260, 635, 330, fill = "black", width = 2)
screen.create_line (610, 295, 660,295 , fill = "black", width = 2)
screen.create_rectangle (535, 375, 585, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (560, 375, 560, 440, fill = "black", width = 2)
screen.create_line (535, 410, 585, 410, fill = "black", width = 2)
screen.create_rectangle (610, 375, 660, 440, outline ="black"  , width = 2.5,  fill = "white")
screen.create_line (635, 375, 635, 440, fill = "black", width = 2)
screen.create_line (610, 410, 660, 410, fill = "black", width = 2)



#ARCS AND TRIANGLES BETWEEN WINDOWS
screen.create_arc( 150, 340, 200, 375, start=0, extent=180, outline = "black", width = 3, fill="white")
screen.create_polygon(225, 358, 275, 358, 250, 340, fill ="white", outline = "black", width = 2.5)
screen.create_arc( 315, 341, 360, 381, start=0, extent=180, outline = "black", width = 3, fill="white")
screen.create_arc( 450, 342, 490, 382, start=0, extent=180, outline = "black", width = 3, fill="white")
screen.create_polygon(380, 358, 425, 358, 402, 340, fill ="white", outline = "black", width = 2.5)
screen.create_arc( 610,340, 660, 385, start=0, extent=180, outline = "black", width = 3, fill="white")
screen.create_polygon(535, 358, 585, 358, 560, 340, fill ="white", outline = "black", width = 2.5)

#ROOF
screen.create_polygon(100, 225, 200, 75, 600,75, 700, 225, fill = "lavender", outline = "black", width =2.5)
screen.create_polygon (175, 120, 260, 175, 320, 120, 407, 175, 475, 120, 570, 175, 635, 120, 640,127, 570, 182, 475, 127, 400, 182, 320, 127, 260, 182, 165, 127,smooth = "true", fill = "red")
screen.create_polygon (190, 90, 260, 135, 320, 80, 407, 135, 475, 80, 570, 135, 615, 90, 620,105 , 570, 142, 475, 87, 400, 142, 320, 87, 260, 142, 180, 100, smooth = "true", fill = "yellow")
screen.create_polygon (150, 150, 260, 215, 320, 160, 407, 215, 475, 160, 570, 215, 650, 150, 660,157, 570, 222, 475, 167, 400, 222, 320, 167, 260, 222, 145, 160, smooth = "true", fill = "green2")
 


#PEOPLE
for people in range(50):
    x = randint(50, 750)
    y = randint(475, 550)
    a = x -5
    b = y - 5
    x = x + 15
    a = a + 15
    colour = [ "bisque", "tan3", "brown", "peach puff", "khaki", "white"]
    skincolour = choice(colour)
    bodycolours1 = ["yellow", "red", "orange", "green", "blue",]
    bodycolour = choice(bodycolours1)
    screen.create_polygon(x, y, x + 6, y ,x + 8, y + 20, x - 3, y + 20, fill = bodycolour, outline = "black", smooth = "true")
    screen.create_oval(a, b, a +13, b + 13, fill = skincolour, outline = "black", width = 2)

#TEXT
screen.create_text(100,75, text="By  Nima Sheth", font="Arial 18", fill="black")
  

spacing = 50

for x in range(50, 800, spacing): 
    screen.create_line(x, 30, x, 600, fill="blue")
    screen.create_text(x, 10, text=str(x), font="Times 9", anchor = N)

for y in range(50, 600, spacing):
    screen.create_line(25, y, 800, y, fill="blue")
    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W)


screen.mainloop()
