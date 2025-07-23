from flask import Flask, request, render_template_string

app = Flask(__name__)

UNSUB_FILE = 'unsubscribed.txt'

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
