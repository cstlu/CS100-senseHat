from sense_hat import SenseHat
sense = SenseHat()
import socket
while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(("8.8.8.8", 80))
		sense.show_message(s.getsockname()[0])
		s.close()
	except:
		sense.show_message("FALSE")
