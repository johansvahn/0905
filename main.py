start = 1980
slut = 1970
year = start
for year in range(1980,1970,-2):
    print("Year is:", year)
    if year == 1972:
        print("Då föddes Stefan")
    elif year == 1973:
        print("Då föddes Foppa")

playGame = True
while playGame == True:
    print("Kör spelet")
    print("Visa highescore")
    inmatning = input("Vill du spela igen J/N")
    if inmatning != "J":
        break

x = 10
while x > 0:
    print("Nu är x ", x)
    x = x -1
print("Klart")
# if age > 6:
#       print("Du går i skolan")
# while KLOCKAN > 9 and KLOCKAN < 16:
#     print("Du går i skolan")
#     print("Hej")
# print("Klart")