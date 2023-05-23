import tabula
import re


def main():
    pdf_content = tabula.read_pdf("data_pdf.pdf", pages="all")
    text_content = "".join(pdf_content[0])
    # print(text_content)

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


if __name__ == '__main__':
    main()

