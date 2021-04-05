from flask import Flask
from flask import render_template
from flask import request
#from keras.models import load_model

app = Flask("Adarsh Industries")

#model = load_model("dia_model.h5")

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/check', methods=['GET'])
def mymenu():
    pregnant = request.args.get('pregnant')
    glucose = request.args.get('glucose')
    bp = request.args.get('bp')
    thickness = request.args.get('thickness')
    insulin = request.args.get('insulin')
    bmi = request.args.get('bmi')
    pedigree = request.args.get('pedigree')
    age = request.args.get('age')
    #output = model.predict([[pregnant, glucose, bp, thickness, insulin, bmi, pedigree, age]])
    if pregnant == '0':
        return render_template('pass_test.html')
    else:
        return render_template('fail_test.html')


app.run(host="192.168.29.22", port=3456)
