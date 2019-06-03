with open("writing.txt","w") as wfile :
    wfile.write("No angels in our heaven")

# ammends text to file , so no overwrites
with open('writing.txt',"a")as wfile:
    wfile.write("\nNo they are not natural")

quotes = ["see ya later baby","\na silent poem asylum","\nno justice for the righteous"]

# using as a for loop
wfile_list = []

# for i in quotes:
#     wfile_list.append(i)
# print(wfile_list)
#
# with open("writing.txt", "a") as wfile :
#     wfile.write(str(wfile_list))

"""
writelines expects lines as argument
"""
with open ("writing.txt","a") as wfile:
    wfile.writelines(quotes)