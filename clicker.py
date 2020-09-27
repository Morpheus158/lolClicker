from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(r"C:\Users\Pavel\Documents\python\lolClicker\chromedriver.exe")
answers = ["Tryndamere", "FunPlus Phoenix", "SK Telecom T1", "2009", "Ezreal", "Graves", "Jönköping", "Marksman", "The blade dancer", "Fighter", "Kai'Sa", "Fnatic", "Viper", "Orb of Deception",
 "Paris", "08:00", "Tremors", "The prodigal explorer", "Caitlyn", "+75 Mana", "71:34 min", "Ornn", "Samira and Yone", "USA", "99", "Ryze", "2011", "110", "9", "The deceiver", "'40,000", "20:00",
 "Team Liquid", "213", "22", "Terrashape", "151", "The blind monk", "85,5%", "Named after Riot employees", "Jinx", "59", "Pantheon", "Bladework", "Gen.G", "Kled", "Garen", "Galio",
 "The titan of the depths", "23:33 min", "Katarina and Cassiopeia", "+3 life on-hit", "Kennen and Tahm Kench", "Pudong Football Stadium"]

counter = 0

driver.maximize_window()
driver.get(r"https://join.stagecast.se/api/web/code/3563/Md61PapT0Uh1PRxtriaLnoTuUEeYFnkkxYQ9")

driver.switch_to.frame("frame")

checkbox = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "mc-checkmark")))
checkbox.click()

startButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "main-button")))
startButton.click()

playAgainButton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Play Again"]')))
playAgainButton.click()

time.sleep(5)

while True:
    for answer in answers:
        isFound = driver.find_elements_by_xpath('//span[text()="' + answer +'"]')
        if len(isFound) > 0:
            print("Here")
            time.sleep(0.4)
            isFound[0].click()
            time.sleep(0.55)