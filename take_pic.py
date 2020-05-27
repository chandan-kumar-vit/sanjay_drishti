import cv2
import os
camera = cv2.VideoCapture(0)
camera2 = cv2.VideoCapture(0)
def click_pic():
	return_value, image = camera.read()
	cv2.imwrite('test'+'.jpg', image)
while(True):
	ret, frame=camera.read()
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF ==ord('p'):
		click_pic()
	elif cv2.waitKey(1) & 0xFF ==ord('q'):
		break

camera.release()
cv2.destroyAllWindows()

#os.system('python face_rec.py')

