def txt_file(filename, content):
    try:
        # Write to file
        with open(filename, 'w') as file:
            file.write(content)
        print(f"-> Successfully wrote to {filename}")

        # Read from file
        with open(filename, 'r') as file:
            data = file.read()
        print(f"->Contents of {filename}:\n\n\t{data}")

    except FileNotFoundError:
        print("File not found.")
    except IOError as e:
        print(f"IO ERROR:{e} ")
        
        
txt_file("new2.txt","Hi Welcome to world of Developers")