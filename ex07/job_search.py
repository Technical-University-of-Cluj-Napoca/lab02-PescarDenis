import sys
import requests
from bs4 import BeautifulSoup

def fetch_jobs(word: str):
    base_url = "https://www.juniors.ro/jobs?q=" # base url
    url = base_url + word.lower().strip() #create each url for the given programming language
    
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

    soup = BeautifulSoup(response.text, "html.parser") 

    #same code above forom ex 06 

    jobs = soup.find_all("li", class_="job") # we find each job in here
    results = [] # make a list for the found jobs

   
    for job in jobs[:7]:  # Limit to top 7

        # title is inside <div class="job_header_title"><h3>Title</h3>>
        header_title = job.find("div", class_="job_header_title")

        #if the title header exists and also the h3 section exists get the job title else print N/A
        if(header_title and header_title.find("h3")) :
            title = header_title.find("h3").get_text() 
        else :
            title = "N/A" # not available

        #get the location as it is on level below h3 in the strong, but in the same job header title
        if(header_title and header_title.find("strong")) :
            text = header_title.find("strong").get_text(strip = True) # get the full text
            parts = [p.strip() for p in text.split("|")] # split the text into parts as they are separated by an |

            location = parts[0]  
            date_posted = parts[1]  
        else :
            location = "N/A" # not available
            date_posted = "N/A"

        # Company: inside <ul class="job_requirements"><strong>Companie:</strong> UiPath</li>
        company_header = job.find("ul", class_="job_requirements")
        if company_header:
            strong_header = company_header.find("strong")
            if strong_header and "Companie" in strong_header.get_text():
                company = strong_header.next_sibling.strip() if strong_header.next_sibling else "N/A"
            else:
                company = "N/A"
        else:
            company = "N/A"

        # Technologies (if any)
        tags_section = job.find("ul", class_="job_tags")
        technologies = []
        if tags_section:
            tags = tags_section.find_all("li")
            technologies = [t.get_text(strip=True) for t in tags if t.get_text(strip=True)]

        results.append({
            "title": title,
            "company": company,
            "location": location,
            "date_posted" : date_posted,
            "technologies": technologies
        })

    return results

def print_jobs(jobs):
    if not jobs:
        print("No job listings found.")
        return

    for i, job in enumerate(jobs, start=1):
        print(f"\n{i}. {job['title']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['location']}")
        print(f"Date posted: {job['date_posted']}")
        if job['technologies']:
            print(f"Technologies: {', '.join(job['technologies'])}")
        else:
            print("Technologies: N/A")


def main():
    if len(sys.argv) < 2:
        print("Usage: py job_search.py <programming_language>")
        sys.exit(1)

    programming_language = sys.argv[1]
    jobs = fetch_jobs(programming_language)
    print_jobs(jobs)


if __name__ == "__main__":
    main()
