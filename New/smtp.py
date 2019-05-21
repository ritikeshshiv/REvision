import smtplib

smtpUser='1997gour@gmail.com'
smtpPass='Naitik@19'

toAdd='nsg1909@gmail.com'
fromAdd=smtpUser

subject='Raspberry pi Notification'
header='To: '+toAdd+'\n'+'From: '+fromAdd+'\n'+'Subject: '+subject
body='Hello world'

print(header+'\n'+body)
s=smtplib.SMTP('smtp.gmail.com',587)

s.ehlo()
s.starttls()
s.ehlo()

s.login(smtpUser,smtpPass)
s.sendmail(fromAdd,toAdd,header+body)
s.quit()
