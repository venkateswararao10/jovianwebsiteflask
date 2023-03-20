from flask import Flask, render_template, jsonify, request
from mysqlconnectordatabase import db

#from pymongocon import fun
'''jobs=[
  {'id':1,'title':'Data-scientist','location':'Bengaluru','salary':'Rs 20,00,000'},
  {'id':2,'title':'Data-Analyst','location':'Delhi','salary':'Rs 10,00,000'},
  {'id':3,'title':'Python Developer','location':'Hyderabad'}
]'''
d = db()
jobs = d.fun()
app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=jobs, company="Venky")


@app.route('/api/jobs')
def joblist():
  return jobs


@app.route('/api/<id>')
def job(id):
  re = d.loadjob(id)
  return jsonify(re)


@app.route('/job/<id>')
def jobpage(id):
  re = d.loadjob(id)
  if not re:
    return "Not Found", 404

  return render_template('jobpage.html', job=re)


@app.route('/job/<id>/apply', methods=['post'])
def jobapp(id):
  print(request.form)
  data = dict(request.form)
  job = d.loadjob(id)
  #job = load_job_from_db(id)
  d.apptodb(id, data)
  #fun(data)
  return render_template('applicationsubmitted.html',
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
