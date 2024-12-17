import requests
import time
from datetime import datetime 



start_date_from_user_input = input("Enter starting date in yyyy/mm/dd format: ")
print("\n")
end_date_from_user_input = input("Enter closing date in yyyy/mm/dd format:")
print("\n")

# convert user input into datetime format for computer use
start_date = datetime.strptime(start_date_from_user_input, "%Y/%m/%d")
end_date = datetime.strptime(end_date_from_user_input, "%Y/%m/%d")
#print(start_date)
#print(end_date)

"""'ticker symbol' indicate various company's ticker symbols according to NASDAQ"""
ticker_symbol = input("Enter the ticker symbol: ")
print("\n")

"""the 'time.mktime' takes in a timetuple which consists of 'struct_time', and returns the time in non-leaped seconds"""
epoch_start_time = int(time.mktime(start_date.timetuple()))
epoch_end_time =  int(time.mktime(end_date.timetuple()))
#print(epoch_start_time)
#print(epoch_end_time)

"""this 'header' variable contains a fire way to combat download issues of website"""
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker_symbol}?period1={epoch_start_time}&period2={epoch_end_time}&interval=1d&events=history&includeAdjustedClose=true"
link_to_yahoo_download = requests.get(url, headers= headers).content     
"""here we have requested the url object and used the '.content' to grab the content which outputs 'forbidden' bc file is in bytes"""
# the yahoo page, similar to most modern page does not allow scripts to download files. 
# this issue can be bypassed using the "header" variable created above
print(link_to_yahoo_download)
print("\n")


"""since file is a byte object, we need to create an empty file and write those bytes into as actual file we can use"""
with open("stock_data.csv", "wb") as stockdata_csv_file:
    stockdata_csv_file.write(link_to_yahoo_download)
    # this uses the byte object to create a new csv file

