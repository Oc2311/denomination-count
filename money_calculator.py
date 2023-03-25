def count():
    one=float(input("Enter the number of notes of 2000rs: "))
    # value=int(input("Enter the value of the note/coins you have entered: "))
    total1=one*2000
    # print(f"{one} notes of 2000 rupees = {total1}")
    # gap

    one=float(input("Enter the number of notes of 500rs: "))
    # value=int(input("Enter the value of the note/coins you have entered: "))
    total2=one*500
    # print(f"{one} notes of 500 rupees = {total2}")
    # Gap
    one=float(input("Enter the number of notes of 200rs: "))
    # value=int(input("Enter the value of the note/coins you have entered: "))
    total3=one*200
    # print(f"{one} notes of 200 rupees = {total3}")
    # Gap
    one=float(input("Enter the number of notes of 100rs: "))
    # value=int(input("Enter the value of the note/coins you have entered: "))
    total4=one*100
    # print(f"{one} notes of 100 rupees = {total4}")





    print(f"{one} notes of 2000 rupees = {total1}")
    print(f"{one} notes of 500 rupees = {total2}")
    print(f"{one} notes of 200 rupees = {total3}")
    print(f"{one} notes of 100 rupees = {total4}")
    gtotal=total1+total2+total3+total4
    if gtotal>=100000:
        print(f"Total Cash available is {gtotal} Lakh Rupees Only")
    elif gtotal<1000:
        print(f"Total Cash available is {gtotal} Hundred Rupees Only")
    elif gtotal>=1000:
        print(f"Total Cash available is {gtotal} Thousand Rupees Only")
    else:
        print("Please Check the given inputs.")



count()