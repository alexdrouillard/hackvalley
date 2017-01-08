import socket, traceback, win32api, win32con, time

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
while 1:
    message, address = s.recvfrom(8192)
    messageString = message.decode("utf-8")
    #print(messageString)
    key1 = "Gyroscope1>"
    key2 = "Gyroscope2>"
    key3 = "Gyroscope3>"
    gyro1 = messageString[(messageString.index(key1) + len(key1))
     : (messageString.index("/" + key1) -1)]

    gyro2 = messageString[(messageString.index(key2) + len(key2))
     : (messageString.index("/" + key2) -1)]

    gyro3 = messageString[(messageString.index(key3) + len(key3))
     : (messageString.index("/" + key3) -1)]


    print (gyro1 + " " + gyro2 + " " + gyro3)

    click(int(float(gyro3)) * 10,int(float(gyro1)) * 10)
	
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
