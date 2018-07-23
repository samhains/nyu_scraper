import requests

from bs4 import BeautifulSoup
import smtplib
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("sdhains2", "")

def check_nyu():
    url = "https://m.albert.nyu.edu/app/catalog/classsection/NYUNV/1188/22604"

    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all(text="Closed"):
        if link == "Closed":
            msg = "\r\n".join([
                "From: sdhains2@gmail.com",
                "To: sam@samhains.com",
                "Subject: WAITLIST CLOSED",
                "",
                "NEURAL AESTHETIC DOES NOT HAVE SPOT ON WAITLIST!"
            ])
            server.sendmail("sdhains2@gmail.com", "sam@samhains.com", msg)
        else:
            msg = "\r\n".join([
                "From: sdhains2@gmail.com",
                "To: sam@samhains.com",
                "Subject: WAITLIST OPEN",
                "",
                "NEURAL AESTHETIC HAS A SPOT ON WAITLIST!"
            ])
            server.sendmail("sdhains2@gmail.com", "sam@samhains.com", msg)

check_nyu()
