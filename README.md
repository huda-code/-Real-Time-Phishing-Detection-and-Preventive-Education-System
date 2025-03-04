# -Real-Time-Phishing-Detection-and-Preventive-Education-System


Hajira Sultana
Lewis University
Romeoville, IL 60446
Title: Real-Time Phishing Detection and Preventive Education System
Abstract:
Phishing attacks trick people into revealing sensitive information like passwords and financial details,
leading to major security risks. Many users fall victim to these scams because they don’t know how
to recognize them or don’t have tools to detect them. This project introduces a Real-Time Phishing
Detection and Preventive Education System, which helps users identify phishing threats
instantly while teaching them how to avoid future attacks. The system will use smart technology
to scan emails, links, and messages for suspicious signs and provide immediate alerts. Additionally,
an interactive learning feature will guide users through real-world phishing scenarios, helping
them build skills to recognize scams before they become victims. By combining real-time security
with preventive education, this system aims to strengthen cybersecurity awareness and reduce
phishing-related risks. This research provides a practical solution for staying safe online in an
increasingly digital world

How This Works:
The script trains a Naïve Bayes classifier on a small dataset of phishing and legitimate emails.
It saves the trained model and vectorizer using joblib for real-time usage.
The phishing_alert() function:
Loads the trained model.
Processes the email input.
Detects whether it's phishing or legitimate.
If phishing is detected, it provides security tips for user education.
Next Steps to Improve This Model:
✅ Use a larger dataset for improved accuracy.
✅ Integrate with email scanning services (IMAP/SMTP APIs) for real-time analysis.
✅ Add URL inspection for suspicious links using re (regex).
✅ Implement machine learning enhancements (e.g., deep learning with LSTMs for textual analysis).
