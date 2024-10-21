# app.py

from flask import Flask, render_template, request, redirect, flash
from email_sender import send_email

app = Flask(__name__)
app.secret_key = "uavm makp crhl fblh"  # Required for flashing messages

# Route to render the HTML form
@app.route('/')
def index():
    return render_template('send_email.html')

# Route to handle the email sending logic
@app.route('/send', methods=['POST'])
def send():
    to_address = request.form['to']
    subject = request.form['subject']
    message_body = request.form['message']

    # Call the send_email function to send the email
    feedback = send_email(to_address, subject, message_body)

    # Flash feedback to the user (success or failure message)
    flash(feedback)

    # Redirect back to the form page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
