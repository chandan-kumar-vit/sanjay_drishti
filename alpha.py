import os
import requests
import cv2
import numpy as np
import json
f=open('all_links.json')
link=json.load(f)

url=link['links']['video_link']


while True:
	img_resp=requests.get(url)
	img_arr= np.array(bytearray(img_resp.content), dtype=np.uint8)
	img=cv2.imdecode(img_arr,-1)
	#os.system('python mike.py')
	cv2.imshow("AndroidCam",img)
	
	if cv2.waitKey(1)==27:
		break
		f.close

