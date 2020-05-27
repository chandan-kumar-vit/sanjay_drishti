
from flask import Flask,render_template, url_for, request,session,redirect
import pymysql
import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
from time import sleep
import datetime
from werkzeug.utils import secure_filename
import json
import xlsxwriter
#from openpyxl import Workbook
#import xlwt
#from xlwt import Workbook
#from urllib2 import urlopen


"""
<-------------------- FACE RECOGNITION CODE- START ------------>
"""
def get_encoded_faces():

    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded

def unknown_image_encoded(img):

    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding

def classify_imgae(im):
	faces = get_encoded_faces()
	faces_encoded = list(faces.values())
	known_face_names = list(faces.keys())

	img = cv2.imread(im, 1)

   	face_locations = face_recognition.face_locations(img)

   	unknown_face_encodings = face_recognition.face_encodings(img, face_locations)
   	face_names=""
   	for face_encoding in unknown_face_encodings:
   		matches=face_recognition.compare_faces(faces_encoded, face_encoding)
   		name="unknown"

   		face_distances=face_recognition.face_distance(faces_encoded, face_encoding)
   		best_match_index = np.argmin(face_distances)
   		if matches[best_match_index]:
   			name=known_face_names[best_match_index]
   		face_names=name
   	
   	while True:
   		return face_names
"""
<---------------------------FACE RECOGNITION END---------------------------->
"""

app=Flask(__name__)
app.config['SESSION_TYPE']='memcached'
app.config['SECRET_KEY']='super secret key'
app.config['UPLOAD_FOLDER'] = '/home/chandan/projects/online_class/faces'

@app.route("/")

@app.route("/home")
def home():
	return render_template('home.html')


@app.route("/student_login",methods=['GET','POST'])
def student_login():
	flag=0
	if(request.method=='POST'):
		uname=request.form.get('uname')
		pwd=request.form.get('password')
	
		try:

			db= pymysql.connect(host='localhost',
	                             user='root',
	                             password='',
	                             db='sanjay_drishti',
	                             autocommit=True)
			cursor=db.cursor()
			q1="SELECT * FROM students NATURAL JOIN stud_reg_courses WHERE reg_no=%s"
			cursor.execute(q1,(uname))
			global results
			results=cursor.fetchall()
			print(results)
			if(pwd==results[0][5]):
				session['username']=uname

				return render_template('classroom.html',results=results)

			else:
				return "Incorrect password"
			
		except Exception, e:
			flag=0
			print("NO results found!")
			print(e)

		finally:
			db.close()
	else:
		return "Please Sign Up First"
	return "PLEASE SIGN UP FIRST!!"

@app.route("/student_signup",methods=['GET','POST'])
def student_signup():
		#inserting data into database
	try:
		db= pymysql.connect(host='localhost',
	                             user='root',
	                             password='',
	                             db='sanjay_drishti')
		if(request.method=='POST'):
			reg_no=request.form.get('reg_no')
			name=request.form.get('name')
			email=request.form.get('email')
			contact_no=request.form.get('contact_no')
			college=request.form.get('college')
			pwd=request.form.get('pwd')
			pic1=request.files['pic1']
			pic2=request.files['pic2']
			pic3=request.files['pic3']

			fn1=secure_filename(pic1.filename)
			print(fn1)
			pic1.save(os.path.join(app.config['UPLOAD_FOLDER'],fn1))

			fn2=secure_filename(pic2.filename)
			pic2.save(os.path.join(app.config['UPLOAD_FOLDER'],fn2))

			fn3=secure_filename(pic3.filename)
			pic3.save(os.path.join(app.config['UPLOAD_FOLDER'],fn3))

			print("All images saved")
			
			print("writing in DB")
			cursor=db.cursor()
			sql="INSERT INTO students VALUES(%s,%s,%s,%s,%s,%s)"
			cursor.execute(sql,(reg_no,name,email,contact_no,college,pwd))
			db.commit()
			msg="Your Account Created Successfully"
			return render_template('home.html',msg=msg)
		else:
			return "Problem in inserting data"
	
	except Exception, e:
		print str(e)

	finally:
		db.close()

	return "not done"


@app.route("/attend_class",methods=['GET','POST'])
def attend_class():
	if(request.method=='POST'):
		course=request.form.get('course')
		print(course)
	return render_template('attend_class.html',course=course)

@app.route("/join_class",methods=['GET','POST'])
def join_class():
	if(request.method=='POST'):
		url_class=request.form.get('class_link')
		url_vid=url_class+":8080/shot.jpg"
		url_aud=url_class+":8080/audio.wav"
		print(url_vid)
		print(url_aud)

		all_url={}

		all_url['links']={'video_link':url_vid,'audio_link':url_aud}
		with open('all_links.json','w') as f:
			json.dump(all_url,f)

		os.system('python alpha.py')
	return render_template('take_attendance.html')

@app.route("/attendance")
def attendance():
	os.system('python take_pic.py')
	attndee= classify_imgae("test.jpg")
	attndee=attndee[0:9]
	current_time = datetime.datetime.now()
	time= current_time.hour+current_time.minute
	workbook = xlsxwriter.Workbook('attendance_sheet.xlsx')
	worksheet = workbook.add_worksheet()
	worksheet.write('A1', 'reg_no')
	worksheet.write('B1', 'time')
	worksheet.write('A2', attndee)
	worksheet.write('B2', current_time)
	workbook.close() 

	return render_template('take_attendance.html',attndee=attndee)

@app.route("/log_out")
def log_out():
	session.clear()
	return render_template('home.html')

if __name__=='__main__':
	app.run(debug=True)