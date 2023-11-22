text_file = open("./prob2_writeAndRead.txt", "w")
print("Input your string...")
lines = []

def finished():
    # print(lines)
    file_read = open("./prob2_writeAndRead.txt", "r")
    print(f"Your inputs are below..\n{file_read.read()}")
    print(file_read.readlines())
    print(file_read)
    file_read.close()

while True:
    text = input(">> ")
    if text == "Q":
        print("Write process has been finished\n\n")
        text_file.writelines(lines)
        text_file.close
        finished()
        break
    else:
        lines.append(text + "\n")

