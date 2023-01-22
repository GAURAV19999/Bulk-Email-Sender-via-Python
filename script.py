import pandas as pd
import smtplib

SenderAddress = "xxxx@.com"
password = "jvvqqdohcpewegwm"

e = pd.read_excel("test.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SenderAddress, password)
greeting = "Dear Alumni,"
msg="""Hello, How are doing today!"""
#link=" Your feedback is highly appreciated and will deinitely help us to improve. Please fill the feedback from the link \n https://forms.gle/pUfDbaTyRbbyKXaQ7"
end="We hope to see you next time."
regards="""Gaurav Kr Vishwakarma"""
name="FRAMES Association"
subject = "XXXX"
body = "Subject: {}\n\n{}\n\n{}\n\n{}\n\n{}\n{}".format(subject,greeting,msg,end,regards,name)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()

print("All MAIL SENT")