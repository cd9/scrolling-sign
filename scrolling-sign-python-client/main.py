from firebase import firebase
import serial
import time
import ntplib
from time import ctime
from firebase.firebase import FirebaseApplication, FirebaseAuthentication

if __name__ == "__main__":

	SECRET = '6FmRtZWFEupG9O140dJmr86XUfBcWxawvRkYAzar'
	DSN = 'https://scrolling-sign.firebaseio.com'
	EMAIL = 'dalyco884@gmail.com'
	authentication = FirebaseAuthentication(SECRET,EMAIL, True, True)
	firebase = FirebaseApplication(DSN, authentication)
	data = firebase.get('/mode', None)
	mode = firebase.get('/data', None)
	#ser = serial.Serial('')
	time.sleep(1)
	showtext = "booting up..."
	#ser.write(showtext)
	c = ntplib.NTPClient()
	response = c.request('europe.pool.ntp.org', version=3)

	print(ctime(response.tx_time))

	while True:
		print("refreshing")
		data = firebase.get('/data', None)
		mode = firebase.get('/mode', None)
		if mode is 0:
			#MODE 0 = static text
			showtext = data['text']
			print(showtext)

		if mode is 1:
			print(showtext)
			response = c.request('europe.pool.ntp.org', version=3)
			showtext = ctime(response.tx_time)[0:3]