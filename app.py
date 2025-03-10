from flask import Flask, render_template,jsonify, request
from database import load_job_from_db, load_jobs_from_db,add_application_to_db,db_port

app=Flask(__name__)#object of class

@app.route("/")
def first():
  jobs_list=load_jobs_from_db()
  return render_template('home.html',
                         jobs=jobs_list)

@app.route("/api/jobs")#application programming interface-returns structured data (here-json) instead of html
def list_jobs():
  jobs_list=load_jobs_from_db()
  return jsonify(jobs_list)



@app.route("/job/<int:id>")
def show_job(id):
  job=load_job_from_db(id)
  if not job:
    return "Not Found",404
  
  job_dict = job._asdict()
  return render_template('jobpage.html',job=job_dict)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data=request.form
  add_application_to_db(id,data)
  return render_template('application_submitted.html',application=data)



if __name__=="__main__":
  app.run(host='0.0.0.0',port=db_port,debug=True)