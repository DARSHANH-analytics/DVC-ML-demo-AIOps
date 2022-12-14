from genericpath import exists
import yaml
import os
import json

def read_yaml(path_of_yaml_file:str) -> dict:
    with open(path_of_yaml_file) as yaml_file:
        content = yaml.safe_load(yaml_file)
    return content

def create_directory(dirs):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        print(f"directory is created at {dir_path}")

def save_local_df(data, data_path, index_status=False):
    data.to_csv(data_path, index=index_status)
    print(f"data is saved at {data_path}")

def save_reports(report: dict, report_path: str, indentation=4):
    with open(report_path, "w") as f:
        json.dump(report, f, indent=indentation)
    print(f"reports are saved at {report_path}")