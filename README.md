# RepoSavant 🕵️‍♂️🔍💻

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/kartikeymish/RepoSavant/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/kartikeymish/RepoSavant.svg)](https://github.com/kartikeymish/RepoSavant/issues)
<!--[![GitHub Stars](https://img.shields.io/github/stars/kartikeymish/RepoSavant.svg)](https://github.com/kartikeymish/RepoSavant/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/kartikeymish/RepoSavant.svg)](https://github.com/kartikeymish/RepoSavant/issues)-->

RepoSavant is an innovative Python-based utility designed to elevate your GitHub experience. By simply inputting a GitHub user's URL, RepoSavant excels at pinpointing the epitome of technical complexity within their repository portfolio. 🕵️‍♂️ Harnessing the power of cutting-edge technologies, including GPT and LangChain, the tool conducts a meticulous assessment of each repository, culminating in the identification of the most technically challenging gem. 💎

## 🌟 Why Use RepoSavant?

- 🤓 **For Developers:** Quickly identify the most complex repository in your GitHub profile and focus on improving your skills and projects.
- 🕵️‍♀️ **For Recruiters:** Access candidates' most complex projects to gain insights into their technical expertise and best work.
- 📈 **For Managers:** Evaluate your team's technical prowess by analyzing their GitHub repositories.

## 🧐 How It Works

### Backend Process

1. **Data Extraction:** RepoSavant uses the GitHub API to fetch JSON data of users' repositories.
2. **Data Processing:** Important features such as description, contributors, size, language, topics, stars, forks, labels, and issues are extracted to determine repository complexity. Unstarred forks are excluded.
3. **Data Analysis:** The data is then sent to GPT-3.5 Turbo LLM via LangChain with a subtle and accurate prompt to extract the most complex repository based on all the features. It also provides an analysis of why the selected repository is the most complex.

### Frontend

- Flask is used for the frontend, maintaining a GitHub theme to provide a seamless user experience.

## 📦 Project Dockerization

To run RepoSavant in a Docker container, follow these steps:

1. Clone this repository.
2. Build the Docker image:
```bash[]
docker build -t reposavant .
```
3. Run the Docker container:
```bash[]
docker run -d -p 5000:5000 reposavant
```

## 🏃‍♂️ Getting Started

1. Clone this repository.
2. Install the required dependencies:
```bash[]
pip install -r requirements.txt
```
3. Run the Flask app:
```bash[]
python app.py
``` 
 4. Open your browser and navigate to `http://localhost:5000`.

## 💪 Contributing

We welcome contributions from the community! If you'd like to contribute to RepoSavant.

## ❤️ Sponsor Us

RepoSavant relies on OpenAI's powerful API, and credits are limited. By sponsoring this project, you help maintain and improve this tool for the entire GitHub community. Please consider sponsoring us [here](https://github.com/sponsors/KartikeyMish).

Thank you for your support! 🙏

---

**Note:** This project is not affiliated with GitHub or OpenAI.

