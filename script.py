import requests
from bs4 import BeautifulSoup
import json

doi = "10.1007/s11104-013-1678-0"
url = f"https://doi.org/{doi}"

# Follow redirect to publisher
resp = requests.get(url, allow_redirects=True, headers={"User-Agent": "Mozilla/5.0"})
resolved_url = resp.url

# Fetch the publisher page
html = requests.get(resolved_url, headers={"User-Agent": "Mozilla/5.0"}).text
soup = BeautifulSoup(html, "html.parser")

# Extract JSON-LD Schema.org
schema_data = []
for script in soup.find_all("script", type="application/ld+json"):
    try:
        data = json.loads(script.string)
        schema_data.append(data)
    except Exception:
        pass

print(json.dumps(schema_data, indent=2))
