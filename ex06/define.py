import sys
import requests
from bs4 import BeautifulSoup

def fetch_definition(word : str) -> None:
    base_url = "https://www.oxfordlearnersdictionaries.com/us/definition/english/"
    url = base_url + word.lower().strip()

    #my User-Agent

    headers = {
        "User-Agent" : (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/141.0.0.0 Safari/537.36Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
        )
    }

    print(f"Searching for: {word}")
    print(f"Fetching from: {url}\n")

    response = requests.get(url, headers=headers) # get the response
    if response.status_code != 200: #if we could not find the given page print an error
        print(f"Error: Could not retrieve page (status code {response.status_code})")
        return

    soup = BeautifulSoup(response.text, "html.parser") #

    #Oxford uses <span class="def"> for definitions
    definitions = soup.find_all("span", class_="def")

    if not definitions:
        print("No definitions found. Check the spelling or try another word.")
        return

    print(f"Definitions for '{word}':\n")
    for i, deff in enumerate(definitions[:3], 1):  #limit te definitions to 3
        print(f"{i}. {deff.get_text()}")

if __name__ == "__main__" :
    if(len(sys.argv)!=2) :
        print("Usage : py define.py <word>")
        sys.exit(1)
    word = sys.argv[1]
    fetch_definition(word)
