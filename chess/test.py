import pyfirmata
import time
import keyboard
angle1=160
angle2=0
angle3=10
angle4=0
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
servo.write(angle1)
servo2.write(angle2)
servo3.write(angle3)
servo4.write(angle4)
servo5.write(angle5)
servo6.write(angle6)


while True:
	if keyboard.is_pressed('w'):
         if angle1<180:
        		angle1+=1
        		print(angle1)
        		servo.write(angle1)
        		time.sleep(0.05)
	if keyboard.is_pressed('s'):
		if angle1>=0:
        		angle1=angle1-1
        		print(angle1)
        		servo.write(angle1)
        		time.sleep(0.05)	
	if keyboard.is_pressed('a'):
         if angle2<180:
        		angle2+=1
        		print(angle2)
        		servo2.write(angle2)
        		time.sleep(0.05)
	if keyboard.is_pressed('d'):
		if angle2>0:
        		angle2=angle2-1
        		print(angle2)
        		servo2.write(angle2)
        		time.sleep(0.05)	
	if keyboard.is_pressed('q'):
         if angle3<180:
        		angle3+=1
        		print(angle3)
        		servo3.write(angle3)
        		time.sleep(0.05)
	if keyboard.is_pressed('e'):
		if angle3>0:
        		angle3=angle3-1
        		print(angle3)
        		servo3.write(angle3)
        		time.sleep(0.05)		
	if keyboard.is_pressed('r'):
         if angle4<180:
        		angle4+=1
        		print(angle4)
        		servo4.write(angle4)
        		time.sleep(0.05)
	if keyboard.is_pressed('f'):
		if angle4>0:
        		angle4=angle4-1
        		print(angle4)
        		servo4.write(angle4)
        		time.sleep(0.05)		
	if keyboard.is_pressed('t'):
         if angle5<180:
        		angle5+=1
        		print(angle5)
        		servo5.write(angle5)
        		time.sleep(0.05)
	if keyboard.is_pressed('g'):
		if angle5>0:
        		angle5=angle5-1
        		print(angle5)
        		servo5.write(angle5)
        		time.sleep(0.05)
	if keyboard.is_pressed('z'):
         if angle6<180:
        		angle6+=1
        		print(angle6)
        		servo6.write(angle6)
        		time.sleep(0.05)
	if keyboard.is_pressed('x'):
         if angle6>0:
        		angle6=angle6-1
        		print(angle6)
        		servo6.write(angle6)
        		time.sleep(0.05)
	if keyboard.is_pressed('l'):
		print(angle1,angle2,angle4,angle5,angle6)		
	
servo.write(10)
time.sleep(5)
