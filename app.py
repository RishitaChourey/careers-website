from flask import Flask, render_template,jsonify
from database import load_jobs_from_db
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
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)