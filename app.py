from flask import Flask, render_template, request
import os
import cv2

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'static'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload',methods=['POST'])
def upload():
    file=request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'],file.filename))
    return render_template('frames.html')
    
    
capture= cv2.VideoCapture(r"C:\Users\HP\Documents\Flask_Task\static\video.mp4")

try:
    if not os.path.exists('data'):
        os.makedirs('data')

except OSError:
    print('Error:Creating directory of data')

sframe=0


while(True):
    ret,frame =capture.read()

    if ret:
        name='./data/frame' + str(sframe)+ '.jpg'
        cv2.imwrite(name,frame)
        sframe+=1
        

    else:
        break

capture.release()

if __name__=='__main__':
    app.run(debug=True)