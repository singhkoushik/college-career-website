from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [
  {
    'id':1,
    'title':'Software Engineer',
    'location':'Bengaluru, India',
    'salary':'RS. 12LPA'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location':'Pune, India'
  },
  {
    'id':3,
    'title':'ML Engineer',
    'location':'New York, USA',
    'salary':'RS. 50LPA'
  },
  {
    'id':4,
    'title':'Frontend Developer',
    'location':'Remote',
    'salary':'RS. 8LPA'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name="College")
print("hi")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  print("I'm inside if now")
  app.run(host='0.0.0.0',debug=True)