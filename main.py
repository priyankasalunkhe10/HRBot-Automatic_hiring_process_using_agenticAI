from flask import Flask, render_template, request, redirect
from database.requirement import init_db, insert_job, fetch_jobs

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_requirement",methods=["GET","POST"])
def add_requirement():
    if request.method == "POST":
        job_title = request.form["title"]
        skills = request.form["skills"]
        experience = request.form["experience"]

        insert_job(job_title, skills, experience)

        return render_template(
            "success.html", 
            title=job_title, 
            skills=skills, 
            experience=experience
        )

    return render_template("requirement_form.html")

@app.route("/show_requirement",methods=["GET"])
def show_requirements():
    jobs = fetch_jobs()
    return render_template("requirements.html", jobs=jobs)


if __name__=="__main__":
    app.run(debug=True)