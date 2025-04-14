import pandas as pd
import tkinter as tk
from tkinter import messagebox
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# -------------------------
# STEP 1: Load and preprocess the dataset
# -------------------------
try:
    df = pd.read_csv("Phishing_Email.csv").dropna()
except FileNotFoundError:
    print("❌ ERROR: 'Phishing_Email.csv' not found in the directory.")
    exit()

df = df[df['Email Type'].isin(["Safe Email", "Phishing Email"])]  # Clean only valid labels

X = df["Email Text"]
y = df["Email Type"]

# -------------------------
# STEP 2: Vectorize and train model
# -------------------------
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

model = RandomForestClassifier(n_estimators=10)
model.fit(X_vect, y)

# -------------------------
# STEP 3: GUI logic
# -------------------------
def analyze_email():
    email_text = entry.get("1.0", tk.END).strip()
    if not email_text:
        messagebox.showinfo("Input Required", "Please enter email text to analyze.")
        return

    email_vect = vectorizer.transform([email_text])
    prediction = model.predict(email_vect)[0]

    if prediction == "Phishing Email":
        messagebox.showwarning(
            "⚠️ Warning: Phishing Email Detected",
            "⚠ This looks like a phishing email!\n\n💡 Tips:\n"
            "- Do NOT click suspicious links\n"
            "- Verify the sender\n"
            "- Report to IT/security team"
        )
    else:
        messagebox.showinfo("✅ Safe Email", "This email appears to be safe.")

# -------------------------
# STEP 4: GUI layout
# -------------------------
root = tk.Tk()
root.title("Phishing Email Detector")
root.geometry("650x450")

label = tk.Label(root, text="Enter email content below:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Text(root, height=12, width=70, font=("Courier New", 10))
entry.pack(pady=10)

btn = tk.Button(root, text="Analyze Email", font=("Arial", 11, "bold"), bg="#4CAF50", fg="white", command=analyze_email)
btn.pack(pady=10)

root.mainloop()
