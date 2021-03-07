import requests
from bs4 import BeautifulSoup as bs


def get_pare_name(pare: str):
    pare = pare.strip().split(",")
    res = pare[0] if pare[0] else "pare does not exist"
    if len(pare) > 1:
        res = "".join([i for i in pare if i != pare[0] and i != pare[-1]]).strip()
    return res


group_number = "116"
file_name = "schedule" + group_number + ".txt"
url = "https://profkomstud.khai.edu/schedule/group/" + group_number

response = requests.get(url)

soup = bs(response.text, "html.parser")

table_rows = soup.find("table", class_="table").select("tr")

f = open(file_name, "w")
f.write("")
with open(file_name, "a") as f:
    for row in table_rows:
        if "class" in row.attrs:
            day_name = row.select("td")[1].get_text()
            f.write(day_name + "\n")
        else:
            row_data = row.select("td")
            pare = get_pare_name(row_data[-1].get_text())
            if len(row_data) == 2:
                time = row_data[0].get_text()
                f.write("\t" + time + "\n")
            f.write("\t\t" + pare + "\n")
