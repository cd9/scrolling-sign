from firebase import firebase
import serial
import time
import datetime
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

if __name__ == "__main__":
	time.sleep(5)
	SECRET = '6FmRtZWFEupG9O140dJmr86XUfBcWxawvRkYAzar'
	DSN = 'https://scrolling-sign.firebaseio.com'
	EMAIL = 'dalyco884@gmail.com'
	authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
	firebase = FirebaseApplication(DSN, authentication)
	data = firebase.get('/mode', None)
	mode = firebase.get('/data', None)
	showtext = "booting up..."
	last = None
	while True:
		print("refreshing")
		data = firebase.get('/data', None)
		mode = firebase.get('/mode', None)
		last = showtext
		if mode is 0:
			#MODE 0 = static text
			showtext = data['text']
			print(showtext)

		if mode is 1:
			showtext = datetime.datetime.now().weekday()
			if showtext is 0:
				showtext = data['monday']
			elif showtext is 1:
				showtext = data['tuesday']
			elif showtext is 2:
				showtext = data['wednesday']
			elif showtext is 3:
				showtext = data['thursday']
			elif showtext is 4:
				showtext = data['friday']
			elif showtext is 5:
				showtext = data['saturday']
			elif showtext is 6:
				showtext = data['sunday']
			print showtext
		if (last!= showtext):
			ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout = 2)
			time.sleep(5)
			print(last)
			print(showtext)
			ser.write(str(showtext))
			last = showtext
			print ('it different')
			ser.close()
