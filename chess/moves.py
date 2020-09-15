import pyfirmata
import time
import keyboard
angle1=160
angle2=160

angle4=160
angle5=160
angle6=90
board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()
servo=board.get_pin('d:11:s')
servo2=board.get_pin('d:10:s')
servo3=board.get_pin('d:9:s')
servo4=board.get_pin('d:6:s')
servo5=board.get_pin('d:5:s')
servo6=board.get_pin('d:3:s')
input='a1'
def start(angle1,angle2,angle4,angle5,angle6):
	angle1=160
	angle2=160

	angle4=160
	angle5=160
	angle6=90
	servo.write(angle1)
	servo2.write(angle2)
	servo4.write(angle4)
	servo5.write(angle5)
	servo6.write(angle6)
	time.sleep(1)
def pos(input):
	if input=='a1':
		return([153, 125, 139, 160, 81])
	if input=='b1':
		return([153, 114, 148, 160, 89])
	if input=='c1':
		return([157, 102, 154, 160, 93])
	if input=='d1':
		return([153, 86, 169, 160, 101])
start(angle1,angle2,angle4,angle5,angle6)
angles=pos(input)
servo.write(angles[0])
time.sleep(1)
servo2.write(angles[1])
time.sleep(1)
servo4.write(angles[2])
time.sleep(1)
servo5.write(angles[3])
time.sleep(1)
servo6.write(angles[4])
time.sleep(1)

