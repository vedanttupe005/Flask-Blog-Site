from flask import Flask, render_template,request
import requests
import time
import smtplib
from email.message import EmailMessage

posts = requests.get("https://api.npoint.io/a7020bc84c3ce3dd2532").json()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(template_name_or_list="index.html", post_data = posts)



@app.route('/About')
def about():
    return render_template("about.html")



@app.route('/Contact')
def contact():
    return render_template("contact.html")



@app.route("/post")
def post():
    keyword = request.args.get('data_id')
    print(keyword)
    if keyword:
        for i in posts:
            if i["id"]==int(keyword):
                return render_template(template_name_or_list="post.html",  data = i)
    time.sleep(3)
    return render_template(template_name_or_list="post.html", data = posts[0])


@app.route("/data-entry", methods =['post'])
def recieve_dat():
    # Email content
    name = request.form.get('name')
    email_address = request.form.get('sednder_email')
    phone_no = request.form.get('phone_no')
    feedback = request.form.get('feedback')
    msg = EmailMessage()
    msg['Subject'] = 'Blog Feedbak'
    msg['Name'] = name
    msg['From'] = email_address
    msg['To'] = 'vedanttupe005@gmail.com'
    msg['Phone No.'] = phone_no
    msg.set_content(feedback)

    # Gmail SMTP server settings
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Your Gmail credentials
    sender_email = 'vedanttupe005@gmail.com'
    sender_password = 'bare oega zoxo yurk'  # Use App Password, NOT your Gmail password

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print("Email sent successfully!")
            return "<h1>your email has been sended successfully</h1>"
    except Exception as e:
        print("Error sending email:", e)
        return "<h1>something wnr wrong we cant send your email</h1>"

@app.route("/connectivity")
def social_media():
    return "<h3>We don't have Twiter or FackBook page however you can send us feedback mail form Contact section on navbar or you can visit my github profile</h3>"

if __name__ == '__main__':
    app.run(debug=True)