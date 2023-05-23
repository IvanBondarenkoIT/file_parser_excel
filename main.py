import tabula
import re
import pandas as pd


def read_xlsx(filename: str):
    df = pd.read_excel(filename)
    data_as_list_of_dicts = df.to_dict('records')
    # print(data_as_list_of_dicts)
    for _dict in data_as_list_of_dicts:
        print(_dict)


def read_pdf(filename: str):
    pdf_content = tabula.read_pdf(filename, pages="all")
    text_content = "".join(pdf_content[0])

    all_regex = r"(?<=\rname)(.+?)" \
                r"\rdate(.+?)" \
                r"\rnationality(.+?)" \
                r"\raddress(.+?)" \
                r"\rtel(.+?)" \
                r"\remail(.+?)" \
                r"(\rname|Unnamed: 0)"
    all_matches = re.findall(all_regex,
                             text_content, re.IGNORECASE)

    for match in all_matches:
        print(match)


def main():
    # read_pdf("data_pdf.pdf")
    read_xlsx("data.xlsx")



if __name__ == '__main__':
    main()

