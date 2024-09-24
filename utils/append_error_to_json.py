import json
import pandas as pd
import numpy as np


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def load_csv(file_path):
    return pd.read_csv(file_path)


def add_errors_to_json(json_data, csv_data):
    for index, row in csv_data.iterrows():
        box_id = row['Box_ID']
        keypoint_id = row['KeyPointID']
        problem = row['Problem']
        image_name = row['Image_name']

        error_entry = {
            'problem': problem,
            'box_id': int(box_id) if not np.isnan(box_id) else None,
            'keypoint_id': int(keypoint_id) if not np.isnan(keypoint_id) else None
        }

        # If image_name is present in JSON, find its annotations
        for annotation in json_data['annotations']:
            # Match based on Box_ID and Image_name in the CSV
            if (annotation['image_id'] == image_name):
                # Initialize errors if they don't exist
                if 'errors' not in annotation:
                    annotation['errors'] = []
                annotation['errors'].append(error_entry)

    return json_data


def save_json(file_path, json_data):
    with open(file_path, 'w') as f:
        json.dump(json_data, f, indent=4)


def main(json_file, csv_file, output_json_file):
    json_data = load_json(json_file)
    csv_data = load_csv(csv_file)

    updated_json_data = add_errors_to_json(json_data, csv_data)

    save_json(output_json_file, updated_json_data)
    print(f"Updated JSON saved to {output_json_file}")


json_file_path = './test.json'
csv_file_path = './test.csv'
output_json_file_path = './result.json'

main(json_file_path, csv_file_path, output_json_file_path)
