import openai
import re
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from github import Github

app = Flask(__name__)

# Set up OpenAI API credentials
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def extract_url(user_url):
    pattern = r"(?:https?://)?(?:www\.)?github\.com/([a-zA-Z0-9_-]+)"
    match = re.search(pattern, user_url)
    if match:
        return match.group(0)
    else:
        return None


def get_user_repositories(username):
    client = Github(os.getenv('GITHUB_TOKEN'))
    user = client.get_user(username)
    repos = user.get_repos()
    repo_info = []
    for repo in repos:
        # If repo is a fork and no one starred it, skip it
        if repo.fork and repo.stargazers_count==0:
            continue
        print(repo.name)
        render_template("index.html", currepo=repo.name)
        repo_info.append({
            "name": repo.name,
            "url": repo.html_url,
            "description": repo.description,
            "contributors": repo.get_contributors().totalCount,
            "size": repo.size,
            "language": repo.language,
            "topics": repo.get_topics(),
            "stars": repo.stargazers_count,
            "forks": repo.forks_count,
            "labels": repo.get_labels(),
            "issues": repo.get_issues(state="all"),
        })
    return repo_info


context = """
Utilizing the provided JSON data of a user's GitHub repositories, conduct a comprehensive analysis to pinpoint the repository 
with the highest level of technical complexity. Delve into a multitude of criteria, encompassing repository size, contributors
(striving for at least 4), tags, stargazer count as starts, pertinent topics, issues, pull requests, fork count, and the repository description. 
Once determined, furnish summary but concise (within 100 words) yet technically-informed summary elucidating the facets that contribute to its complexity.

( Most Important Must follow ) output format - all in one line & no double quotes around values ( IMOPORTANT ): name = repo_name , url = repo_url, justify  = analysis 
\
"""


def find_complex(json_data):
    # Generate analysis justification using GPT-3
    prompt = f"Analyzing repository {json_data}."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {
                "role": "user",
                "content": context,
            },
        ],
        temperature=0,
        max_tokens=200,
    )
    analysis = response.choices[0].message.content
    return analysis


def nameRepoData(input_string):
    # Use regular expressions to extract name, url, and analysis
    # Define regular expressions to match the desired values
    name_pattern = r'name = ([^,]+)'
    url_pattern = r'url = ([^,]+)'
    justify_pattern = r'justify = (.+)'
    name_match = re.search(name_pattern, input_string)
    url_match = re.search(url_pattern, input_string)
    analysis_match = re.search(justify_pattern, input_string)
    if name_match and url_match and analysis_match:
        name = name_match.group(1)
        url = url_match.group(1)
        analysis = analysis_match.group(1)
        return name, url, analysis
    else:
        return render_template("index.html", error="Some Internal Error Occurred.\n Please try again.")

def cleanAnalysys(input_text):
    # Find the position of the first opening parenthesis
    start_pos = input_text.find('(')
    end_pos = input_text.find(')')
    # If an opening parenthesis is found, extract the substring up to that position
    if start_pos != -1:
        output_text = input_text[:start_pos].strip()
        output_text += " "+input_text[end_pos+1:].strip()
    else:
        output_text = input_text
    return output_text

@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_repository():
    
    # Handle the repository analysis request
    user_url = request.form.get("username")
    # user_url = extract_url(user_url)
    username = user_url.split("/")[-1] if user_url else None
    if username:
        repos = get_user_repositories(username)
        if repos is not None:
            analysis = find_complex(repos)
            analysis = cleanAnalysys(analysis)
            name, url, analysis = nameRepoData(analysis)
            if name and url and analysis:
                return render_template("index.html", result=name, repo_url=url, analysis=analysis)
        else:
            return render_template("index.html", error="Failed to fetch repositories.")
    else:
        return render_template("index.html", error="Invalid GitHub User.")


if __name__ == "__main__":
    app.run(debug=True,host="127.0.0.1",port=5000,threaded=True)
