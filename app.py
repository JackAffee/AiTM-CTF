from flask import Flask, request, redirect, make_response
import uuid

app = Flask(__name__)

sessions = {}

@app.route('/')
def login():
    return '''
    <html>
    <head>
        <title>LeBron Secure Login</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                background: #552583;
                color: white;
                padding: 30px;
            }
            img {
                width: 250px;
                max-width: 90%;
                border-radius: 12px;
                margin: 20px 0;
                box-shadow: 0 8px 18px rgba(0,0,0,0.35);
            }
            input {
                margin: 6px;
                padding: 10px;
                border-radius: 8px;
                border: none;
            }
            .btn {
                background: #FDB927;
                color: #552583;
                font-weight: bold;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>👑 LeBron Secure Login 👑</h1>
        <img src="/static/lebron_login.jpg" alt="LeBron Login">
        <form method="POST" action="/login">
            Email: <input name="email"><br>
            Password: <input name="password" type="password"><br>
            <input class="btn" type="submit" value="Enter the League">
        </form>
    </body>
    </html>
    '''

@app.route('/login', methods=['POST'])
def capture():
    email = request.form.get('email')
    password = request.form.get('password')

    print("Captured creds:", email, password)

    session_token = str(uuid.uuid4())
    sessions[session_token] = email

    print("Stolen session token:", session_token)
    print(f"[ATTACKER] Stolen session cookie: {session_token}")

    response = make_response(redirect("/dashboard"))
    response.set_cookie("session", session_token)

    return response

@app.route('/dashboard')
def dashboard():
    return '''
    <html>
    <head>
        <title>LeBron Dashboard</title>
        <style>
            body {
                text-align: center;
                font-family: Arial, sans-serif;
                background: #1d428a;
                color: white;
                padding: 30px;
            }
            img {
                width: 300px;
                max-width: 90%;
                border-radius: 12px;
                margin: 20px 0;
                box-shadow: 0 8px 18px rgba(0,0,0,0.35);
            }
        </style>
    </head>
    <body>
        <h2>🏀 Login Successful 🏀</h2>
        <p>You made it to the league... but this is not the finals yet.</p>
        <img src="/static/lebron_dashboard.jpg" alt="LeBron Dashboard">
        <p>Nothing interesting here...</p>
        <!-- TODO: restrict admin panel -->
    </body>
    </html>
    '''

@app.route('/admin')
def admin():
    token = request.args.get("token")

    if token in sessions:
        flag = "itc266{Lebron_is_my_sunshine}"
        return f"""
        <html>
        <head>
            <title>LeBron Admin Access</title>
            <style>
                body {{
                    margin: 0;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #552583, #FDB927);
                    color: white;
                    text-align: center;
                    padding: 40px;
                }}
                .container {{
                    max-width: 900px;
                    margin: auto;
                    background: rgba(0, 0, 0, 0.35);
                    border-radius: 20px;
                    padding: 30px;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
                }}
                h1 {{
                    font-size: 3rem;
                    margin-bottom: 10px;
                }}
                h2 {{
                    font-size: 2rem;
                    color: #FDB927;
                }}
                img {{
                    width: 320px;
                    max-width: 90%;
                    border-radius: 16px;
                    margin: 25px 0;
                    box-shadow: 0 8px 20px rgba(0,0,0,0.4);
                }}
                .flag {{
                    font-size: 1.4rem;
                    font-weight: bold;
                    background: white;
                    color: #552583;
                    display: inline-block;
                    padding: 15px 20px;
                    border-radius: 12px;
                    margin-top: 20px;
                    word-break: break-word;
                }}
                .sub {{
                    font-size: 1.2rem;
                    margin-top: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>👑 LeBron Admin Access Granted 👑</h1>
                <h2>Welcome {sessions[token]}</h2>
                <p class="sub">You just took over the session like the King taking over the game.</p>
                <img src="/static/lebron.jpg" alt="LeBron themed admin page">
                <p class="sub">Championship-level session hijack complete.</p>
                <div class="flag">Flag: {flag}</div>
            </div>
        </body>
        </html>
        """
    else:
        return "Access denied"

app.run(host='0.0.0.0', port=5000)
