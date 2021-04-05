from flask import Flask
from flask import render_template
from flask import request
from keras.models import load_model

app = Flask("Adarsh Industries")

model = load_model("dia_model.h5")

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/check', methods=['GET'])
def mymenu():
    pregnant = int(request.args.get('pregnant'))
    glucose = int(request.args.get('glucose'))
    bp = int(request.args.get('bp'))
    thickness = int(request.args.get('thickness'))
    insulin = int(request.args.get('insulin'))
    bmi = float(request.args.get('bmi'))
    pedigree = float(request.args.get('pedigree'))
    age = int(request.args.get('age'))
    output = model.predict([[pregnant, glucose, bp, thickness, insulin, bmi, pedigree, age]])
    if output == '0':
        return render_template('pass_test.html')
    else:
        return render_template('fail_test.html')


app.run(host="0.0.0.0", port=3456)
