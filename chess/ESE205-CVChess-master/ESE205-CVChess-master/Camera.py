# import the necessary packages
import time
import cv2
import imutils
from picamera.array import PiRGBArray
class Camera:

	def __init__(self):
		self.cam = cv2.VideoCapture(0)

	def takePicture(self):

		# initialize the camera and grab a reference to the raw camera capture
		rawCapture = PiRGBArray(self.cam)

		# allow the camera to warmup
		time.sleep(1)

		# grab an image from the camera
		self.cam.capture(rawCapture, format="bgr")
		image = rawCapture.array
		resized = imutils.resize(image, height = 400, width = 400)


		return resized
