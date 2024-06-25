import json
import os

print('''
                _  _____  ____  _   _           
               | |/ ____|/ __ \| \ | |          
               | | (___ | |  | |  \| |          
           _   | |\___ \| |  | | . ` |          
          | |__| |____) | |__| | |\  |          
   _____ _ \____/|_____/ \____/|_|_\_|__ _____  
  / ____| |  | | |  | | \ | | |/ /  ____|  __ \ 
 | |    | |__| | |  | |  \| | ' /| |__  | |__) |
 | |    |  __  | |  | | . ` |  < |  __| |  _  / 
 | |____| |  | | |__| | |\  | . \| |____| | \ \ 
  \_____|_|  |_|\____/|_| \_|_|\_\______|_|  \_\
                                              
''')

print("------ Developed by uj4 | https://uj4.dev/ ------")
print("")

data_folder = 'Data'
json_files = [f for f in os.listdir(data_folder) if f.endswith('.json')]

if not json_files:
    print("Unable to locate json files, please put your files in the Data folder...")
    print("Make sure they end with .json | e.g. data.json")
    exit()
else:
    print("Located the following json files:")
    for idx, file_name in enumerate(json_files, start=1):
        print(f"{idx}. {file_name}")

    while True:
        try:
            file_index = int(input("Please enter the number of the JSON file to process: ")) - 1
            if file_index < 0 or file_index >= len(json_files):
                raise ValueError("Invalid file index | Please enter a valid number.")
            break
        except ValueError as e:
            print(e)
    
    selected_file = os.path.join(data_folder, json_files[file_index])

    while True:
        try:
            entries_per_file = int(input("Please enter how many JSON entries you want to chunk: "))
            if entries_per_file <= 0:
                raise ValueError("Number of entries per file must be great than zero.")
            break
        except ValueError as e:
            print(e)

    output_directory = 'Output'

def chunkin(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def write_chunks(data, chunk_size, output_dir, file_pref):
    os.makedirs(output_dir, exist_ok=True)

    for idx, chunk in enumerate(chunkin(data, chunk_size)):
        file_name = os.path.join(output_dir, f'{file_pref}_chunk_{idx+1}.json')
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(chunk, f, indent=2)

def run(input_file, entries_per_file, output_directory):
    file_pref = os.path.splitext(os.path.basename(input_file))[0]
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    write_chunks(data, entries_per_file, output_directory, file_pref)

run(selected_file, entries_per_file, output_directory)