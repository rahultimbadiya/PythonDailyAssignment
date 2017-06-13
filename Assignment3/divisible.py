def Divisible(main_lst):
    lst = []
    for num in main_lst:
        if num>2000 and num<3000:
            if num % 5 == 0:
                lst.append(num)

    print("The numbers is between 2000 and 3000 with divisible by 5 are:",lst)

main_lst = [2100,1900,2345,2500,2600,2900,2950,3000]
Divisible(main_lst)

