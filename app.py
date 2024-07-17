from flask import Flask, render_template
app=Flask(__name__)#object of class
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location':'Bangluru,India',
    'salary':'Rs.10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Delhi,India',
    'salary':'Rs.15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location':'Remote',
    'salary':'Rs.13,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location':'Remote',
    'salary':'Rs.14,00,000'
  }
]
@app.route("/")
def first():
  return render_template('home.html',
                         jobs=JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)