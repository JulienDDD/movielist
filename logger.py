from datetime import date
from datetime import datetime


def log(message) :
    with open("movie.log", "a") as f:
        now = datetime.now()
        fulltime = str(date.today()) + " " + str(now.strftime("%H:%M:%S"))
        f.write("\n" + fulltime + " - " + message)
        f.close()

