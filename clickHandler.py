import socket, traceback, win32api, win32con, time, os

host = ''
port = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.bind((host, port))

#used for debugging

def click(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#gyro 1 y rotation, gyro3 z rotation

print("Success binding")
x = 500
y = 500
while 1:
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


    print (xRotation + " " + yRotation + " " + zRotation)
    time.sleep(0.01)
    for i in range (10):
    	x += int(float(zRotation) * -10)
    	y += int(float(yRotation) * -10)
    	#click(x,y)
	
# Example of XML data received:
# <Node Id>node12</Node Id>
# <GPS>
# <Latitude>1.123123</Latitude>
# <Longitude>234.1231231</Longitude>
# <Accuracy>40.0</Accuracy>
# </GPS>
# <Accelerometer>
# <Accelerometer1>0.38444442222</Accelerometer1>
# <Accelerometer2>0.03799999939</Accelerometer2>
# <Accelerometer3>9.19400000331</Accelerometer3>
# </Accelerometer>
# <TimeStamp>1370354489083</TimeStamp>
