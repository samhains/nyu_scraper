"""The first step is to create an SMTP object, each object is used for connection
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("sdhains2", "")

#Send the mail
msg = "HEY"
mwsg = "\r\n".join([
  "From: sdhains2@gmail.com",
  "To: sam@samhains.com",
  "Subject: WAITLIST",
  "",
  "Why, oh why"
  ])
server.sendmail("sdhains2@gmail.com", "sam@samhains.com", msg)
