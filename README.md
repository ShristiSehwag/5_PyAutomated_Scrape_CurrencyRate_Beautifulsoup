# 5. Scrape Currency Rate Using Beautifulsoup
website : https://www.x-rates.com/calculator/?from=USD&to=INR&amount=1

Beautiful soup is a Python library that is highly suitable for Web Scraping. It creates a parse tree that can be used to extract data from HTML on a website. Beautiful soup also has multiple features for navigation, searching, and modifying these parse trees.

## Code :
The script uses BeautifulSoup and requests to scrape real-time currency exchange rates from x-rates.com.

It constructs a URL with input and output currencies specified to fetch the exchange rate.

It sends a GET request to the URL and parses the HTML content using BeautifulSoup.

It extracts the exchange rate from the parsed HTML by locating the relevant HTML element.

Finally, it returns the extracted exchange rate, which can then be used in further processing or displayed.

## Reference :
![Alt text](https://github.com/ShristiSehwag/5_PyAutomated_Scrape_CurrencyRate_Beautifulsoup/blob/main/Scrape_CurrencyRate_Beautifulsoup.png)

