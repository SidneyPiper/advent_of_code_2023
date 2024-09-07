import sys
import requests
from bs4 import BeautifulSoup
import os

data = {"Cookie": "session=YOUR_SESSION_COOKIE"}

day = sys.argv[1]

normal_input = requests.get(
    "https://adventofcode.com/2023/day/" + day + "/input", headers=data
)

test_input = requests.get("https://adventofcode.com/2023/day/" + day, headers=data)
soup = BeautifulSoup(test_input.text, "html.parser")
parts = soup.find_all("article", class_="day-desc")
parts = list(map(lambda x: x.select_one("pre code").get_text(), parts))

os.mkdir("./Day " + day)

with open("./Day " + day + "/input.txt", "w") as f:
    f.write(normal_input.text)

with open("./Day " + day + "/test_input.txt", "w") as f:
    f.write(parts[0])

with open("./template.py") as template:
    with open("./Day " + day + "/day" + day + "_2023.py", "w") as f:
        for line in template:
            f.write(line)
