# Football Stats Data Scraping

## Overview

This script scrapes data from fbref.com for all teams in the English Premier League. It loops through all teams and extracts the data from the table. This is achieved by first extracting the links for each team from the main table. The links are then used to construct the full URLs for each team. The script then loops through each team URL and extracts the data from the "Standard Stats" table. The data is then appended to a list, which is then converted to a DataFrame. Finally, the data is saved to a CSV file.

Although this script is used for the English Premier League, it can also be used for LaLiga and other leagues.

## Dependencies

The script requires the following Python libraries:

- BeautifulSoup
- pandas
- requests
- time

## Usage

To run the script, simply execute the `premScraper.py` file. The script will automatically scrape the data and save it to a file named `prem_stats.csv`.

Please note that the script pauses for 5 seconds after scraping each team to avoid being blocked by the website.

## Contact

For any issues or suggestions, please reach out through the [GitHub repository](https://github.com/Riasy7/Football-Stats-Data-Scraping).
