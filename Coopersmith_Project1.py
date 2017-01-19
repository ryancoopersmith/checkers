#My first Python project
#Author: Ryan Coopersmith (ryancoopersmith1@gmail.com)
import Tkinter
from Tkinter import *
root = Tkinter.Tk()
root.title("Checkers")
Canv = Tkinter.Canvas(root, bg="blue", height=645, width=624)
Canv.pack()
Canv.focus()

player1 = raw_input("Enter the name of Player 1: ")
player2 = raw_input("Enter the name of Player 2: ")
#add code for a Python Checkers title here

print "Python Checkers Rules: \n"
print "1) To jump another piece, click on the piece you want to move and if the Jump"
print "button is highlighted, click it and then move to your desired square. \n"
print "2) To double jump, click on the piece you want to move, hit the Double Jump"
print "button, click on the first square you wish to jump to then click on the"
print "second square you wish to jump to. \n"
print "3) Be responsible with your jumps! This program may detect more jump"
print "opportunities than there are. \n"
print "4) To become a king, reach the opposite end of the board"
print "(black pieces will become purple, and red pieces will become orange). \n"
print "5) Have fun! \n"


mainCounter = 1
counter = 0
x = -48
y = 24
x2 = 24
y2 = 96
stopper = 2
switch = False
blackPos = []
redPos = []
jump = False
blackLost = 0
redLost = 0
doubleJump = False

while mainCounter < 58:
	mainCounter += 1
	if counter < 8:
		counter += 1
		x += 72
		x2 += 72
		if mainCounter % 2 == 0:
			color = "white"
		else:
			color = "gray"
		Canv.create_rectangle(x, y, x2, y2,tags = "square", fill = color)
		if color == "gray" and mainCounter < 24:
			Canv.create_oval(x, y, x2, y2,tags = "piece", fill = "red")
		elif color == "gray" and mainCounter > 38:
			Canv.create_oval(x, y, x2, y2,tags = "piece", fill = "black")
	else:
		mainCounter -= 1
		counter = 1
		y += 72
		y2 += 72
		x = 24
		x2 = 96
		if mainCounter % 2 == 0:
			color = "white"
		else:
			color = "gray"
		Canv.create_rectangle(x, y, x2, y2,tags = "square", fill = color)
		if color == "gray" and mainCounter < 22:
			Canv.create_oval(x, y, x2, y2,tags = "piece", fill = "red")
		elif color == "gray" and mainCounter > 36:
			Canv.create_oval(x, y, x2, y2,tags = "piece", fill = "black")

def callback(event):
	global stopper
	global prev
	cur = Canv.find_withtag("current")[0]
	if stopper % 2 == 0:
		Canv.itemconfig(cur, outline = "yellow")
		if stopper != 2:
			Canv.itemconfig(prev, outline = "black")
		stopper += 1
	else:
		Canv.itemconfig(cur, outline = "yellow")
		Canv.itemconfig(prev, outline = "black")
		stopper += 1
	prev = cur
	jumpPieces()
	return prev

def movePieces(event):
	global prev
	global switch
	global jump
	global doubleJump
	if 'prev' in globals():
		Canv.tag_raise("filler")
		nav = Canv.coords(prev)
		x = nav[0]
		y = nav[1]
		if jump == True:
			if event.x < x and event.x > x - 144 and event.y < y and event.y > y - 144 and switch == False:
				Canv.move(prev,-144,-144)
				if doubleJump == False:
					switch = True
					Canv.itemconfig(txt, text = player2, fill = "red")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x - 72, y - 72, x, y, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player2lost()
			elif event.x > x and event.x < x + 216 and event.y < y and event.y > y - 144 and switch == False:
				Canv.move(prev,144,-144)
				if doubleJump == False:
					switch = True
					Canv.itemconfig(txt, text = player2, fill = "red")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x + 144, y - 72, x + 72, y, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player2lost()
			elif event.x < x and event.x > x - 144 and event.y > y and event.y < y + 216 and switch == True:
				Canv.move(prev,-144,144)
				if doubleJump == False:
					switch = False
					Canv.itemconfig(txt, text = player1, fill = "black")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x - 72, y + 72, x, y + 144, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player1lost()
			elif event.x > x and event.x < x + 216 and event.y > y and event.y < y + 216 and switch == True:
				Canv.move(prev,144,144)
				if doubleJump == False:
					switch = False
					Canv.itemconfig(txt, text = player1, fill = "black")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x + 144, y + 72, x + 72, y + 144, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player1lost()
			DoubleJumpOff()
		else:
			if event.x < x and event.x > x - 72 and event.y < y and event.y > y - 72 and switch == False:
				Canv.move(prev,-72,-72)
				switch = True
				Canv.itemconfig(txt, text = player2, fill = "red")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x > x and event.x < x + 144 and event.y < y and event.y > y - 72 and switch == False:
				Canv.move(prev,72,-72)
				switch = True
				Canv.itemconfig(txt, text = player2, fill = "red")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x < x and event.x > x - 72 and event.y > y and event.y < y + 144 and switch == True:
				Canv.move(prev,-72,72)
				switch = False
				Canv.itemconfig(txt, text = player1, fill = "black")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x > x and event.x < x + 144 and event.y > y and event.y < y + 144 and switch == True:
				Canv.move(prev,72,72)
				switch = False
				Canv.itemconfig(txt, text = player1, fill = "black")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			Canv.itemconfig(prev, outline = "black")
		checkForKing()
		return switch

