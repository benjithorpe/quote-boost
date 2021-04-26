# scrape DSTI website for job posts
from bs4 import BeautifulSoup
import requests

dsti_recruitment_page = requests.get("https://www.dsti.gov.sl/recruitment/")
soup = BeautifulSoup(dsti_recruitment_page.text, 'lxml')

job_wrapper = soup.find('div', class_='tatsu-column')

print(job_wrapper.prettify())
# job_titles = soup.find_all()
for job_div in job_wrapper:
    pass

# ====== find links in the button ======
description_link = soup.find_all('div', class_='tatsu-normal-button')

with open("description_links.txt", 'w') as links_file:
    for button in description_link:
        # links_file.write(button.find('a')['href'] + '\n')
        pass
    # print(button.find('a')['href'])
# ======================================


# print(job_wrapper.prettify())

# with open("../../benjithorpe.github.io/index.html", 'r') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')


# # whole_site = soup.find('div')
# links_in_figcaption = soup.find_all('figcaption')
# for figcaption in links_in_figcaption:
#     summary = figcaption.p.text
#     # print(summary, '\n')

# hobies_and_interest = soup.find('section', id='hobbies').ul
# [print(hobby, end='') for hobby in hobies_and_interest.text]
# # print(hobies_and_interest.prettify())
