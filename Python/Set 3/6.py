import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('celndaph@gmail.com','password')
server.sendmail('celndaph@gmail.com', 'daph97babu@gmail.com', 'Hello!, How are you?')
server.quit()