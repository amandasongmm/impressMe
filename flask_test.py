from flask import Flask, render_template, request, redirect
import numpy as np
import cv2
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('first_page.html')

@app.route("/score")
def score():
    return "score"

@app.route('/post', methods=['POST'])
def upload_im():
    if request.method == 'POST':
        # print request.form['image']
        image_file = request.files.getlist('image')
        print image_file
        for file in image_file:
            img = file.read()
            np_img = np.fromstring(img, np.uint8)
            img_arr = cv2.imdecode(np_img, cv2.CV_LOAD_IMAGE_UNCHANGED)
            print img_arr.shape

        print 'yesy'
        score_value = [1, 2, 3]
    return redirect('score')


app.run(debug=True)