import cv2
import cognitive_face as CF
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import time 


class Face():
	KEY = '6e59a9ae0dc941e482e22fe58c936533' 
	CF.Key.set(KEY)

	BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'
	CF.BaseUrl.set(BASE_URL)

	ramp_frames = 6
	camera = ''

	for j in range(1,3):

		def get_image():
			camera_port = 0
			camera = cv2.VideoCapture(camera_port)
			retval, im = camera.read()
			return im

		for i in xrange(ramp_frames):
			temp = get_image()

		print("Taking image...")

		camera_capture = get_image()
		file = "image"+str(j)+".png"

		cv2.imwrite(file, camera_capture)
		del(camera)

		img_urls = ['image2.JPG','image2.jpg' ]

		faces = [CF.face.detect(img_url) for img_url in img_urls]

		for x in range(0, len(faces[0])):
			similarity = CF.face.verify(faces[0][x]['faceId'], faces[1][0]['faceId'])
			print (similarity)
			print("------------")
			time.sleep(3)