print("calculator\n")
print("1.addition\n2.sutract\n3.mutiply\n4divide\nchoose from 1 - 4")
choice = int(input("\n\nenter your choice: "))

if choice == 1:
   num_1 = float(input("enter first number="))
   num_2 = float(input("enter second number="))

   sum = num_1 + num_2
   print("sum:",sum)
   input("")

elif choice == 2 :
   num_1 = float(input("enter first number="))
   num_2 = float(input("enter second number="))

   dif = num_1 - num_2
   print("dif:",dif)
   input("")

elif choice == 3 :
   num_1 = float(input("enter first number="))
   num_2 = float(input("enter second number="))

   multi = num_1 * num_2
   print("multiplication:",multi)
   input("")

elif choice == 4 :
   num_1 = float(input("enter first number="))
   num_2 = float(input("enter second number="))

   divi = num_1 / num_2
   print("division:",divi)
   input("")
