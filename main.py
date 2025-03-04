import re
import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

# Sample phishing and legitimate email dataset (replace with actual dataset)
data = {
    "email_text": [
        "Your account has been compromised, please reset your password immediately using this link.",
        "Congratulations! You have won a lottery of $1,000,000. Click here to claim.",
        "Dear user, your bank has detected suspicious activity. Click the link below to verify your identity.",
        "Hello, please find the attached document as per our discussion.",
        "Reminder: Your payment is due next week. Visit your dashboard for details."
    ],
    "label": [1, 1, 1, 0, 0]  # 1 = Phishing, 0 = Legitimate
}

# Load dataset into DataFrame
df = pd.DataFrame(data)

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['email_text'])
y = df['label']

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model and vectorizer for real-time usage
joblib.dump(model, "phishing_detector.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

# Educational component
def phishing_alert(email_text):
    model = joblib.load("phishing_detector.pkl")
    vectorizer = joblib.load("vectorizer.pkl")

    email_vectorized = vectorizer.transform([email_text])
    prediction = model.predict(email_vectorized)[0]

    if prediction == 1:
        print("\n⚠ **Warning: Potential Phishing Email Detected!** ⚠")
        print(" **Security Tips:**")
        print("   - Do not click on suspicious links.")
        print("   - Verify sender details before responding.")
        print("   - Never share personal or financial information via email.")
        print("   - Report phishing emails to IT security.")
    else:
        print("\n This email appears to be legitimate.")

# Test real-time detection
test_email = input("\n Enter an email text to analyze: ")
phishing_alert(test_email)
