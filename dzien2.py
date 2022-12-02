import random

prezenty = ["Perfume", "Socks", "Sweater", "Cup", "Hat", "Tea", "Coffee", "Clock", "Bag", "Book", "Wallet", "Cream", "Earrings"]
p = (random.sample(prezenty,3))

prezent1=p[0]
prezent2=p[1]
prezent3=p[2]

listToStr_1 = ''.join(map(str, prezent1))
listToStr_2 = ''.join(map(str, prezent2))
listToStr_3 = ''.join(map(str, prezent3))


n = input("Tell me your name: ")
print("Hello " + n + " Your presents this year are: " + listToStr_1 + ", " + listToStr_2 + ", " + listToStr_3  + " . Marry Christmas" )
