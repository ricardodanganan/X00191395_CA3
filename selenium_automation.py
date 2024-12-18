from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the application URL
    driver.get("http://localhost:8000")  # Replace with your test environment URL
    time.sleep(2)  # Allow time for the page to load

    # Step 2: Simulate user action (search or input field)
    search_box = driver.find_element(By.NAME, "q")  # Replace 'q' with your input field name
    search_box.send_keys("Test Data")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    # Step 3: Validate results
    assert "No results found." not in driver.page_source
    print("Test Passed: Search functionality works!")

except Exception as e:
    print(f"Test Failed: {str(e)}")

finally:
    driver.quit()  # Close the browser
