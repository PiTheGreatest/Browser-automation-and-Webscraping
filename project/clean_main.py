from bs4 import BeautifulSoup
from pathlib import Path
import requests
import pandas as pd

url = "https://www.rottentomatoes.com/browse/tv_series_browse/?page=7"

for page in range(1, 10):
    response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")
else:
    print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("div", attrs={'data-qa' : 'discovery-media-list-item'})


def crawl_movies(show_tags):

    show_name_list = []
    latest_ep_list = []
    critic_score_list = []
    audience_score_list = []
    show_cover_image_list = []
    synopsis_list = []
    network_list = []
    genre_list = []
    rating_list = []
    language_list = []
    release_date_list = []

    for show in show_tags:
        try:
            show_name_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-title'}).text.strip())
            latest_ep_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-start-date'}).text[29:].strip())
            critic_score_list.append(show.find("rt-text", attrs={'slot' : 'criticsScore'}).text.strip())
            audience_score_list.append(show.find("rt-text", attrs={'slot' : 'audienceScore'}).text.strip())
        
        except:
            show_name_list.append("Missing")
            latest_ep_list.append("Missing")
            critic_score_list.append("Missing")
            audience_score_list.append("Missing")

        del show_name_list[116:]
        del latest_ep_list[116:]
        del critic_score_list[116:]
        del audience_score_list[116:]
            

    return {"Show-name" : show_name_list, "Latest-episode" : latest_ep_list, "Critic-score" : critic_score_list, "Audience-score" : audience_score_list}

movies_data = crawl_movies(tags)
"""print(movies_data)"""   # this returns the data saved in a dictionary

# creating a file to store scrapped data
path = Path("Browser automation and Webscraping/project")
filename = "crawl-movies.csv"
filepath = path / Path(filename)
#filepath.touch()    #this creates the file in the specified directory. it is good practice to delete this command after file has been created

# saving the scraped data as a csv file
pd.DataFrame(movies_data).to_csv("Browser automation and Webscraping/project/crawl-movies.csv", index=False)