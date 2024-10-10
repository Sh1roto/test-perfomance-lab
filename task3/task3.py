import json
import sys

def find_value_by_id(values, test_id):
    for item in values:
        if item['id'] == test_id:
            return item['value']
    return None

def fill_test_values(test_structure, values):
    if 'value' in test_structure and test_structure['id']:
        value = find_value_by_id(values, test_structure['id'])
        if value:
            test_structure['value'] = value

    if 'values' in test_structure:
        for subtest in test_structure['values']:
            fill_test_values(subtest, values)

def main(values_file, tests_file, report_file):
    with open(values_file, 'r') as vf:
        values_data = json.load(vf)['values']

    with open(tests_file, 'r') as tf:
        tests_data = json.load(tf)

    for test in tests_data['tests']:
        fill_test_values(test, values_data)

    with open(report_file, 'w') as rf:
        json.dump(tests_data, rf, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <values.json> <tests.json> <report.json>")
        sys.exit(1)

    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    main(values_file, tests_file, report_file)