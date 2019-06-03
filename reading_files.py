def seq_filter(line):
    return "nova" not in line


with open("Nova.txt")as nova_star:

    for i in nova_star:
     print(i)

     # removes gaps between each line
     print(i.rstrip())



    # readlines () does = reads each line
    # and stores its elements in the list
    """
    seek () in order to return to the first line in the text file, since the previous for loop has move us to the 
    end 
    """
    nova_star.seek(0)

    lines = nova_star.readlines()
    print(lines)

    # read , characters in a particular range using = read()
    nova_star.seek(50)
    file_txt = nova_star.read(100)
    print(file_txt)

    print(list(filter(seq_filter,lines)))
