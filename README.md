# 📧 Fake Mail Detection

A machine learning web app that detects spam/fake emails using NLP and Logistic Regression.

## 🔗 Live Demo
👉 [Click here to try the app](https://fake-mail-detection-6i7ck4qlyzpjpcgutkfqlb.streamlit.app/)

## 🧠 How it Works
1. User enters email content in the text box
2. TF-IDF Vectorizer converts raw text into numerical features
3. Logistic Regression model predicts Spam or Ham
4. Result is displayed instantly on the screen

## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python | Programming language |
| NLP | Text processing |
| TF-IDF Vectorizer | Convert text to numbers |
| Logistic Regression | Classification model |
| Scikit-learn | ML library |
| Streamlit | Web app deployment |

## 📊 Model Performance
- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF Vectorization
- Classes: Spam / Ham

## 🚀 Run Locally
```bash
git clone https://github.com/LOKESH1027-V/fake-mail-detection
cd fake-mail-detection
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure
```
fake-mail-detection/
├── app.py              # Streamlit web app
├── model.pkl           # Trained Logistic Regression model
├── feature.pkl         # Trained TF-IDF Vectorizer
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```
