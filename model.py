import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import re
import os

print("=" * 50)
print("🤖 Training Scam Detection Model")
print("=" * 50)

# Check if dataset exists
if not os.path.exists('sms_spam.csv'):
    print("❌ Error: sms_spam.csv not found!")
    print("📝 Please run: python dataset.py first")
    exit(1)

# Load dataset
print("📂 Loading dataset...")
data = pd.read_csv('sms_spam.csv', sep='\t', header=None)
data.columns = ['label', 'text']
print(f"✅ Loaded {len(data)} messages")

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

data['cleaned_text'] = data['text'].apply(clean_text)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Train model
print("🔄 Training model...")
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['cleaned_text'])
y = data['label']

model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X, y)

# Save model
print("💾 Saving model...")
with open('model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print("✅ Model trained and saved as 'model.pkl'")
print(f"📊 Accuracy: {model.score(X, y)*100:.1f}%")
print("=" * 50)