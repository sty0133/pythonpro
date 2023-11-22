text_file = open("./write_it.txt", "w")
text_file.write("Line 1\n")
text_file.write("This is line 2\n")
text_file.write("That makes this line 3\n")
text_file.close()

text_file = open("./write_it2.txt", "w")
lines = ["Line 1\n", "This is line 2\n","That makes this line 3\n"]
text_file.writelines(lines)
text_file.close()