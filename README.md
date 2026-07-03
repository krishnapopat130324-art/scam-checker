# 🔍 AI Scam Checker

### *AI-Powered Scam Message Detection using Machine Learning*

An intelligent web application that detects scam messages, phishing SMS, and suspicious text content using Machine Learning and Natural Language Processing techniques.

---

## ✨ Features

| Feature                     | Description                                                  |
| --------------------------- | ------------------------------------------------------------ |
| 🤖 **AI-Powered Detection** | Uses Machine Learning to identify scam and phishing messages |
| ⚡ **Real-Time Analysis**    | Instant predictions with confidence scores                   |
| 📊 **Confidence Scores**    | Displays prediction certainty percentage                     |
| 🌐 **Modern Web Interface** | Responsive and user-friendly design                          |
| 🔌 **REST API Support**     | Easy integration with other applications                     |
| 🔒 **Open Source**          | Completely free and transparent                              |

---

## 🎯 How It Works

1. User enters a suspicious message.
2. Text is cleaned and preprocessed.
3. TF-IDF converts text into numerical features.
4. The Logistic Regression model analyzes the message.
5. The system returns:

   * Scam or Safe prediction
   * Confidence score
   * Risk indication

---

## 🛠️ Tech Stack

### Backend

* Python 3.8+
* Flask
* Scikit-learn
* Pandas
* Pickle

### Frontend

* HTML5
* CSS3
* JavaScript

### Machine Learning

* Logistic Regression
* TF-IDF Vectorizer
* NLP Preprocessing

---

## 📦 Installation

### Clone Repository

```bash
git clone <repository-url>
cd scam-checker
```

### Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python dataset.py
python model.py
```

### Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

## 🚀 Usage

1. Paste a suspicious message.
2. Click **Check for Scam**.
3. Review prediction results and confidence score.

### Example Predictions

| Message                            | Result           |
| ---------------------------------- | ---------------- |
| FREE MONEY! Claim your prize now!  | ⚠️ Scam Detected |
| Your account has been compromised. | ⚠️ Scam Detected |
| Are you coming for dinner tonight? | ✅ Safe           |
| I will arrive in 10 minutes.       | ✅ Safe           |

---

## 📊 Dataset

The application uses the **SMS Spam Collection Dataset** containing **5,574 labeled SMS messages**.

* **Ham** → Legitimate messages
* **Spam** → Scam or fraudulent messages

---

## 📈 Model Performance

| Metric    | Score               |
| --------- | ------------------- |
| Accuracy  | ~98%                |
| Precision | ~96%                |
| Recall    | ~95%                |
| Algorithm | Logistic Regression |
| Features  | TF-IDF              |

---

## 📁 Project Structure

```text
scam-checker/
│
├── app.py                 # Flask application
├── model.py               # ML model training
├── dataset.py             # Dataset processing
├── model.pkl              # Trained model
├── sms_spam.csv           # Dataset
├── requirements.txt       # Dependencies
├── README.md              # Documentation
│
└── templates/
    └── index.html         # Frontend interface
```

---

## 🙏 Acknowledgments

* SMS Spam Collection Dataset
* Flask Community
* Scikit-learn Team
* Open Source Contributors

---

## ⭐ Support

If you find this project useful, consider giving it a **GitHub Star**.

**Made with ❤️ by Krishna Popat**
