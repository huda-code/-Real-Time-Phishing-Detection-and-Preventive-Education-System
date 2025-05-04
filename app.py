import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import gradio as gr

# Load and preprocess the dataset
df = pd.read_csv("Phishing_Email.csv").dropna()
df = df[df['Email Type'].isin(["Safe Email", "Phishing Email"])]
X = df["Email Text"]
y = df["Email Type"]

vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

model = RandomForestClassifier(n_estimators=10)
model.fit(X_vect, y)

# Inference function
def predict(email_text):
    vect = vectorizer.transform([email_text])
    pred = model.predict(vect)[0]

    phishing_clues = []

    # Rule-based clues
    if "verify" in email_text.lower():
        phishing_clues.append("Uses the word 'verify'")
    if "click here" in email_text.lower() or "http" in email_text.lower():
        phishing_clues.append("Contains suspicious links")
    if "password" in email_text.lower():
        phishing_clues.append("Mentions 'password'")
    if "gift card" in email_text.lower() or "$" in email_text:
        phishing_clues.append("Mentions money or rewards")
    if "suspended" in email_text.lower() or "locked" in email_text.lower():
        phishing_clues.append("Threatens account access")

    if pred == "Phishing Email":
        reason = "\n• " + "\n• ".join(phishing_clues) if phishing_clues else "\n• Suspicious language or pattern detected"
        return f"⚠️ This looks like a phishing email!\n\nWhy:\n{reason}"
    else:
        return "✅ This email appears to be safe."


# Gradio interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(lines=10, placeholder="Paste your email here..."),
    outputs="text",
    title="Phishing Email Detector",
    description="Detect phishing emails in real-time using a trained machine learning model."
)

demo.launch()
