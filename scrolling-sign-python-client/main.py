from firebase import firebase
import serial
import time
import datetime
from firebase.firebase import FirebaseApplication, FirebaseAuthentication
from kraken import kraken

SIGN_LENGTH = 26;
repetitions = 5;

ser = None

def writeString(s, repetitions):
	for i in range(0, SIGN_LENGTH):
		time.sleep(0.01)
		ser.write(' ')

	for j in range(0, repetitions):
		for i in range(0, len(s)):
			time.sleep(0.01)
			ser.write(s[i])

		for i in range(0, SIGN_LENGTH/4):
			time.sleep(0.01)
			ser.write(' ')

	time.sleep(0.01)
	ser.write('~')


if __name__ == "__main__":
	k = kraken()
	ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout = 2)
	time.sleep(5)
	SECRET = '6FmRtZWFEupG9O140dJmr86XUfBcWxawvRkYAzar'
	DSN = 'https://scrolling-sign.firebaseio.com'
	EMAIL = 'dalyco884@gmail.com'
	authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
	firebase = FirebaseApplication(DSN, authentication)
	data = firebase.get('/data', None)
	mode = data['mode']
	showtext = "booting up..."
	last = None
	while True:
		print("refreshing")
		data = firebase.get('/data', None)
		mode = data['mode']
		print(mode)
		last = showtext
		if mode is 0:
			#MODE 0 = static text
			showtext = data['text']
			print(showtext)
			repetitions = 3
		elif mode is 1:
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
			print(showtext)
			repetitions = 5
		elif mode is 2:
			pair = data['crypto']['pair']
			price = k.getTickerInfo(pair)['result']['XETHZUSD']['a'][0]
			showtext = str(pair)+': '+str(price)
			repetitions = 10

		if (last!= showtext):
			writeString(showtext, repetitions)
			last = showtext
			print ('it different')