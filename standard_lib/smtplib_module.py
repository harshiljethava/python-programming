import os
import smtplib
from urllib.request import urlopen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase

server_smtp=smtplib.SMTP('SMTP_EMAIL_ADDRESS',587)

login="YOUR_EMAIL_ADDRESS"
password="EMAIL_PASSWORD"
try:
	fromaddr = "FROM_EMAIL_ADDRESS"
	toaddr = "TO_EMAIL_ADDRESS"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SUBJECT_NAME"
	link = "LINK_FOR_ATTACHMENT"
	link_res=urlopen(link)
	link_file=link_res
	filename = "FILENAME_WITH_EXTENSION"
	attachment = link_file
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part)
 
	body="MESSAGE_BODY"
	msg.attach(MIMEText(body, 'plain'))
	server_smtp.login(login,password)	
	text=msg.as_string()
	server_smtp.sendmail(fromaddr,toaddr,text)
	server_smtp.quit()
except Exception as e:
	raise
	print("Error ! Mail not sent ",e)
else:
	pass
finally:
	pass
	print("\n\nSuccessfully mail sent !")



