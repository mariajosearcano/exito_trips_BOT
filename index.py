from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Evita logs innecesarios
chrome_options.add_argument("--disable-usb")  # Desactiva búsqueda USB
chrome_options.add_argument("--ignore-certificate-errors")  # Ignora errores SSL
chrome_options.add_argument("--disable-extensions")  # Desactiva extensiones

# Connect with the driver and open the browser
service = Service("driver/chromedriver.exe")
bot = webdriver.Chrome(service=service, options=chrome_options)
bot.maximize_window()
# Open the page
bot.get("https://www.viajesexito.com")
time.sleep(1)

# Go to the packages section
packages = bot.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[1]/a')
time.sleep(1)
packages.click()
time.sleep(1)

# Do a little scroll
bot.execute_script("window.scrollTo(0, 200)")
time.sleep(1)

# Select the origin
inputOrigin = "jose maria"
origin = bot.find_element(By.XPATH, '//*[@id="CityPredictiveFrom_netactica_airhotel"]')
time.sleep(1)
origin.click()
time.sleep(1)
originPopUp = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveFrom_netactica_airhotel"]')
time.sleep(1)
originPopUp.click()
time.sleep(1)
originPopUp.send_keys(inputOrigin)
time.sleep(3)
# Select the airport
airportOrigin = bot.find_element(By.XPATH, '//*[@id="ui-id-5"]/li/div/div[2]/p')
time.sleep(1)
airportOrigin.click()
time.sleep(1)

# Select the destination
inputDestination = "Aeropuerto Internacional de Cancún"
destination = bot.find_element(By.XPATH, '//*[@id="CityPredictiveTo_netactica_airhotel"]')
time.sleep(1)
destination.click()
time.sleep(1)
destinationPopUp = bot.find_element(By.XPATH, '//*[@id="popUpCityPredictiveTo_netactica_airhotel"]')
time.sleep(1)
destinationPopUp.click()
time.sleep(1)
destinationPopUp.send_keys(inputDestination)
time.sleep(3)
# Select the airport
airportDestination = bot.find_element(By.XPATH, '//*[@id="ui-id-6"]/li/div/div[2]')
time.sleep(1)
airportDestination.click()
time.sleep(1)

# Select the date
date = bot.find_element(By.XPATH, '//*[@id="Date_netactica_air_hotel"]')
time.sleep(1)
date.click()
time.sleep(1)
# Select the departure date
departureDate = bot.find_element(By.XPATH, '//div[@aria-label="Lunes, Diciembre 23, 2024"]')
time.sleep(1)
departureDate.click()
time.sleep(1)
# Select the return date
returnDate = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[1]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/div/div[3]/div/div[3]/div[1]')
time.sleep(1)
returnDate.click()                      
time.sleep(1)
# Click on the button to accept
accept = bot.find_element(By.XPATH, '/html/body/div[9]/div[2]/div[2]/div[2]/button[2]')
time.sleep(1)
accept.click()
time.sleep(1)

# Select the number of rooms
rooms = bot.find_element(By.XPATH, '//*[@id="txtNumPassengersPaquetesComplete"]')
time.sleep(1)
rooms.click()
time.sleep(1)
# Select one more room
moreRooms = bot.find_element(By.XPATH, '//*[@id="btbAddRoomtwopaquetes"]')
time.sleep(1)
moreRooms.click()
time.sleep(1)
# Select the number of adults
adults = bot.find_element(By.XPATH, '//*[@id="roomtwopaquetes"]/div/div[3]/div/div[2]/div/span[2]/button')
time.sleep(1)
actions = ActionChains(bot)
actions.double_click(adults).perform()
time.sleep(1)
# Apply the changes
apply = bot.find_element(By.XPATH, '/html/body/form/div[3]/div[2]/article/div/div[1]/div/div[1]/div/div/div[2]/div[2]/div[3]/div[4]/div[2]/div[2]/button')
time.sleep(1)
apply.click()
time.sleep(1)

# Click on the search button
search = bot.find_element(By.XPATH, '//*[@id="sbm_netactica_airhotel"]')
time.sleep(1)
search.click()
time.sleep(10)

# Go to new tab
bot.switch_to.window(bot.window_handles[1])


# Show packages
packages = WebDriverWait(bot, 10).until(
    ec.presence_of_all_elements_located(
        (By.XPATH, '//*[@id="divAirResults"]/div/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
    )
)


print("Price of all packages")
print("")
for idx, package in enumerate(packages):
    print(f"Package {idx + 1}: {package.text}")

print("")
# print("Price of all packages")
# print("")

# for i in range(0, 9):
#     package = WebDriverWait(bot, 10).until(
#         ec.presence_of_element_located((By.XPATH, '//*[@id="divAirResults"]/div[' + str(i+1) + ']/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')))
#     print("Package " + str(i+1) + ": " + package.text)

# print("")


#show airline
airline = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[1]/div[2]/div[1]/div/div[5]/div/div/div[4]/div[1]/input')
time.sleep(30)
airline.click()
time.sleep(20)


#whasapp footer
whatsapp = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[1]/header/div[1]/div[2]/nav/div/div[1]/a')
time.sleep(5)
whatsapp.click()
time.sleep(10)



# # Select the sixth package
# # sixthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[6]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# sixthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[6]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# print("Sixth package: " + sixthPackage.text)
# print("")
# time.sleep(3)

# # Select the seventh package
# # seventhPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[7]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# seventhPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[7]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# print("Seventh package: " + seventhPackage.text)
# print("")
# time.sleep(3)
#
# # Select the eighth package
# # eighthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[8]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# eighthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[8]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# print("Eighth package: " + eighthPackage.text)
# print("")
# time.sleep(3)
#
# # Select the ninth package
# # ninthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[9]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# ninthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[9]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# print("Ninth package: " + ninthPackage.text)
# print("")
# time.sleep(3)
#
# # Select the tenth package
# # tenthPackage = bot.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/div[4]/div/div/div/div[2]/div[7]/div/div[1]/div[6]/div[10]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# tenthPackage = bot.find_element(By.XPATH, '//*[@id="divAirResults"]/div[10]/div/div/div[2]/div/div[1]/div[2]/p[1]/span[2]')
# print("Tenth package: " + tenthPackage.text)
# print("")
# time.sleep(3)




