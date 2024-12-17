from bs4 import BeautifulSoup
import requests

def get_currency_rate(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1#google_vignette"
    source_code_content = requests.get(url).text
    soup_object = BeautifulSoup(source_code_content, "html.parser")
    currency_rate = soup_object.find("span", class_ = "ccOutputRslt").get_text()
    rate_string_list = currency_rate.split(" ")
    float_from_string_list = float(rate_string_list[0])
    return float_from_string_list


print("\n")
current_rate = get_currency_rate("EUR", "AUD")
print(current_rate)

