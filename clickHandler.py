import socket, traceback, win32api, win32con, time, os, turtle 
from win32api import GetSystemMetrics

host = ''
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

print("Success binding")


############################################################
#						Turtle stuff					   #
############################################################
      # Create our favorite turtle

#gyro 1 y rotation, gyro3 z rotation
def read():
    print("Reading")
    for i in range (10):
    	message, address = s.recvfrom(8192)
    	messageString = message.decode("utf-8")
    #print(messageString)
    key1 = "RotationVector1>"
    key2 = "RotationVector2>"
    key3 = "RotationVector3>" #placeholder
    xRotation = messageString[(messageString.index(key1) + len(key1))
     : (messageString.index("/" + key1) -1)]

    yRotation = messageString[(messageString.index(key2) + len(key2))
     : (messageString.index("/" + key2) -1)]

    zRotation = messageString[(messageString.index(key3) + len(key3))
     : (messageString.index("/" + key3) -1)]


    return [float(xRotation) + 1, float(yRotation) + 1, float(zRotation) + 1]


# The next four functions are our "event handlers".
counter = [0]
#Used for calibration
xCList = []
yCList = []
zCList = []
def h1():
	readOut = read()
	xCList.append(readOut[0])
	yCList.append(readOut[1])
	zCList.append(readOut[2])
	print(xCList)
	print(yCList)
	print(zCList)
	counter[0] += 1
	if (counter[0] == 4):
		move()

def click(x,y):
    win32api.SetCursorPos((x,y))

def move():
	print("moving")
	while 1:
		currentPos = read()
		xDistance = (zCList[0] - zCList[1])
		yDistance = (yCList[0] - yCList[2])
		posxDistance = (currentPos[2] - zCList[1])
		posyDistance = (currentPos[1] - yCList[0])

		if (xDistance > 1):
			xDistance = 1 - xDistance % 1
		if (yDistance > 1):
			yDistance = 1 - yDistance % 1
		if (posxDistance > 1):
			posxDistance = 1 - posxDistance % 1
		if (posyDistance > 1):
			posyDistance = 1 - posyDistance % 1
		x = posxDistance / xDistance

		y = posyDistance / yDistance

		print("X: " + str(x) + " Y: " + str(y))

		click(int(x)* 400, int(y) * 400)

while 1:
	if (win32api.GetAsyncKeyState(ord('H'))):
		h1()
		time.sleep(1)
	read()