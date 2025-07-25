# 🐍 Insecure Python App (Training Repository)

This repository contains an **intentionally insecure Python Flask application** created for training and assessment purposes. It's designed to help junior cybersecurity analysts and DevSecOps practitioners practice identifying and understanding common security flaws in application code.

> ⚠️ **Warning:** This app is insecure by design. **Do not deploy in production environments.**

## 🛠 Purpose
This project is designed to:

* Provide a sandbox for secure code review practice
* Explore insecure coding patterns
* Simulate basic web application vulnerabilities
* Evaluate junior cybersecurity capabilities

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hima-devsecops/insecure-python-app.git
cd insecure-python-app
```
### 2. Set Up a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3.  Install Dependencies
`pip install -r requirements.txt`  

## 🚀 Running the Application
Start the app using:  
`python app/app.py`

Once running, open your browser to:  
`http://127.0.0.1:5000`

## 📖 Usage Example
The application exposes a simple endpoint that accepts a `name` parameter via a GET request.

You can test it by opening a browser or using curl:

```bash
curl "http://127.0.0.1:5000/?name=YourName"
```

Replace `YourName` with any string. The app will respond with a JSON message greeting the provided name.

Example response:
```
{
  "message": "Hello YourName 👋, welcome to our insecure web application!"
}
```

## 🎯 What You Should Do
You are encouraged to:
* Review the source code for common security issues
* Document and explain your findings
* Suggest code or configuration improvements
* Optionally, run static or dynamic analysis tools
* Think from both a defender and attacker perspective

💡 This exercise is open-ended. There's no single correct approach — your observations matter most.

## ❗Important Notes
* This project is intended only for local use in controlled environments
* Do not expose this app to the internet
* Treat this as an educational challenge — avoid modifying the code before reviewing it

