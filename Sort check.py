#Python
#Javad Razaz Rahmaty
#Check List

sort = True

num = input("\nEnter the Numbers (with space key and ',') = ")

num = num.split(" , ")

num_list = [int(i) for i in num]

for i in range(1 , len(num_list)):
    if num_list[i-1] > num_list[i]:
        sort = False
        break

if sort:
    print("\n\n      ====>>>> The List is Sorted <<<<====")

else:
    print("\n\n      ====>>>> The List is not Sorted <<<<====")
