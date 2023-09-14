import analyze 
from flask import Flask, render_template, request

#Create a Flask app
app = Flask(__name__)

@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_repository():
    # Handle the repository analysis request
    user_url = request.form.get("username")
    user_url = analyze.extract_url(user_url)
    username = user_url.split("/")[-1] if user_url else None
    if username:
        repos = analyze.get_user_repositories(username)
        if repos is not None:
            output = analyze.find_complex(repos)
            name, url, analysis = analyze.nameRepoData(output)
            if name and url and analysis:
                return render_template("index.html", result=name, repo_url=url, analysis=analysis)
        else:
            return render_template("index.html", error="Failed to fetch repositories.")
    else:
        return render_template("index.html", error="Invalid GitHub User")


if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000,threaded=True)