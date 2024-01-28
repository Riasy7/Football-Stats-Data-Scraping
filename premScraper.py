"""
Football Stats Data Scraping
Written by Ahmad Saadawi
Github: https://github.com/Riasy7
repo: https://github.com/Riasy7/Football-Stats-Data-Scraping
----------------------------------------
This script scrapes data from fbref.com for all teams in the English Premier League.
The script loops through all teams and extracts the data from the table.
This is done by first extracting the links for each team from the main table.
The links are then used to construct the full URLs for each team.
The script then loops through each team URL and extracts the data from the "Standard Stats" table.
The data is then appended to a list.
The list is then converted to a DataFrame.
The data is then saved to a CSV file.
----------------------------------------
This code is also used for LaLiga, and can be used for other leagues as well.
"""



from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

all_teams = []  # Initialize list to store data for all teams

html = requests.get('https://fbref.com/en/comps/9/Premier-League-Stats').text # Retrieve HTML content from the URL
soup = BeautifulSoup(html, 'lxml')
table = soup.find_all('table', class_ = 'stats_table')[0] # Extract the first table from the HTML

links = table.find_all('a')  # Extract all links present in the table
links = [l.get("href") for l in links]
links = [l for l in links if "/squads" in l] # Filter links to only include those containing "/squads"

team_urls = [f"https://fbref.com{l}" for l in links]  # Construct full URLs for each team

for team_url in team_urls:
    team_name = team_url.split("/")[-1].replace("-Stats","") # Extract team name from the URL
    data = requests.get(team_url).text
    soup = BeautifulSoup(data, 'lxml')
    stats = soup.find_all('table', class_ = 'stats_table')[0] # Extract the first table from the HTML

    if stats and stats.columns: stats.columns = stats.columns.droplevel() # Format the columns

    team_data = pd.read_html(str(stats))[0]
    team_data['Team'] = team_name
    all_teams.append(team_data) # Append the team data to the list
    time.sleep(5) # Pause execution for 5 seconds to avoid being blocked

stat_df = pd.concat(all_teams) # Concatenate all team data into a single DataFrame
stat_df.to_csv("prem_stats.csv") # Save the DataFrame to a CSV file