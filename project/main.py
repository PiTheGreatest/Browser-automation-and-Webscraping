from bs4 import BeautifulSoup
import os
import requests
import pandas as pd

url = "https://www.rottentomatoes.com/browse/tv_series_browse/?page=6"

for page in range(1, 10):
    response = requests.get(url)

if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")
else:
    print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("div", attrs={'data-qa' : 'discovery-media-list-item'})
#print(movie_tags)

for tag in tags:
        url2 = tag.find("a", attrs={"data-qa" : "discovery-media-list-item-caption"}.get("href"))
        r2 = requests.get(url2)
        if r2.status_code != 200:
            raise Exception(f"Failed to load page {url}")
        else:
            print(response.status_code)
            
        # soup2 = BeautifulSoup(r2.text, "html.parser")
        # tag2 = soup2.find_all("div", attrs={"data-adobe-id" : "media-scorecard"}


# extract name of show
def get_name_of_shows(show_tags):

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
         pass
        # shows = show.find("span", attrs={'data-qa' : 'discovery-media-list-item-title'})
        # dates = show.find("span", attrs={'data-qa' : 'discovery-media-list-item-start-date'})
    #     try:
    #         # show_name_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-title'}).text.strip())
    #         # latest_ep_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-start-date'}).text[29:].strip())
    #         synopsis_list.append(comp_list.find("rt-text", attrs={"slot" : "content"}).text.strip())

    #     except:
    #         # show_name_list.append("Missing")
    #         # latest_ep_list.append("Missing")
    #         synopsis_list.append()

    # return show_name_list, latest_ep_list, synopsis_list


# extract latest episode
# def get_latest_ep(show_tags):

#     latest_ep_list = []

#     for show in show_tags:
#         dates = show.find("span", attrs={'data-qa' : 'discovery-media-list-item-start-date'})
#         #latest_ep_list.append(show.find("span", attrs={'data-qa' : 'discovery-media-list-item-start-date'}).text[16:].strip())
#     print(type(dates))


# name_of_movies = get_name_of_shows(tags)
# print(name_of_movies)

# latest_dates = get_latest_ep(movie_tags)
# print(latest_dates)




