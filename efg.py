import csv

def csv_file(filename, content=None):
    try:
        if content is not None:
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(content)  # content should be a list of lists
            print(f"CSV written to {filename}")
        else:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                print(f"Content of {filename}:")
                for row in reader:
                    print(row)
    except Exception as e:
        print("CSV file error:", e)

data=[["ALEN"],["Alice"],["Elvin"]]
csv_file("new2.csv",data)
csv_file("new2.csv")