import json

# Read data from TXT file
with open(r'D:\gg\lou\Dont Look Up (2021) [2160p] [4K] [WEB] [5.1] [YTS.MX]\data.txt', 'r') as file:
    data_lines = file.readlines()

# Parse data and create a list of lists
data_list = []
for line in data_lines:
    question, answer = line.strip().split('\t')
    data_list.append([question, [answer]])

# Convert list of lists to JSON
json_data = json.dumps(data_list, indent=4)  # Indent for pretty formatting

# Write JSON data to a file
with open(r'D:\gg\lou\Dont Look Up (2021) [2160p] [4K] [WEB] [5.1] [YTS.MX]\data.json', 'w') as json_file:
    json_file.write(json_data)

print("Conversion completed. Data has been saved to data.json.")
