from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import threading
import requests

toaster = ToastNotifier()

def check_nyu():
    threading.Timer(60.0, check_nyu).start()
    url = "https://m.albert.nyu.edu/app/catalog/classsection/NYUNV/1188/22604"

    r  = requests.get(url)

    data = r.text

    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all(text="Closed"):
        if link == "Closed":
            print("still closed")
        else:
            print("WAITLIST! GO!")
            toaster.show_toast("WAITLIST! GO!")

check_nyu()
