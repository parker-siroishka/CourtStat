import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless=new")
options.add_argument('--pageLoadStrategy=none')
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()

# Open the URL in the web browser
url = 'https://canadawest.org/sports/mvball/2023-24/teams'
driver.get(url)

# Find all anchor elements matching the XPath
elements = driver.find_elements(
    By.XPATH, '//a[contains(@href, "/sports/mvball/2023-24/teams/")]')

# Extract the href attribute values into a list
href_values = set([element.get_attribute("href") for element in elements])
# Close the web browser
# driver.quit()

for href in href_values:
    outer_start = time.time()
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
    player_hrefs = set(player_hrefs)

    for href in player_hrefs:
        inner_start = time.time()
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML%2C like Gecko) Chrome/97.0.4692.99 Safari/537.36 OPR/83.0.4254.62'
        request = Request(href, headers={'User-Agent': user_agent})
        page = urlopen(request)
        soup = BeautifulSoup(page, 'html.parser')
        player_data = {}
        # Find the table by its ordering
        table = soup.findAll("table")[0]
        player_name = soup.findAll("h1")[0]
        player_name = player_name.contents[2].replace(
            '\n', '').replace('\r', '').replace('\t', '').strip()
        # Get player name
        player_data['Player Name'] = player_name
        # Loop through each row in the table
        for row in table.find_all("tr"):
            # Extract the text content of the cells in the row
            cells = row.find_all("td")
            if cells:
                key = cells[0].text.strip()
                values = [cell.text.strip() for cell in cells[1:]]
                player_data[key] = {
                    "Total": values[0],
                    "Rank": values[1],
                    "Conference": values[2],
                    "Conference Rank": values[3],
                }

        # Print the result
        print(player_data)
        inner_stop = time.time()
        print("Inner time:" + str(inner_stop - inner_start))
    outer_stop = time.time()
    print("Outer time:" + str(outer_stop - outer_start))
