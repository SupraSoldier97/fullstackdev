import time
import webbrowser

total_breaks = 20
break_count = 0

url = "https://houston.craigslist.org/boa/6164726014.html"

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

print ("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(2)
    webbrowser.get(chrome_path).open(url)
    break_count = break_count + 1