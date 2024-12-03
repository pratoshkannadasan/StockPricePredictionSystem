import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert_email(price, threshold, stock_symbol):
    sender_email = "your_email@example.com"
    receiver_email = "receiver_email@example.com"
    password = "your_email_password"

    subject = f"Price Alert: {stock_symbol} reached {price}"
    body = f"The stock price of {stock_symbol} has reached your threshold of {threshold}. Current price: {price}"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        print(f"Alert sent: {stock_symbol} price alert!")
    except Exception as e:
        print(f"Error sending alert: {e}")
