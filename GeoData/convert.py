with open("convert.txt", "r") as data:
    output = open("output.txt", "a")
    for line in data:
        line = (line.split(("\t")))
        output.write(f"https://www.google.com/maps/dir//{str(line)}\n")
