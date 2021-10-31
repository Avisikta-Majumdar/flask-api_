from flask import Flask , render_template , request
import pickle
import numpy as np


app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def Homepage():
    return  render_template("index.html")

@app.route("/result",methods=["GET","POST"])
def Check():
    if request.method =='POST':
        Swidth = request.form['swidth']
        Slength = request.form['slength']
        Pwidth = request.form['pwidth']
        Plength = request.form['plength']
        with open('model_pickle', 'rb') as file:
            mp = pickle.load(file)
        # SepalLengthCm	SepalWidthCm	PetalLengthCm	PetalWidthCm
        check = [Slength , Swidth , Plength , Pwidth]
        # print(type(check), len(check))
        check = np.array(check).reshape(1, -1)
        # print(type(check), (check.shape))
        answer = mp.predict(check)[0]
        # print(answer)
        result_ = { 0 : 'versicolor' , 1 : 'virginica' , 2: 'setosa' }
        return render_template("result.html" , Species = result_.get(answer))

if __name__ == "__main__":
    app.run(debug = True)