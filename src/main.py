from html2image import Html2Image
import os
import pandas as pd
import argparse

def main():
    parser = argparse.ArgumentParser(description="Create Google Form confession images")
    parser.add_argument("--file", "-f", type=str, default="./files/test.xlsx", help="Path of excel file to retrieve data from")
    parser.add_argument("--question", "-q", type=str, help="Set question for form")
    parser.add_argument("--save-path", "-s", "-o", type=str, default="../runs", help="Output path for image(s)")
    parser.add_argument("--model", "-m", type=str, default="mimic.html", help="Path to model html")
    args = parser.parse_args()

    file = args.file
    question = args.question
    save_path = args.save_path
    model_path = args.model

    dirname = os.path.dirname(__file__)

    data = pd.read_excel(os.path.join(dirname, file), sheet_name="Sheet1").to_dict()
    hti = Html2Image(output_path=os.path.join(dirname, save_path))
    html = open(os.path.join(dirname, model_path), "r", encoding="utf8").read()

    try:
        _ = data[question]
    except Exception as e:
        print("\33[33m" + f"Excel column '{question}' was not found. Are you sure you've typed that in correctly, or that it exists?" + "\x1b[0m")
        exit(1)

    count = 0
    for i in data[question]:
        confession = data[question][i]
        new_html = html.replace("your_confession_here", confession)

        hti.screenshot(
            html_str=new_html,
            save_as=f'{count}.png',
            size=(500, 500)
        )

        count += 1

if __name__ == "__main__":
    main()