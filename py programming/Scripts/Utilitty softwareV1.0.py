print("                                             A Basic utillity software!")
def main():
 print("1.Table Printer\n2.Calculator")
 help = input("Enter your choice!: ")
 print("---------------------------------------------------------------------------")
 if "1" in help:
  def table(a):
    
   print("TABLE PRINTER!!")
   num = int(input("Enter the table to be printed: "))

   for _ in range(10):
     a=a+1
     tbl= num*a
     print(tbl)
  
  table(0)
  input()

 if "2" in help:
  print("1.Addition\n2.Subtract\n3.Mutiply\n4.Divide")
  choice = int(input("\nEnter your choice: "))
  print("---------------------------------------------------------------------------")
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

main()

for _ in range(99) :
 exit = input("Do you want to exit?(Y/N) :")

 if  "Y" and "y" in exit:
    quit()

 else:
   print("\n")
   main()
