from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

UNSUB_FILE = 'unsubscribed.txt'

@app.route('/')
def home():
    return "<h3>✅ Flask App is Running</h3>"

@app.route('/unsubscribe')
def unsubscribe():
    email = request.args.get('email', '').strip().lower()
    if email:
        with open(UNSUB_FILE, 'a') as f:
            f.write(email + '\n')
        return render_template_string("""
            <h2>You've been unsubscribed 😢</h2>
            <p>{{ email }} will no longer receive emails from us.</p>
        """, email=email)
    return "Invalid email."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
