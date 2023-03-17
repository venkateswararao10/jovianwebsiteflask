from flask import Flask,render_template
jobs=[
  {'id':1,'title':'Data-scientist','location':'Bengaluru','salary':'Rs 20,00,000'},
  {'id':2,'title':'Data-Analyst','location':'Delhi','salary':'Rs 10,00,000'},
  {'id':3,'title':'Python Developer','location':'Hyderabad'}
]

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html",jobs=jobs,company="Venky")

@app.route('/api/jobs')
def joblist():
  return jobs
if __name__=="__main__":
   app.run( host='0.0.0.0',port=5000,debug=True)