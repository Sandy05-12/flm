import smtplib
from email.message import EmailMessage
import logging
# Configure logging
logging.basicConfig(level=logging.DEBUG)
def sendmail(to,subject,body):
    try:
    # Send email
        server=smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('p.sandhya32p@gmail.com','skqg qubx vxfj pbuv')
        msg=EmailMessage()
        msg['From']='p.sandhya32p@gmail.com'
        msg['To']=to
        msg['Subject']=subject
        msg.set_content(body)
        server.send_message(msg)
        server.quit()
        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error("Error sending email:", e)
    