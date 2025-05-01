PCOS We Care: Early risk assessment of Polycystic Ovary Syndrome

🩺 Overview
PCOS We Care is a machine learning-based risk assessment system designed to assist in the early detection of Polycystic Ovary Syndrome (PCOS). By analyzing clinical, biometric, and appearance-based data, the tool provides a preliminary risk evaluation and encourages timely medical consultation. The system is deployed via a web interface to ensure accessibility and ease of use.

🌟 Motivation
- PCOS is a common but often underdiagnosed endocrine disorder affecting up to 13% of women of reproductive age. Traditional diagnosis is invasive and delayed due to vague symptoms. This project aims to:
- Provide a non-invasive screening tool
- Leverage machine learning models for accurate prediction
- Empower women with early health insights

🧠 Features
- Built using Python, Pandas, Scikit-learn, Flask, and Streamlit
- Supports prediction using multiple ML models: Random Forest, Logistic Regression, Naive Bayes, Linear Regression, Gradient Boosting, and MLP
- Uses feature selection techniques (Embedded Random Forest, Mutual Information)
- Trained on a curated Kaggle dataset with 41 medical features
- Web-based form collects basic, non-invasive input
- Maintains user privacy with no data stored

📊 Dataset
Source: https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos
541 records of women with 41 features each
Balanced distribution between PCOS and non-PCOS cases

🚀 Tech Stack
Frontend: HTML/CSS (via Streamlit/Flask UI)
Backend: Python, Scikit-learn
ML Models: Random Forest, Logistic Regression, Naive Bayes, MLP, Gradient Boosting,Linear Regression
Visualization: Matplotlib, Seaborn

👨‍🔬 Team & Acknowledgments
Developed by:
Rishika Chaubal, Anoushka Menon, Hritika Mulay, Sakshi Ganjewar
Special thanks to Dr. Pauras Mhatre, KEM Hospital, Mumbai for clinical insight and guidance.
