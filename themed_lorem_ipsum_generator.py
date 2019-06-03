from random import randint

ninja_words = ["Aiki", "Buyu","Chimonjutsu","Cho sen","Dojo","Gakusei","Haibo",
               "Jin","Kenshi","Obake ken","Rakusha","Samaru","Tekkon","Yoko"]

def ninjarize(word):
    random_position = randint(0,len(ninja_words)-1)
    return (word+ninja_words[random_position])

paragraphs = int(input("How many paragraphs of ninja ipsum: "))


with open("ipsum.txt") as original:
    items = original.read().split()   # list of words

    for i in range(paragraphs):
        ninja_words=list(map(ninjarize,items))
        with open("ninjaipsum.txt","a") as ninip:
            ninip.write(' '.join(ninja_words)+'\n\n')
