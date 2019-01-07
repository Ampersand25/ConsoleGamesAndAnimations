#A program that selects from "words_list.txt" the words that have cont letters or even more
f = open("words_list.txt","r")
g = open("results.txt","w")
cont = int(input())
for line in f:
    str = line
    if len(str) > cont:
        g.write(str)
f.close()
g.close()
