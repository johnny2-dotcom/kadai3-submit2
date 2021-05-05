import eel
import search
 
# eel.init("html")


@eel.expose
def kimetsu_search(word,csv_name):
    search.kimetsu_search(word,csv_name)

eel.init("html")
eel.start("index.html")
