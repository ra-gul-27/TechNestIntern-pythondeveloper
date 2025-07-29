import json

def json_file(filename, content=None):
    try:
        if content is not None:
            with open(filename, 'w') as f:
                json.dump(content, f, indent=4)
            print(f"JSON written to {filename}")
        else:
            with open(filename, 'r') as f:
                data = json.load(f)
            print(f"Content of {filename}:\n{data}")
    except Exception as e:
        print("JSON file error:", e)
        
        
data = {"name": "Ragul", "skills": ["Python", "MySQL"]}
json_file("new3.json", data)
json_file("new3.json")
