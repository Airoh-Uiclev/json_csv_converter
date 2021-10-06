import json
import csv
import sys

def process_json_single_dict(example_json):
    # example_json = '{ "col1":[ "val11", "val12"], "col2":[ "val21", "val22"]}'

    example_but_dict = json.loads(example_json)

    # print(example_but_dict["col1"])
    # print(example_but_dict.keys())
    # print(example_but_dict.values())
    # print(list(example_but_dict.values()))

    keys = list(example_but_dict.keys())
    values = list(example_but_dict.values())


    with open('csv_output_single_dict.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ',')
        csv_writer.writerow(keys)

        nr_cols = len(keys)
        # used to determine how many entries the table has by counting the nr of values on a column
        first_col = values[0]
        nr_rows = len(first_col)

        for row_index in range(nr_rows):
            row = []
            for col in range(nr_cols):
                row.append(values[col][row_index])
            csv_writer.writerow(row)

def process_json_dict_array(example_json):
    # example_json = '[ { "col1":"val11", "col2":"val21" }, { "col1":"val12", "col2":"val22" } ]'
    
    example_but_dict_array = json.loads(example_json)

    with open("csv_output_dict_array.csv", 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter = ',')

        col_names = list(example_but_dict_array[0].keys())
        csv_writer.writerow(col_names)

        for dict_entry in example_but_dict_array:
            csv_writer.writerow(dict_entry.values())

if __name__ == "__main__":
    input_json_file_name = sys.argv[1]
    json_format_used = sys.argv[2]
    input_json_str = ""
    
    with open(input_json_file_name, 'r') as input_json_file:
        input_json_str = "".join(input_json_file.readlines())
        print(input_json_str)
        input_json_str = input_json_str.translate(str.maketrans('', '', ' \n\t\r'))
        print(input_json_str)


    if json_format_used == "dict":
        process_json_single_dict(input_json_str)
    elif json_format_used == "array":
        process_json_dict_array(input_json_str)