from flask import Flask,render_template,request
import pandas as pd
import pandas_profiling as pp

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return render_template('dataanalysis.html')

@app.route('/eda',methods=['POST'])
def data():
    if(request.method=='POST'):
        f=request.form['file']
        df=pd.read_csv(f)
        result=df.head(5)
    return render_template('result.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)