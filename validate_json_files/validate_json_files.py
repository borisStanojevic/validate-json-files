import os
import sys
import json

def validate_json_files(directory):
    json_files = [ file for file in os.listdir(directory) if file.endswith("json") ]
    
    number_of_invalid_files = 0
    
    for json_file in json_files:
        with open(json_file, "r") as file:
            content = file.read()
            
            try:
                json.loads(content)
            except ValueError as error:
                print("Invalid json file: {0}. Error: {1}".format(json_file, error))
                number_of_invalid_files += 1
    
    if number_of_invalid_files > 0:
        raise Exception("One or more files do not contain valid JSON.")
                
if __name__ == "__main__":
    validate_json_files(os.getcwd())
