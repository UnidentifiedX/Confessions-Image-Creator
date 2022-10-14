from html2image import Html2Image
import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

dirname = os.path.dirname(__file__)

data = pd.read_excel(os.path.join(dirname, r".\files\test.xlsx"), sheet_name="Sheet1").to_dict()

hti = Html2Image(output_path=os.path.join(dirname, "../runs"))

html = open(os.path.join(dirname, "mimic.html"), "r", encoding="utf8").read()

count = 0
for i in data['your confession ^^']:
    confession = data["your confession ^^"][i]
    new_html = html.replace("your_confession_here", confession)

    hti.screenshot(
        html_str=new_html,
        save_as=f'{count}.png',
        size=(500, 500)
    )

    count += 1