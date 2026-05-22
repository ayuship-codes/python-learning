year = int(input("Enter the year: "))

if year%100==0 and year%400==0 :                                  #if year%100==0 and year%4==0
    print(f"Yes, year {year} is a leap year.")
elif year%100!=0 and year%4==0:
    print(f"Yes, year {year} is a leap year.")
else:
    print(f"No,year {year} is not a leap year.")
