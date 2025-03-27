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

initial_roll_number = 551865  # Initial roll number
number_of_roll_numbers = 10 # Number of roll numbers to fetch

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
    
    roll = roll_element.text.strip()
    name = name_element.text.strip()
    gpa = gpa_element.text.strip()
    result = result_element.text.strip()
   
    filename = f"{name}_{roll}_{gpa}_{result}.txt"
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\nRoll: {roll}\nGPA: {gpa}\nResult: {result}")

driver.quit()  # Close the browser after fetching all results
