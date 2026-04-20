# AiTM CTF – Stolen Session

## Challenge Name
Stolen Session: AiTM Session Hijacking

## Type
Web / Application Security

---

## Description

This challenge simulates an Adversary-in-the-Middle (AiTM) attack.

In real AiTM attacks, attackers intercept authentication traffic and steal session tokens after a user logs in. These tokens can then be reused to access accounts without needing to re-authenticate.

In this lab, you will interact with a fake login page, capture a session token, and use it to access a protected resource.

---

## Objective

Log into the system, identify the session token, and use it to access a restricted endpoint to retrieve the flag.

---

## Setup Instructions

0. Download the full zip containing the Static folder, README.md, and app.p

1. Open terminal, navigate to the folder, and make sure Python is installed

       python --version

3. Install Flask in the folder:

       pip install flask

4. Run the server:

       python app.py

5. After running the server, you should see a message like:

       Running on http://127.0.0.1:5000

6. Open your browser and go to:

       http://localhost:5000

7. You should now see the login page

---

## How to Solve


Log into the application and analyze how authentication is handled. Identify any session-related data that may grant access to protected resources.

Use this information to access the restricted endpoint and retrieve the flag.

---

## Flag Format

Example:

`flag{3f2a9c1e-8b21-4c7a-9e2a-123456789abc}`

---

## Hints

**Hint 1:**  
The flag is not on the dashboard. There may be an admin-related endpoint worth exploring. Experiment with changing the URL.

**Hint 2:**  
Authentication often relies on tokens. Look for session-related data in your browser and consider how it might be reused. /admin?token= ...

---

## How This Relates to AiTM

This challenge demonstrates the core concept behind Adversary-in-the-Middle (AiTM) attacks: session token theft and reuse.

Instead of only stealing credentials, attackers capture session cookies after authentication. These cookies allow them to access accounts without triggering multi-factor authentication again.

In this challenge:

- The login simulates credential capture
- The session cookie represents the stolen authentication token
- The `/admin` endpoint simulates unauthorized access using a hijacked session

This mirrors real-world AiTM attacks where attackers bypass MFA by reusing valid session tokens.

---

## Author

Jack McAffee
