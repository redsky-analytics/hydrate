#%%
import json
import requests
from bs4 import BeautifulSoup
from pathlib import Path

url = "https://docs.python.org/3.12/py-modindex.html"
print(url)

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

modules = []
for row in soup.find_all("tr")[1:]:  # Skip the header row
    if row.find("code", class_="xref"):
        module = row.find("code", class_="xref").text.strip().split(".")[0]
        modules.append(module)

modules = list(dict.fromkeys(modules))
print(json.dumps(modules))
Path('stdlib/python3.12.json').write_text(json.dumps(modules))