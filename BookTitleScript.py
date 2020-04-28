import os
import re #regex

l_temp = os.listdir(path='C:\\Downloads\\Springer Ebooks\\') #replace with the path of the folder on your own pc
l_bookTitle = []

for title in l_temp:
    if title[0:4].isnumeric():
        if title[5:10] == 'Book_':
            if title[-4:] == 'epub':
                l_bookTitle.append(re.sub(r"(\w)([A-Z])", r"\1 \2", title[10:-5])) #remove .epub from name, add spacing between uppercase letters and add to list
            else:
                l_bookTitle.append(re.sub(r"(\w)([A-Z])", r"\1 \2", title[10:-4])) #remove .pdf from name, add spacing between uppercase letters and add to list

l_bookTitle = list(dict.fromkeys(l_bookTitle)) #remove duplicates

l_bookTitle.sort() #sort by alphabetical order


file = open('BookTitles.txt','w')

for title in l_bookTitle:
    file.write(title + '\n')

file.close()

