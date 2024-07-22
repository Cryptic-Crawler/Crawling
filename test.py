import requests
from bs4 import BeautifulSoup

# URL of the League of Legends profile
url = 'https://www.leagueofgraphs.com/summoner/euw/TheShackledOne-003'

# Headers
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    match_cells = soup.find_all('td', class_='text-center nopadding kdaColumn')

    # Open a file for writing the data
    with open('lol_profile_results.txt', 'w', encoding='utf-8') as file:
        for cell in match_cells:
            # Extract match result
            result_element = cell.find_previous_sibling('td', class_='resultCellLight').find('div', class_='victoryDefeatText')
            if result_element:
                result = result_element.text.strip()
                file.write(f"Match Result: {result}\n")

                # Extract game mode
                game_mode_element = cell.find_previous_sibling('td', class_='resultCellLight').find('div', class_='gameMode')
                if game_mode_element:
                    game_mode = game_mode_element.text.strip()
                    file.write(f"Game Mode: {game_mode}\n")

                # Extract game date
                game_date_element = cell.find_previous_sibling('td', class_='resultCellLight').find('div', class_='gameDate')
                if game_date_element:
                    game_date = game_date_element.text.strip()
                    file.write(f"Game Date: {game_date}\n")

                # Extract game duration
                game_duration_element = cell.find_previous_sibling('td', class_='resultCellLight').find('div', class_='gameDuration')
                if game_duration_element:
                    game_duration = game_duration_element.text.strip()
                    file.write(f"Game Duration: {game_duration}\n")

                # Extract kills, deaths, assists
                kda_element = cell.find('div', class_='kda')
                if kda_element:
                    kills = kda_element.find('span', class_='kills').text.strip()
                    deaths = kda_element.find('span', class_='deaths').text.strip()
                    assists = kda_element.find('span', class_='assists').text.strip()
                    file.write(f"Kills/Deaths/Assists: {kills}/{deaths}/{assists}\n")
                else:
                    file.write("Kills/Deaths/Assists: N/A\n")
                # Extract LP change
                lp_change_element = cell.find_previous_sibling('td', class_='resultCellLight').find('div', class_='lpChange')
                if lp_change_element:
                    lp_change = lp_change_element.text.strip()
                    file.write(f"LP Change: {lp_change}\n")
                else:
                    file.write("LP Change: N/A\n")

                file.write("-" * 20 + "\n")

    print("Data saved to 'lol_profile_results.txt'")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
