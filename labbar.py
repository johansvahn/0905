# print("Mata in två tal:")
# tal1 = int(input(""))
# tal2 = int(input(""))

# if tal1 > tal2: # 10, 2
#     for tal in range(tal1,tal2, -1):
#         print(tal)
# elif tal1 < tal2: # 2, 10
#     for tal in range(tal1, tal2):
#         print(tal)

svar = True
while svar == True:
    print("Mata in två tal")
    tal1 = int(input(""))
    tal2 = int(input(""))
    print(tal1 + tal2)
    print("Vill du fortsätta(J/N)?")
    svar = input("")
    if svar == "J":
        svar = True
    elif svar == "N":
        break

# print("Mata in två tal:")
# tal1 = int(input(""))
# tal2 = int(input(""))

# if tal1 > tal2:
#     while aktuellTal < tal2:
#         print(aktuellTal)
#         aktuellTal = aktuellTal + 1
# elif tal1 < tal2:
#     while aktuellTal > tal2:
#         print(aktuellTal)
#         aktuellTal = aktuellTal + 1