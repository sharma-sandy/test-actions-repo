import os
import subprocess

print(os.environ)

all_errors_list = []
fileandfolders = os.listdir()

# file check errors
if ".gitignore" not in fileandfolders:
    all_errors_list.append({"type": "main", "filename":".gitignore", "message":"Missing gitignore"})
    
if "README.md" not in fileandfolders:
    all_errors_list.append({"type": "main", "filename":"README.md", "message":"Missing README"})
    
if any( item not in fileandfolders for item in ["env.yml", "environment.yml"]):
    all_errors_list.append({"type": "main", "filename":"env.yml", "message":"Missing Environment yml file"})


# Get flake8 error report
output = subprocess.run(["flake8", "test.py"], capture_output=True)
stdout_string = output.stdout.decode('UTF-8')
errors_list = stdout_string.split("\n")
for err in errors_list:
    if len(err) == 0:
        continue
    error_content_list = err.split(":")
    error_data = {}
    error_data['type'] =  "file"
    error_data['filename'] =  error_content_list[0]
    error_data['row'] =  error_content_list[1]
    error_data['col'] =  error_content_list[2]
    error_data['message'] =  error_content_list[3].strip()
    all_errors_list.append(error_data)
print(all_errors_list)

