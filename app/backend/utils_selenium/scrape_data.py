from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Open the URL in the web browser
url = 'https://canadawest.org/sports/mvball/2023-24/teams'
driver.get(url)

# Find all anchor elements matching the XPath
elements = driver.find_elements(
    By.XPATH, '//a[contains(@href, "/sports/mvball/2023-24/teams/")]')

# Extract the href attribute values into a list
href_values = [element.get_attribute("href") for element in elements]

# Close the web browser
# driver.quit()

for href in href_values:
    driver.get(href)
    # Click the anchor tag with the specific text
    # Extract the [TEAM] value from the URL
    team_name = href.split("/")[-1]
    link_text = f"/sports/mvball/2023-24/teams/{team_name}?view=lineup"
    team_lineup = driver.find_element(
        By.XPATH, f"//a[contains(@href, '{link_text}')]")
    team_lineup.click()

    players = driver.find_elements(
        By.XPATH, '//a[contains(@href, "/sports/mvball/2023-24/players/")]')

    player_hrefs = [player.get_attribute("href") for player in players]

    for href in player_hrefs:
        driver.get(href)
