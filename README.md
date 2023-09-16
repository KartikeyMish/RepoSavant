# RepoSavant 🕵️‍♂️🔍💻

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/kartikeymish/RepoSavant/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/kartikeymish/RepoSavant.svg)](https://github.com/kartikeymish/RepoSavant/issues)
<a href="https://reposavant.onrender.com">
        <img alt="website" src="https://img.shields.io/website/http/huggingface.co/docs/transformers/index.svg?down_color=red&down_message=offline&up_message=online">
</a>
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

## 🛠️ Configuration

To use RepoSavant effectively, you need to configure your OpenAI API key and GitHub token. Here's how:

1. **OpenAI API Key:**
   - Go to the [OpenAI](https://platform.openai.com/account/api-keys) website and sign in or create an account if you don't have one.
   - Navigate to the API section to obtain your API key. Keep it secure and never share it publicly.

2. **GitHub Token:**
   - Go to your GitHub account settings and navigate to "Developer settings" > "Personal access tokens."
   - Generate a new token with the necessary permissions (e.g., `repo`, `user`, `read:org`) for RepoSavant.
   - Ensure you keep this token secure and do not expose it in public repositories.

3. **Create a `.env` file:**
   - In the root directory of your RepoSavant project, create a `.env` file if it doesn't already exist.
   - Add your OpenAI API key and GitHub token to the `.env` file as follows:
   <br>
   
    ```.env[]
    OPENAI_API_KEY=your_openai_api_key_here
    GITHUB_TOKEN=your_github_token_here
    ```
4. **Save and Secure:**
- Save the `.env` file.
- Ensure that you keep this file private and do not include it in your version control system (e.g., Git). Add it to your `.gitignore` if needed.

With these configurations in place, RepoSavant will be able to access the necessary APIs securely for its functionality.

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

## 🚀 Upcoming Features

We're committed to making RepoSavant even better! Here's a sneak peek at some of the exciting features and improvements we have in the pipeline:

- [x] **Improved User Interface:** We're working on a more responsive and user-friendly UI that will enhance the RepoSavant experience for all users. Whether you're accessing it from your desktop or mobile device, you can expect a seamless and intuitive interface.

- [ ] **Loading Animation:** We understand that waiting for repository analysis results can be a bit nerve-wracking. That's why we'll adding a sleek loading animation to keep you informed and entertained while RepoSavant does its magic behind the scenes.

- [ ] **Top 3**: Quickly assess your top three most complex repositories instead of just one. Gain a deeper understanding for honing your skills effectively.

- [ ] **Plagiarism Checker:** Worried about code uniqueness? RepoSavant will be stepping up its game with a plagiarism checker. This feature will help you identify any similarities between your code and other repositories, ensuring the integrity of your work.

- [ ] **Batch Processing:** We know you're busy, so we'll be introducing the ability to input multiple GitHub URLs for batch processing. Analyze several profiles or repositories in one go, saving you time and effort.


Stay tuned for these updates and more as we continue to evolve RepoSavant to meet your needs! Your feedback and suggestions are always welcome as we work towards a smarter GitHub experience. 🌟


## 🙌 Current Contributors

A big thank you to the talented individuals who have contributed to RepoSavant. Your dedication and expertise are invaluable to the project's success. 

- [Kartikey Mishra](https://github.com/kartikeymish) :  Complete Backend & basic frontend 
- [Suryansh Singh](https://github.com/suryanshsingh2001) : Refactoring, Responsive Design, and CSS Improvement

If you'd like to join this list and make RepoSavant even better.

Your contributions are highly appreciated! 🌟

## ❤️ Sponsor Us

RepoSavant relies on OpenAI's powerful API, and credits are limited. By sponsoring this project, you help maintain and improve this tool for the entire GitHub community. Please consider sponsoring us [here](https://github.com/sponsors/KartikeyMish).

Thank you for your support! 🙏

---

**Note:** This project is not affiliated with GitHub or OpenAI.

