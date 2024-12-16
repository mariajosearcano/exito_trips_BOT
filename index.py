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
# packages = bot.find_element(By.XPATH, '/html/body/form/header/div[2]/div/div/nav/div[1]/a')
packages = bot.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
time.sleep(2)
packages.click()
time.sleep(2)

# Select the origin
inputOrigin = "jose maria"
# origin = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[1]/div/div/input')
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(2)
origin.click()
time.sleep(2)
# originPopUp = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
originPopUp = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveFrom_netactica_airhotel"]')
time.sleep(2)
originPopUp.click()
time.sleep(2)
originPopUp.send_keys(inputOrigin)
time.sleep(2)
# Select the airport
# airportOrigin = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div')
airportOrigin = bot.find_element(By.XPATH, '//*[@id="ui-id-5"]/li/div/div[2]/p')
time.sleep(2)
airportOrigin.click()
time.sleep(2)

# Select the destination
inputDestination = "Aeropuerto Internacional de Cancún"
# destination = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[1]/div/div[3]/div/div/input')
destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
time.sleep(2)
destination.click()
time.sleep(2)
# destinationPopUp = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/div[2]/input')
destinationPopUp = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
time.sleep(2)
destinationPopUp.click()
time.sleep(2)
destinationPopUp.send_keys(inputDestination)
time.sleep(2)
# Select the airport
# airportDestination = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[5]/ul/li/div')
airportDestination = bot.find_element(By.XPATH, '//*[@id="ui-id-6"]/li/div/div[2]')
time.sleep(2)
airportDestination.click()
time.sleep(2)

# Select the date
# date = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[2]/div/input')
date = bot.find_element(By.XPATH, '//*[@id="Date_netactica_air_hotel"]')
time.sleep(2)
date.click()
time.sleep(2)
# Select the departure date
# departureDate = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div[6]/div[4]/div[2]/div[1]')
departureDate = bot.find_element(By.XPATH, '//div[@aria-label="Jueves, Diciembre 26, 2024"]')
time.sleep(2)
departureDate.click()
time.sleep(2)
# Select the return date
# returnDate = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[5]/div[2]/div[1]')
returnDate = bot.find_element(By.XPATH, '//*[@id="Body"]/div[8]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div[5]/div[2]')
time.sleep(2)
returnDate.click()
time.sleep(2)
# Click on the button to accept
# accept = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[3]/button[2]')
accept = bot.find_element(By.XPATH, '//*[@id="Body"]/div[8]/div[2]/div[2]/div[3]/button[2]')
time.sleep(2)
accept.click()
time.sleep(2)

# Select the number of rooms
# rooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[3]/div/div/div/div')
rooms = bot.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
time.sleep(2)
rooms.click()
time.sleep(2)
# Select one more room
# moreRooms = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[1]/button[1]')
moreRooms = bot.find_element(By.XPATH, '//*[@id="btbAddRoomtwopaquetes"]')
time.sleep(2)
moreRooms.click()
time.sleep(2)
# Select the number of adults
# adults = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[1]/div[2]/div[3]/div/div[3]/div/div[2]/div/span[2]/button')
adults = bot.find_element(By.XPATH, '//*[@id="roomtwopaquetes"]/div/div[3]/div/div[2]/div/span[2]/button')
time.sleep(2)
actions = ActionChains(bot)
actions.double_click(adults).perform()
time.sleep(2)
# Apply the changes
# apply = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
apply = bot.find_element(By.XPATH, '//*[@id="btbClosePaxPopup"]')
time.sleep(2)
apply.click()
time.sleep(2)

# Click on the search button
# search = bot.find_element(By.XPATH, '/html/body/form/div[3]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div/div/div[4]/a')
search = bot.find_element(By.XPATH, '//*[@id="sbm_netactica_airhotel"]')
time.sleep(2)
search.click()
time.sleep(2)

print("Price of all packages")
print("")
# Select the first package
# firstPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[1]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
firstPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[1]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("First package: " + firstPackage.text)
print("")
time.sleep(2)
# Select the second package
# secondPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[2]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
secondPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[2]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Second package: " + secondPackage.text)
print("")
time.sleep(2)
# Select the third package
# thirdPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[3]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
thirdPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[3]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Third package: " + thirdPackage.text)
print("")
time.sleep(2)
# Select the fourth package
# fourthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[4]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
fourthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[4]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fourth package: " + fourthPackage.text)
print("")
time.sleep(2)
# Select the fifth package
# fifthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[5]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
fifthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[5]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fifth package: " + fifthPackage.text)
print("")
time.sleep(2)
# Select the six package
# sixthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[6]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
sixthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[6]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fifth package: " + sixthPackage.text)
print("")
time.sleep(2)
# Select the fifth package
# seventhPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[7]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
seventhPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[7]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fifth package: " + seventhPackage.text)
print("")
time.sleep(2)
# Select the fifth package
# eighthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[8]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
eighthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[8]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fifth package: " + eighthPackage.text)
print("")
time.sleep(2)
# Select the fifth package
# ninthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[9]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
ninthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[9]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fifth package: " + ninthPackage.text)
print("")
time.sleep(2)
# Select the fifth package
# tenthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[10]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
tenthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[10]/div/div/div[2]/div/div[1]/div[3]/p[1]/span[2]')
print("Fifth package: " + tenthPackage.text)
print("")
time.sleep(2)

# Advanced options
# advancedOptions = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[6]/a')
advancedOptions = bot.find_element(By.XPATH, '//*[@id="aShowHideAdvanced"]')
time.sleep(2)
advancedOptions.click()
time.sleep(2)
# Select Airline
inputAirline = "Avianca"
# airline = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[7]/div[2]/input')
airline = bot.find_element(By.XPATH, '//*[@id="txtAirlineCode"]')
time.sleep(2)
airline.click()
time.sleep(2)
airline.send_keys(inputAirline)
time.sleep(2)
# Select option
# optionAirline = bot.find_element(By.XPATH, '/html/body/ul[2]/li[1]/a')
optionAirline = bot.find_element(By.XPATH, '//*[@id="ui-id-4"]/li[1]/a')
time.sleep(2)
optionAirline.click()
time.sleep(2)
# Apply the changes
# applyChanges = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[1]/div/div[8]/input')
applyChanges = bot.find_element(By.XPATH, '//*[@id="ulNewSearch"]/div[8]/input')
time.sleep(2)
applyChanges.click()
time.sleep(2)


