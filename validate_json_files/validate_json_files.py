import os
import sys
import json

def validate_json_files(directory):
    json_files = [ file for file in os.listdir(directory) if file.endswith("json") ]
    
    invalid_files = []
    
    for json_file in json_files:
        with open (json_file, "r") as file:
            content = file.read()
            
            try:
                json.loads(content)
            except ValueError as error:
                print("Invalid json file: {0}. Error: {1}".format(json_file, error))
                invalid_files.append(json_file)
    
    if len(invalid_files) > 0:
        raise Exception("One or more files do not contain JSON data.")
                
if __name__ == "__main__":
    validate_json_files(os.getcwd())
