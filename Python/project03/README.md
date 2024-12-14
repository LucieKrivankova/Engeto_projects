# Engeto Python 3.projekt
Třetí projekt pro Python akademii od Engeta.
## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz k prohlédnutí najdete [zde](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).
## Instalace knihoven
Knihovny, které jsou použity v kódu jsou uložene v souboru `requirements.txt`. Pro instalaci doporučuji použít nové virtuální prostředí a s nainstalovaným manažerem spustit následovně:
```
§ pip --version                      # overim verzi manazeru
§ pip install -r requirements.txt    # nainstaluje knihovny
```
## Spuštění projektu
Spuštění souboru `election_scraper.py` v rámci příkazového řádku požaduje dva povinné argumenty.
```
python election_scraper.py <URL> <output_file.csv>
```
Následně se vám stáhnou výsledky jako soubor s příponou `.csv`.
## Ukázka projektu
Výsledky hlasování pro okres Prostějov:
  1. argument: `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6206`
  2. argument: `vysledky_vyskov.csv`
###Spuštění programu:
```
python election_scraper.py 'https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6206' 'vysledky_vyskov.csv'
```
###Průběh stahování:
```
STARTING PROGRAM ELECTIONS SCRAPER
DOWNLOADING DATA FROM SELECTED URL: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6206
SAVING TO FILE: vysledky_vyskov.csv
ENDING PROGRAM ELECTIONS SCRAPER
```
###Částečný výstup:
```
code,location,registered,envelopes,valid,...
592897,Bohaté Málkovice,200,111,111,4,0,0,14,0,2,9,0,1,0,0,0,3,0,1,48,1,0,16,0,0,0,0,10,2,0
592901,Bohdalice-Pavlovice,687,426,422,25,0,0,36,0,19,42,3,0,6,1,1,21,4,6,112,0,1,54,0,3,0,1,87,0,0
```
