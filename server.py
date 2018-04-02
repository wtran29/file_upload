import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\Users\wtran\Desktop\Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "keepitsecret"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/result', methods=['POST'])
def upload_file():
	result = True
	if 'file' not in request.files:
		flash('Your file upload failed. Please try again.')
		result = False
	file = request.files['file']
	if file.filename == '' or not allowed_file(file.filename):
		flash('Your file upload failed. Please try again.')
		result = False
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('Your file has been successfully uploaded!')
	return render_template('result.html', result=result)

app.run(debug=True)