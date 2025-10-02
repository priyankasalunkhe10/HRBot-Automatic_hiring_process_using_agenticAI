from flask import Flask, render_template, request
from database.requirement import init_db, insert_job, fetch_jobs

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_requirement")
def add_requirement():
    return render_template("requirement_form.html")

@app.route("/submit_requirement",methods=['POST'])
def submit():
    job_title = request.form["title"]
    skills = request.form["skills"]
    experience = request.form["experience"]

    insert_job(job_title,skills,experience)

    return render_template("success.html",title=job_title,skills=skills,experience=experience)

@app.route("/requirements")
def show_requirements():
    jobs = fetch_jobs()
    return render_template("requirments.html",jobs=jobs)


if __name__=="__main__":
    app.run(debug=True)