from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize chromedriver
driver = webdriver.Chrome()

# Open the webpage
url = 'https://hscresult.bise-ctg.gov.bd/hsc22/23/individual/'  # Website URL
driver.get(url)

wait = WebDriverWait(driver, 10)

time.sleep(5)  # Wait for the page to load

initial_roll_number = 521654  # Initial roll number
number_of_roll_numbers = 1  # Number of roll numbers to fetch

for i in range(number_of_roll_numbers):
    roll_number = initial_roll_number + i

    driver.get(url)  # Refresh the page for a new roll number

    roll_input = wait.until(EC.presence_of_element_located((By.ID, 'roll')))  # Find the input box
    roll_input.clear()  # Clear any existing text in the input box
    roll_input.send_keys(str(roll_number))  # Enter the roll number

    time.sleep(2)  # Wait for 2 seconds after entering the roll number for the page to load

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'button2')))  # Find the submit button
    submit_button.click()  # Click the submit button

    time.sleep(4)  # Wait for 4 seconds for the result to load

    # Extracting roll number, name, and GPA
    roll_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Roll No')]/following-sibling::td[1]")))
    name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Name')]/following-sibling::td[1]")))
    gpa_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'GPA')]/following-sibling::td[1]")))
    result_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Result')]/following-sibling::td[1]")))
    bangla_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'BANGLA(101)')]/following-sibling::td[1]")))
    english_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'ENGLISH(107)')]/following-sibling::td[1]")))
    ict_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'INFORMATION & COMMUNICATION TECHNOLOGY(275)')]/following-sibling::td[1]")))
    accounting_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'ACCOUNTING(253)')]/following-sibling::td[1]")))
    businessorg_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'BUSINESS ORGANIZATION & MANAGEMENT(277)')]/following-sibling::td[1]")))
    finance_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'FINANCE, BANKING & INSURANCE(292)')]/following-sibling::td[1]")))
    economics_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'ECONOMICS(109)')]/following-sibling::td[1]")))

    roll = roll_element.text.strip()
    name = name_element.text.strip()
    gpa = gpa_element.text.strip()
    result = result_element.text.strip()
    bangla = bangla_element.text.strip()
    english = english_element.text.strip()
    ict = ict_element.text.strip()
    accounting = accounting_element.text.strip()
    business = businessorg_element.text.strip()
    finance = finance_element.text.strip()
    economics = economics_element.text.strip()

    filename = f"{name}_{roll}_{gpa}_{result}.txt"
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\nRoll: {roll}\nGPA: {gpa}\nResult: {result}\n\nSubject Wise-mark:\nBANGLA(101): {bangla}\nENGLISH(107): {english}\nINFORMATION & COMMUNICATION TECHNOLOGY(275): {ict}\nACCOUNTING(253): {accounting}\nBUSINESS ORGANIZATION & MANAGEMENT(277): {business}\nFINANCE, BANKING & INSURANCE(292): {finance}\nECONOMICS(109): {economics}")

driver.quit()  # Close the browser after fetching all results
