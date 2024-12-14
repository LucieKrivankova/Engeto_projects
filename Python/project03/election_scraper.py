"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lucie Křivánková
email: luciekrivankova.10@gmail.com
discord: .torali
"""


import requests
import csv
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


def get_location(url: str):
    """
    Stáhne data o lokalitách a politických stranách.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    location = []
    all_parties = []

    for td in soup.find_all('td', class_='cislo'):
        code_link = td.find('a')
        if code_link:
            code = code_link.get_text()
            full_url = urljoin(url, code_link['href'])

        location_name_td = td.find_next('td', class_='overflow_name')
        if location_name_td:
            location_name = location_name_td.get_text(strip=True)
            location_data = get_location_data(full_url)

            for party_data in location_data.get('votes', []):
                party_name = party_data[0]
                if party_name not in all_parties:
                    all_parties.append(party_name)

            location.append([
                code, location_name, 
                location_data.get('registered', ''),
                location_data.get('envelopes', ''),
                location_data.get('valid', ''),
                location_data.get('votes', [])
            ])

    return location, all_parties


def get_party_votes(soup):
    """
    Získá data o hlasech jednotlivých stran.
    """
    parties = []
    table_rows = soup.find_all('tr')

    for row in table_rows:
        cells = row.find_all('td')
        if len(cells) >= 4:
            party_name = cells[1].get_text(strip=True)
            votes = cells[2].get_text(strip=True)

            if party_name and votes.isdigit():
                parties.append((party_name, int(votes)))

    return parties


def get_location_data(url: str):
    """
    Získá data o konkrétní lokalitě z detailní stránky.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    registered = soup.find('td', headers='sa2').get_text(strip=True)
    envelopes = soup.find('td', headers='sa3').get_text(strip=True)
    valid = soup.find('td', headers='sa6').get_text(strip=True)

    votes = get_party_votes(soup)

    return {
        'registered': registered,
        'envelopes': envelopes,
        'valid': valid,
        'votes': votes
    }


def save_to_csv(data, parties, output_file):
    """
    Uloží data do CSV souboru.
    """
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow(['code', 'location', 'registered', 'envelopes', 'valid'] + parties)

        for town in data:
            row = town[:5]
            voting_results = {party: '0' for party in parties}

            for party_data in town[5]:
                party = party_data[0]
                votes = party_data[1]
                voting_results[party] = votes

            row.extend([voting_results[party] for party in parties])
            writer.writerow(row)


VALID_URL_PREFIX = "https://www.volby.cz/pls/ps2017nss/"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("USAGE: python election_scraper.py <URL> <output_file.csv>") 
        sys.exit(1)

    elections_url = sys.argv[1]
    output_file = sys.argv[2]

    parsed_url = urlparse(elections_url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        print("ERROR: THE FIRST ARGUMENT MUST BE A VALID URL.") 
        sys.exit(1)

    if not elections_url.startswith(VALID_URL_PREFIX):
        print(f"ERROR: THE URL MUST START WITH '{VALID_URL_PREFIX}'.") 
        sys.exit(1)

    print("STARTING PROGRAM ELECTIONS SCRAPER")
    print(f"DOWNLOADING DATA FROM SELECTED URL: {elections_url}")
    
    try:
        results, parties = get_location(elections_url)
    except Exception as e:
        print(f"ERROR WHILE DOWNLOADING OR PROCESSING DATA: {e}") 
        sys.exit(1)

    print(f"SAVING TO FILE: {output_file}")
    
    try:
        save_to_csv(results, parties, output_file)
    except Exception as e:
        print(f"ERROR WHILE SAVING DATA TO FILE: {e}") 
        sys.exit(1)

    print("ENDING PROGRAM ELECTIONS SCRAPER")
