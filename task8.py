with open("old.txt", "w+") as file:
    file.write("asddddasfsfdfasdfasdfsdfsfasdfasvdsdvavsdvsdv")
    file.close()
with open("old.txt", "r") as file:
    a = file.read()
    print(a)
    a = a[::-1]
with open ('newfile.txt', 'w+') as new_file:
    new_file.write(a)
    file.close()
with open ('newfile.txt', 'r') as new_file:
    b = new_file.read()
    print(b)