def jumpPieces():
	global prev
	global jump
	jump = False
	nav = Canv.coords(prev)
	xVal = nav[0]
	yVal = nav[1]
	if switch == False:
		blackPos.append([xVal,yVal])
	else:
		redPos.append([xVal,yVal])
	b = len(blackPos)
	r = len(redPos)
	diff = abs(r - b)
	for i in range(diff - 1):
		if r  > b:
			redPos.pop(0)
		elif b  > r:
			blackPos.pop(0)
	for j in range(len(blackPos)-1):
		for i in range(len(blackPos)-1):
			 firstComp = blackPos[j][0]
			 secondComp = redPos[i][0]
			 thirdComp = blackPos[j][1]
			 fourthComp = redPos[i][1]
			 if thirdComp == fourthComp - 216 or thirdComp - 216 == fourthComp or thirdComp - 288 == fourthComp or thirdComp == fourthComp - 288:
				 if i != j  and firstComp == secondComp - 72 or firstComp - 72 == secondComp or firstComp - 216 == secondComp or firstComp == secondComp - 216 or firstComp - 144 == secondComp or firstComp == secondComp - 144 or firstComp == secondComp:
					 jump = True
				 else:
					 jump = False
	if jump == True:
		jump = False
		button.configure(command=Jump, bg = "yellow")
		button2.configure(command=DoubleJump, bg = "yellow")
	return jump

def replace(event):
	global prev
	cur = Canv.find_withtag("current")[0]
	Canv.tag_lower("filler")
	Canv.tag_raise(prev)
	Canv.itemconfig(cur, tags = "nofiller")

def Jump():
	global jump
	jump = True
	button.configure(bg = "white")
	button2.configure(bg="white")
	return jump

def DoubleJump():
	global doubleJump
	doubleJump = True
	button2.configure(bg="white")
	button.configure(bg = "white")
	Jump()
	return doubleJump

def DoubleJumpOff():
	global doubleJump
	doubleJump = False
	return doubleJump

def checkForKing():
	global prev
	global switch
	nav = Canv.coords(prev)
	y = nav[1]
	if switch == True and y == 24:
		Canv.itemconfig(prev, tags = "king", fill = "purple")
	elif switch == False and y == 528:
		Canv.itemconfig(prev, tags = "king", fill = "orange")

def kingCallback(event):
	global stopper
	global prev
	cur = Canv.find_withtag("current")[0]
	if stopper % 2 == 0:
		Canv.itemconfig(cur, outline = "yellow")
		if stopper != 2:
			Canv.itemconfig(prev, outline = "black")
		stopper += 1
	else:
		Canv.itemconfig(cur, outline = "yellow")
		Canv.itemconfig(prev, outline = "black")
		stopper += 1
	prev = cur
	Canv.tag_bind("square", "<Button-1>", moveKing)
	jumpPieces()
	return prev

