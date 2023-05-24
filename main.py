import pandas as pd
import data_manager as dm


CSV_FILE_PATH = 'result_csv_file.csv'
EXCEL_FILE_PATH = 'data.xlsx'
SHEET_NAME = 'Basic Worksheet'


def read_xlsx(filename: str):
    df = pd.read_excel(filename)
    data_as_list_of_dicts = df.to_dict('records')
    return data_as_list_of_dicts


def main():
    data_interpreter = dm.DataInterpreter()
    for record in read_xlsx(EXCEL_FILE_PATH):
        print(record)
        data_interpreter.add_data(record)

    df = pd.DataFrame(data_interpreter.get_final_values())
    df.to_csv(CSV_FILE_PATH, index=False)

    df = pd.DataFrame(data_interpreter.get_not_valid_data())
    df.to_csv("not_valid_data.csv", index=False, header=False)


if __name__ == '__main__':
    main()

