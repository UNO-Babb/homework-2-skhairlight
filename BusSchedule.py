#BusSchedule.py
#Name: Salsabiel Khair Allah
#Date: Oct.21
#Assignment: Homework 2

import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def loadURL(url):
  """
  This function loads a given URL and returns the text
  that is displayed on the site. It does not return the
  raw HTML code but only the code that is visible on the page.
  """
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("--headless");
  driver = webdriver.Chrome(options=chrome_options)
  driver.get(url)
  content=driver.find_element(By.XPATH, "/html/body").text
  driver.quit()

  return content

def loadTestPage():
  """
  This function returns the contents of our test page.
  This is done to avoid unnecessary calls to the site
  for our testing.
  """
  page = open("testPage.txt", 'r')
  contents = page.read()
  page.close()

  return contents

def getHours(time_str):
  """Extracts the hour from 'HH:MM AM/PM' and converts to 24-hour format."""
  t = datetime.datetime.strptime(time_str, "%I:%M %p")
  return t.hour

def getMinutes(time_str):
  """Extracts the minutes from 'HH:MM AM/PM'."""
  t = datetime.datetime.strptime(time_srt, "%I:%M %p")
  retrun t.minute

def isLater(time1, time2):
  """Returns True if time1 is later than time2, otherwise False."""
  return time1 > time2

def findNextBusTimes(text):
  """ Given the page text, this finds all bus times, compares them to current, and displays the next arrivals."""
  lines = text.splitlines()
  times = []

  for line in lines:
    if "AM" in line or "PM" in line:
      line = line.strip()
      if len(line) >= 7 and ":" in line:
        times.append(line)

  current_time = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
  print("Current Time:", current_time.strftime("%I:%M %p"))

  next_buses = []
  for t in times:
    try:
      bus_time = datetime.datetime.strptime(t, "%I:%M %p).replace(year=current_time.year, month=current_time.month, day=current_time.day)
      if isLater(bus_time, current_time):
        diff = (bus_time, current_time):
        next_buses.append(diff)
    except:
      pass

  if len(next_buses) > 0:
    print(f"The next bus will arrive in {next_buses[0]} minutes.")
    if len(next_buses) > 1:
      print(f"The following bus will arrive in {next_buses[1]} minutes.")
  else:
    print("No more buses scheduled today.")
    


def main():
  stopNumber = "2269"
  routeNumber = "11"
  direction = "EAST"
  
  url = "https://myride.ometro.com/Schedule?stopCode={stopNumber}&routeNumber={routeNumber}&directionName={direction}"
  #c1 = loadURL(url) #loads the web page
  c1 = loadTestPage() #loads the test page
  findNextBusTimes(c1)

main()
