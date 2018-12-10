
# send email with python script


import smtplib

# write the body of message

content ='This is test mail generated from python script'

#body with content sender and reciever

body='\r\n'.join(['To: %s'%'reciever_mail_id ',
                  'From: %s'%'sender_mail_id',
                  'Subject: %s'%'Script generated e-mail',content])


#port 587

mail = smtplib.SMTP('smtp.gmail.com', 587)

#start session

mail.starttls()

#enter ur credentials
mail.login('username','password')

try:
   mail.sendmail('sender_email_id','reciever_email_id  ',content)
   print ('mail sent successfully')
except:
   print('error occured')


mail.close()


'''when u run this code, at first time u will get some errors for 'critical security alert'. u have to turn on the 
less secure settings on ur google account''' 
  

