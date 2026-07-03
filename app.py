from flask import Flask, request, jsonify
import pickle
import re
import os

app = Flask(__name__)

print("=" * 50)
print("🚀 Starting Scam Checker Application...")
print("=" * 50)

# Check if model exists
if not os.path.exists('model.pkl'):
    print("❌ ERROR: model.pkl not found!")
    print("📝 Please run: python model.py first")
    exit(1)

# Load model
print("📂 Loading model...")
try:
    with open('model.pkl', 'rb') as f:
        model, vectorizer = pickle.load(f)
    print("✅ Model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    exit(1)

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Simple HTML page
@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🔍 Scam Checker</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 0;
                padding: 20px;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 20px;
                max-width: 500px;
                width: 100%;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            }
            h1 {
                text-align: center;
                color: #333;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
            }
            textarea {
                width: 100%;
                padding: 15px;
                border: 2px solid #ddd;
                border-radius: 10px;
                font-size: 16px;
                min-height: 120px;
                box-sizing: border-box;
                font-family: Arial;
            }
            textarea:focus {
                outline: none;
                border-color: #667eea;
            }
            button {
                width: 100%;
                padding: 15px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                margin-top: 15px;
            }
            button:hover {
                transform: scale(1.02);
            }
            button:disabled {
                opacity: 0.6;
                cursor: not-allowed;
            }
            #result {
                margin-top: 20px;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                font-weight: bold;
                display: none;
            }
            #result.show {
                display: block;
            }
            #result.scam {
                background: #f8d7da;
                color: #721c24;
                border: 2px solid #f5c6cb;
            }
            #result.safe {
                background: #d4edda;
                color: #155724;
                border: 2px solid #c3e6cb;
            }
            #result.loading {
                background: #e7f3ff;
                color: #004085;
                border: 2px solid #b8d4f0;
            }
            .confidence {
                font-size: 14px;
                font-weight: normal;
                margin-top: 5px;
                opacity: 0.8;
            }
            .features {
                display: flex;
                justify-content: space-around;
                margin-top: 25px;
                color: #666;
                font-size: 14px;
            }
            .error {
                color: red;
                padding: 10px;
                background: #ffebee;
                border-radius: 5px;
                margin-top: 10px;
                display: none;
            }
            .error.show {
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔍 Scam Checker</h1>
            <p class="subtitle">AI-powered SMS and message scam detection</p>
            
            <textarea id="message" placeholder="Paste suspicious message, SMS, or text here..."></textarea>
            <button id="checkBtn">🔍 Check for Scam</button>
            
            <div id="result"></div>
            <div id="error" class="error"></div>
            
            <div class="features">
                <span>🤖 AI Powered</span>
                <span>⚡ Real-time</span>
                <span>🔒 100% Free</span>
            </div>
        </div>

        <script>
            document.getElementById('checkBtn').addEventListener('click', function() {
                const message = document.getElementById('message').value.trim();
                const result = document.getElementById('result');
                const error = document.getElementById('error');
                const btn = this;
                
                result.className = '';
                result.style.display = 'none';
                error.className = 'error';
                error.style.display = 'none';
                
                if (!message) {
                    error.textContent = '⚠️ Please enter some text to check!';
                    error.className = 'error show';
                    return;
                }
                
                result.textContent = '⏳ Analyzing your message...';
                result.className = 'show loading';
                result.style.display = 'block';
                btn.disabled = true;
                btn.textContent = '⏳ Analyzing...';
                
                fetch('/check', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'text=' + encodeURIComponent(message)
                })
                .then(response => response.json())
                .then(data => {
                    btn.disabled = false;
                    btn.textContent = '🔍 Check for Scam';
                    
                    if (data.error) {
                        error.textContent = '❌ ' + data.error;
                        error.className = 'error show';
                        result.style.display = 'none';
                        return;
                    }
                    
                    const confidence = Math.round(data.confidence * 100);
                    result.innerHTML = data.message + '<br><div class="confidence">Confidence: ' + confidence + '%</div>';
                    result.className = 'show ' + (data.is_scam ? 'scam' : 'safe');
                    result.style.display = 'block';
                })
                .catch(error => {
                    btn.disabled = false;
                    btn.textContent = '🔍 Check for Scam';
                    error.textContent = '❌ Error: ' + error.message + '. Make sure the server is running!';
                    error.className = 'error show';
                    result.style.display = 'none';
                    console.error('Error:', error);
                });
            });
        </script>
    </body>
    </html>
    '''

@app.route('/check', methods=['POST'])
def check_scam():
    try:
        text = request.form.get('text', '')
        
        if not text or len(text.strip()) == 0:
            return jsonify({'error': 'Please enter some text to check'})
        
        cleaned = clean_text(text)
        vectorized = vectorizer.transform([cleaned])
        
        prediction = model.predict(vectorized)[0]
        confidence = model.predict_proba(vectorized)[0]
        
        return jsonify({
            'is_scam': bool(prediction),
            'confidence': float(max(confidence)),
            'message': '⚠️ SCAM DETECTED!' if prediction == 1 else '✅ Seems safe!'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print("=" * 50)
    print("✅ Application is ready!")
    print("🌐 Open: http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)