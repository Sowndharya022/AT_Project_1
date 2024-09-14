# utils/result_writer.py
import os
import pandas as pd
from datetime import datetime

print("Pandas version:", pd.__version__)


def update_test_result(test_id, result, tester_name):
    file_path = 'data/test_result.csv'

    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_exists = os.path.isfile(file_path)
    headers = ['Test ID', 'Test Result', 'Date', 'Time', 'TesterName']

    if not file_exists:
        df = pd.DataFrame(columns=headers)
        df.to_csv(file_path, index=False)

    try:
        # Load the existing data from the CSV file
        df = pd.read_csv(file_path)

        if 'TesterName' not in df.columns:
            df['TesterName'] = ''

        # Update the test result
        if test_id in df['Test ID'].values:
            df.loc[df['Test ID'] == test_id, 'Test Result'] = result
            df.loc[df['Test ID'] == test_id, 'Date'] = datetime.now().strftime('%Y-%m-%d')
            df.loc[df['Test ID'] == test_id, 'Time'] = datetime.now().strftime('%H:%M:%S')
            df.loc[df['Test ID'] == test_id, 'TesterName'] = tester_name
        else:
            # Add a new row if Test ID is not found
            new_row = pd.DataFrame(
                [{'Test ID': test_id, 'Test Result': result, 'Date': datetime.now().strftime('%Y-%m-%d'),
                  'Time': datetime.now().strftime('%H:%M:%S'), 'TesterName': tester_name}])
            df = pd.concat([df, new_row], ignore_index=True)

        # Write the updated data back to the CSV file
        df.to_csv(file_path, index=False)
        print(f"Test result for '{test_id}' has been updated successfully.")

    except Exception as e:
        print(f"Error updating test result: {e}")
        raise
