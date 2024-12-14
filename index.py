from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time 

# Connect with the driver and open the browser
service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service)
bot.maximize_window()
# Open the page
bot.get("https://www.viajesexito.com")
time.sleep(1)

# Go to the packages section
packages = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[1]/a')
time.sleep(2)
packages.click()
time.sleep(2)

# Select the origin
inputOrigin = "jose maria"
origin = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div')
time.sleep(2)
origin.click()
time.sleep(2)
origin.send_keys(inputOrigin)
time.sleep(2)
# Select the airport
airportOrigin = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div')
time.sleep(2)
airportOrigin.click()
time.sleep(2)

# Select the destination
inputDestination = "Aeropuerto Internacional de Cancún"
destination = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
time.sleep(2)
destination.click()
time.sleep(2)
destination.send_keys(inputDestination)
time.sleep(2)
# Select the airport
airportDestination = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div')
time.sleep(2)
airportDestination.click()
time.sleep(2)

# Select the date
date = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
time.sleep(2)
date.click()
time.sleep(2)
# Select the departure date
departureDate = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[5]/div[5]/div[2]/div[1]')
time.sleep(2)
departureDate.click()
time.sleep(2)
# Select the return date
returnDate = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[2]')
time.sleep(2)
returnDate.click()
time.sleep(2)
# Click on the button to accept
accept = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[3]/button[2]')
time.sleep(2)

# Select the number of rooms
rooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div/p')
time.sleep(2)
rooms.click()
time.sleep(2)
# Select one more room
moreRooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
time.sleep(2)
moreRooms.click()
time.sleep(2)
# Select the number of adults
adults = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button')
time.sleep(2)
actions = ActionChains(bot)
actions.double_click(adults).perform()
time.sleep(2)
# Apply the changes
apply = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
time.sleep(2)
apply.click()
time.sleep(2)

# Click on the search button
search = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a')
time.sleep(2)
search.click()
time.sleep(2)

print("Price of all packages")
print("")
# Select the first package
firstPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[1]/div/div/div[2]/div/div[1]/div[2]/p[1]')
print("First package: " + firstPackage.text)
print("")
time.sleep(2)
# Select the second package
secondPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[2]/p[1]')
print("Second package: " + secondPackage.text)
print("")
time.sleep(2)
# Select the third package
thirdPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/p[1]')
print("Third package: " + thirdPackage.text)
print("")
time.sleep(2)
# Select the fourth package
fourthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[4]/div/div/div[2]/div/div[1]/div[2]/p[1]')
print("Fourth package: " + fourthPackage.text)
print("")
time.sleep(2)
# Select the fifth package
fifthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[5]/div/div/div[2]/div/div[1]/div[2]/p[1]')
print("Fifth package: " + fifthPackage.text)
print("")
time.sleep(2)

# Modify the search
modifySearch = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[1]/div/button[1]')
time.sleep(2)
modifySearch.click()
time.sleep(2)
# Advanced options
advancedOptions = bot.find_element(By.XPATH, '/html/body/div[8]/div/div/div[6]/a')
time.sleep(2)
advancedOptions.click()
time.sleep(2)
# Select Airline
inputAirline = "Avianca"
airline = bot.find_element(By.XPATH, '/html/body/div[8]/div/div/div[7]/div[2]/input')
time.sleep(2)
airline.click()
time.sleep(2)
airline.send_keys(inputAirline)
time.sleep(2)
# Select option
optionAirline = bot.find_element(By.XPATH, '/html/body/ul[2]/li[1]/a')
time.sleep(2)
optionAirline.click()
time.sleep(2)
# Apply the changes
applyChanges = bot.find_element(By.XPATH, '/html/body/ul[2]/li[1]/a')
time.sleep(2)
applyChanges.click()
time.sleep(2)


