with open("files.txt", "r") as data:
    output = open("output.txt", "a")
    for line in data:
        line = (line.split((" ")))
        output.write(f"https://www.google.com/maps/dir//{str(line)}\n")