def moveKing(event):
	global prev
	global switch
	global jump
	global doubleJump
	if 'prev' in globals():
		Canv.tag_raise("filler")
		nav = Canv.coords(prev)
		x = nav[0]
		y = nav[1]
		if jump == True:
			if event.x < x and event.x > x - 144 and event.y < y and event.y > y - 144 and switch == False:
				Canv.move(prev,-144,-144)
				if doubleJump == False:
					switch = True
					Canv.itemconfig(txt, text = player2, fill = "red")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x - 72, y - 72, x, y, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player2lost()
			elif event.x > x and event.x < x + 216 and event.y < y and event.y > y - 144 and switch == False:
				Canv.move(prev,144,-144)
				if doubleJump == False:
					switch = True
					Canv.itemconfig(txt, text = player2, fill = "red")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x + 144, y - 72, x + 72, y, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player2lost()
			elif event.x < x and event.x > x - 144 and event.y > y and event.y < y + 216 and switch == False:
				Canv.move(prev,-144,144)
				if doubleJump == False:
					switch = True
					Canv.itemconfig(txt, text = player2, fill = "red")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x - 72, y + 72, x, y + 144, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player2lost()
			elif event.x > x and event.x < x + 216 and event.y > y and event.y < y + 216 and switch == False:
				Canv.move(prev,144,144)
				if doubleJump == False:
					switch = True
					Canv.itemconfig(txt, text = player2, fill = "red")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x + 144, y + 72, x + 72, y + 144, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player2lost()
			elif event.x < x and event.x > x - 144 and event.y > y and event.y < y + 216 and switch == True:
				Canv.move(prev,-144,144)
				if doubleJump == False:
					switch = False
					Canv.itemconfig(txt, text = player1, fill = "black")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x - 72, y + 72, x, y + 144, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player1lost()
			elif event.x > x and event.x < x + 216 and event.y > y and event.y < y + 216 and switch == True:
				Canv.move(prev,144,144)
				if doubleJump == False:
					switch = False
					Canv.itemconfig(txt, text = player1, fill = "black")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x + 144, y + 72, x + 72, y + 144, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player1lost()
			elif event.x < x and event.x > x - 144 and event.y < y and event.y > y - 144 and switch == True:
				Canv.move(prev,-144,-144)
				if doubleJump == False:
					switch = False
					Canv.itemconfig(txt, text = player1, fill = "black")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x - 72, y - 72, x, y, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player1lost()
			elif event.x > x and event.x < x + 216 and event.y < y and event.y > y - 144 and switch == True:
				Canv.move(prev,144,-144)
				if doubleJump == False:
					switch = False
					Canv.itemconfig(txt, text = player1, fill = "black")
					Canv.itemconfig(prev, outline = "black")
				Canv.create_rectangle(x + 144, y - 72, x + 72, y, tags = "filler square", fill = "gray")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
				player1lost()
			if doubleJump == False:
				Canv.tag_bind("square", "<Button-1>", movePieces)
			DoubleJumpOff()
		else:
			if event.x < x and event.x > x - 72 and event.y < y and event.y > y - 72 and switch == False:
				Canv.move(prev,-72,-72)
				switch = True
				Canv.itemconfig(txt, text = player2, fill = "red")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x > x and event.x < x + 144 and event.y < y and event.y > y - 72 and switch == False:
				Canv.move(prev,72,-72)
				switch = True
				Canv.itemconfig(txt, text = player2, fill = "red")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x < x and event.x > x - 72 and event.y > y and event.y < y + 144 and switch == False:
				Canv.move(prev,-72,72)
				switch = True
				Canv.itemconfig(txt, text = player2, fill = "red")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x > x and event.x < x + 144 and event.y > y and event.y < y + 144 and switch == False:
				Canv.move(prev,72,72)
				switch = True
				Canv.itemconfig(txt, text = player2, fill = "red")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x < x and event.x > x - 72 and event.y > y and event.y < y + 144 and switch == True:
				Canv.move(prev,-72,72)
				switch = False
				Canv.itemconfig(txt, text = player1, fill = "black")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x > x and event.x < x + 144 and event.y > y and event.y < y + 144 and switch == True:
				Canv.move(prev,72,72)
				switch = False
				Canv.itemconfig(txt, text = player1, fill = "black")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x < x and event.x > x - 72 and event.y < y and event.y > y - 72 and switch == True:
				Canv.move(prev,-72,-72)
				switch = False
				Canv.itemconfig(txt, text = player1, fill = "black")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			elif event.x > x and event.x < x + 144 and event.y < y and event.y > y - 72 and switch == True:
				Canv.move(prev,72,-72)
				switch = False
				Canv.itemconfig(txt, text = player1, fill = "black")
				Canv.create_rectangle(x, y, x + 72, y + 72, tags = "filler square", fill = "gray")
			Canv.itemconfig(prev, outline = "black")
		return switch

def player2lost():
	global redLost
	redLost += 1
	if redLost == 12:
		Canv.itemconfig(txt, text = "Winner: " + player1+  "!", fill = "black")
	return redLost

def player1lost():
	global blackLost
	blackLost += 1
	if blackLost == 12:
		Canv.itemconfig(txt, text = "Winner: " + player2 + "!", fill = "red")
	return blackLost

Canv.tag_bind("piece", "<Button-1>", callback)
Canv.tag_bind("square", "<Button-1>", movePieces)
Canv.tag_bind("filler", "<Button-1>", replace)
Canv.tag_bind("king", "<Button-1>", kingCallback)
Canv.tag_raise("piece")
txt = Canv.create_text(312,625,text = player1, fill = "black", font = 100)
button2 = Button(root, text="Double Jump", bg="white")
button2.pack(side="right", expand="True", fill="both")
button = Button(root, text="Jump          ", bg="white")
button.pack(side="left", expand="True", fill="both")

root.mainloop()
