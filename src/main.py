from html2image import Html2Image
import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

dirname = os.path.dirname(__file__)

data = pd.read_excel(os.path.join(dirname, r".\files\test.xlsx"), sheet_name="Sheet1")

hti = Html2Image(output_path=os.path.join(dirname, "runs"))
hti.screenshot(
    html_file=os.path.join(dirname, "mimic.html"),
    save_as='woah.png',
    size=(500, 500)
)