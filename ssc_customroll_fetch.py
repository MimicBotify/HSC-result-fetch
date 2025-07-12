from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Initialize chromedriver
driver = webdriver.Chrome()

# Open the webpage
#url = 'https://hscresult.bise-ctg.gov.bd/hsc22/23/individual/'  # HSC Website URL
url = "https://sresult.bise-ctg.gov.bd/rxto2025/individual/"   # SSC Website URL
driver.get(url)

wait = WebDriverWait(driver, 10)

time.sleep(4)  # Wait for the page to load

with open('roll.txt', 'r') as f:
    roll_numbers = [line.strip() for line in f if line.strip()]

# Create results directory if it doesn't exist
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

for roll_number in roll_numbers:
    driver.get(url)  # Refresh the page for a new roll number

    roll_input = wait.until(EC.presence_of_element_located((By.ID, 'roll')))  # Find the input box
    roll_input.clear()  # Clear any existing text in the input box
    roll_input.send_keys(roll_number)  # Enter the roll number

    time.sleep(2)  # Wait for 2 seconds after entering the roll number for the page to load

    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'button2')))  # Find the submit button
    submit_button.click()  # Click the submit button

    time.sleep(4)   # Wait for 4 seconds for the result to load

   # Extracting roll number, name, and GPA
    roll_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[3]/table/tbody/tr[1]/td[2]")))
    name_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[3]/table/tbody/tr[1]/td[4]")))
    gpa_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[3]/table/tbody/tr[6]/td[2]")))
    result_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div[3]/table/tbody/tr[6]/td[2]")))

    roll = roll_element.text.strip()
    name = name_element.text.strip()
    gpa = gpa_element.text.strip()
    result = result_element.text.strip()

    filename = f"{name}_{roll}_{gpa}_{result}.txt"
    filepath = os.path.join(results_dir, filename)
    with open(filepath, 'w') as file:
        file.write(f"Name: {name}\nRoll: {roll}\nGPA: {gpa}\nResult: {result}\n\nSubject Wise-mark: ")

driver.quit()  # Close the browser after fetching all results