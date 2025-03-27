# Project Result Fetch

This project automates the process of fetching student results from the [Chittagong Board HSC Result website](https://hscresult.bise-ctg.gov.bd/hsc22/23/individual/) using Selenium WebDriver. It retrieves details such as roll number, name, GPA, result, and subject-wise marks (if applicable) and saves them into text files.

## Features

- Fetch results for a range of roll numbers.
- Fetch results for a custom list of roll numbers.
- Extract detailed subject-wise marks (optional).
- Save results in a structured text file format.

## Prerequisites

1. **Python**: Ensure Python is installed on your system.
2. **Selenium**: Install Selenium using pip:
   ```bash
   pip install selenium
   ```
3. **ChromeDriver**: Ensure the `chromedriver.exe` file is in the project directory and matches your installed Chrome version.

## Files

### 1. `Fetchresultwithgrade.py`
Fetches results for a single roll number or a range of roll numbers, including subject-wise marks.

### 2. `Fetchresult.py`
Fetches results for a range of roll numbers but does not include subject-wise marks.

### 3. `customrollfetchresult.py`
Fetches results for a custom list of roll numbers, including subject-wise marks.

### 4. `chromedriver.exe`
The ChromeDriver executable required for Selenium to interact with the Chrome browser.

## Usage

### 1. Fetch Results for a Range of Roll Numbers
Run `Fetchresult.py` or `Fetchresultwithgrade.py`:
```bash
python Fetchresult.py
```
or
```bash
python Fetchresultwithgrade.py
```
Modify the `initial_roll_number` and `number_of_roll_numbers` variables in the script to set the range.

### 2. Fetch Results for Custom Roll Numbers
Run `customrollfetchresult.py`:
```bash
python customrollfetchresult.py
```
Update the `roll_numbers` list in the script with the desired roll numbers.

## Output
Each result is saved as a text file in the format:
```
<Name>_<Roll>_<GPA>_<Result>.txt
```
The file contains:
- Name
- Roll number
- GPA
- Result
- Subject-wise marks (if applicable)

## Notes

- Ensure the website is accessible and functional before running the scripts.
- Adjust the `time.sleep()` values if the website takes longer to load.
- Use a stable internet connection for uninterrupted execution.

## Disclaimer
This project is for educational purposes only. Ensure compliance with the website's terms of use before automating data extraction.
