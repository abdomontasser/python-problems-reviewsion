# # Exercise 1.1

# """
# Expected Output:
# Temperature Converter
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# Choose conversion (1-4): 1
# Enter temperature: 25
# 25.0°C = 77.0°F
# """




# # while True:
# #     print("select which option you need to convert to")

# #     print("1 . Celsius to Fahrenheit \n 2 .  Fahrenheit to Celsius \n 3 . Celsius to Kelvin  \n  4. Kelvin to Celsius \n 5. Enter 5 for exit : ")

# #     choice = int(input("Enter your choice : "))

# #     user_temp = float(input("Please enter the user degress to convert it to selected option :  "))


# #     def convert_Cel_to_Fah(cel):
# #         return (cel * 1.8) + 32
    
# #     def convert_Fah_to_Cel(fah):
# #         return (5/9) * (fah-32)


# #     def convert_Cel_to_Kel(cel):
# #          return cel + 273.15
        


# #     def convert_Kel_to_Cel(kel):
# #         return kel - 273.15


    
# #     match choice:
# #         case 1 :
# #             print(f"{user_temp} = {convert_Cel_to_Fah(round(user_temp,2))}")

# #         case 2 : 
# #             print(f"{user_temp} = {convert_Fah_to_Cel(user_temp)}")
        
# #         case 3 : 
# #             print(f"{user_temp} = {convert_Cel_to_Kel(round(user_temp,2))}")

# #         case 4 : 
# #             print(f"{user_temp} = {convert_Kel_to_Cel(user_temp)}")
        
# #         case 5 : 
# #             print("Good bye :)")
# #             break

# #         case _ :
# #             print("invalid input")

# # *********************************************************

# # Exercise 1.2: List Manipulator

# # user_list = input("Enter a numbers separted : ").split()

# # converted_nums = [int(num) for num in user_list]

# # num_sum = sum(converted_nums)
# # avg = num_sum / len(converted_nums)
# # max_value = max(converted_nums)
# # min_value = min(converted_nums)
# # sorted_nums = sorted(converted_nums)
# # even_nums = [num for num in converted_nums if num %2 ==0]
# # odd_nums = [num for num in converted_nums if num %2!=0 ]


# # print(f"sum = {num_sum} \n  Average = {avg} \n Max = {max_value} \n Min = {min_value} \n sorted = {sorted_nums} \n ")
# # print(f" Even numbers {even_nums} \n odd number {odd_nums} \n")

# # ***************************************************************************

# # Exercise 1.3: String Pattern Analyzer 

# # user_input = input("Enter a string to analyze it : ")

# # freq = {}

# # for c in user_input:
# #     if c in freq:
# #         freq[c] +=1
# #     else:
# #         freq[c] = 1

# # commonlist = []
# # for c,v in freq.items():
# #     if v > 1:
# #         commonlist.append(c)

# # Total_char_with_spaces = len(user_input)
# # Total_char_without_spaces = len(user_input.replace(" ",""))
# # Total_words = len(user_input.split())
# # MostCommon_chars = commonlist
# # Isplaindrome = user_input == user_input[::-1]
# # reverse_input = user_input[::-1]


# # print(f"Total characters  {Total_char_with_spaces} ")
# # print(f"Total characters (Witout spaces) {Total_char_without_spaces}")
# # print(f"Total words {Total_words}")
# # print(f"Character frequency {freq}")
# # print(f"Is palindrome {Isplaindrome}")
# # print(f"Reversed {reverse_input}")
# # print(MostCommon_chars)


# # *************************************************************


# # Exercise 1.4: Number Guessing Game

# # import random

# # print("Welcome to Number Guessing Game : ")

# # print("I am Thinking of a number between 1 and 100 : ")

# # attempts = 7

# # print(f"your have {attempts} ")
# # number_to_guess = random.randint(1,100)
# # import random

# # print("Welcome to the Number Guessing Game!")

# # while True:
# #     number_to_guess = random.randint(1, 100)
# #     attempts = 7
# #     print("\nI'm thinking of a number between 1 and 100.")
# #     print(f"You have {attempts} attempts!")

# #     while attempts > 0:
# #         user_guess = int(input("Your guess: "))

# #         if user_guess < number_to_guess:
# #             attempts -= 1
# #             print(f"Too low! Try again. Attempts left: {attempts}")
# #         elif user_guess > number_to_guess:
# #             attempts -= 1
# #             print(f"Too high! Try again. Attempts left: {attempts}")
# #         else:
# #             print(f" Congratulations! You guessed it with {attempts} attempts remaining!")
# #             break

# #     if attempts == 0 and user_guess != number_to_guess:
# #         print(f" Out of attempts! The number was {number_to_guess}.")

# #     play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
# #     if play_again != "yes":
# #         print("Thanks for playing! Goodbye ")
# #         break


# # ************************************************************************

# # item = {}  

# # while True:
# #     print("\nShopping Cart Menu")
# #     print("1. Add item")
# #     print("2. Remove item")
# #     print("3. Update quantity")
# #     print("4. View cart")
# #     print("5. Checkout")
# #     print("6. Exit")

# #     choice = int(input("Choice: "))

# #     def addItem():
# #         itemName = input("Item name: ")
# #         price = float(input("Enter product price: "))
# #         quantity = int(input("Enter product quantity: "))
# #         item[itemName] = {"price": price, "qty": quantity}
# #         print("✅ Product added successfully!")

# #     def removeItem():
# #         name = input("Enter the item name to remove: ")
# #         if name in item:
# #             del item[name]
# #             print(" Item removed successfully.")
# #         else:
# #             print(" Item not found in cart.")

# #     def updateQuantity():
# #         name = input("Enter the item name to update: ")
# #         if name in item:
# #             new_qty = int(input("Enter new quantity: "))
# #             item[name]["qty"] = new_qty
# #             print("Quantity updated successfully.")
# #         else:
# #             print("Item not found.")

# #     def viewCart():
# #         print("\n--- Cart Summary ---")
# #         if not item:
# #             print("Your cart is empty.")
# #         else:
# #             for key, value in item.items():
# #                 print(f"Item Name: {key}")
# #                 print(f"Price: {value['price']}")
# #                 print(f"Quantity: {value['qty']}")
# #                 print("-" * 30)

# #     def checkout():
# #         subTotal = 0
# #         Discount = 0
# #         for key, value in item.items():
# #                subTotal+=value['price']
# #                print(f"subtotal {subTotal} $")
# #                if subTotal > 100:
# #                    Discount = subTotal*0.10
# #                    print(f"Discount : {Discount}")
# #         print(f"total : {subTotal- Discount}")
              


# #     match choice:
# #         case 1:
# #             addItem()
# #         case 2:
# #             removeItem()
# #         case 3:
# #             updateQuantity()
# #         case 4:
# #             viewCart()
# #         case 5:
# #             checkout()
# #         case 6:
# #             break


# # **********************************************************************************


# # Exercise 1.6: Contact Book Manager

# # def AddContact():
# #     user_data = input("Enter your name, phone, email: ").split(",")
# #     with open("file.txt", "a", newline='|') as f:
# #         f.write(",".join(user_data) + "|")

# # def Viewall():
# #     with open("file.txt", "r") as f:
# #         data = f.readlines()
# #         for line in data:
# #             print(line.strip())

# # def DeletContact():
# #     contact_to_delete = input("Enter the contact name to delete: ").strip()
# #     found = False
# #     with open("file.txt", "r") as f:
# #         data = f.readlines()
# #     with open("file.txt", "w") as f:
# #         for line in data:
# #             name, phone, email = line.strip().split("|")
# #             if name.lower() != contact_to_delete.lower():
# #                 f.write(line)
# #             else:
# #                 found = True
# #     if found:
# #         print("Contact deleted successfully.")
# #     else:
# #         print("Contact not found.")

# # def UpdateContact():
# #     name_to_update = input("Enter the name of the contact to update: ").strip()
# #     with open("file.txt", "r") as f:
# #         lines = f.readlines()

# #     with open("file.txt", "w") as f:
# #         for line in lines:
# #             name, phone, email = line.strip().split("|")
# #             if name.lower() == name_to_update.lower():
# #                 print("Enter new details (leave blank to keep the old one):")
# #                 new_name = input(f"New name [{name}]: ").strip() or name
# #                 new_phone = input(f"New phone [{phone}]: ").strip() or phone
# #                 new_email = input(f"New email [{email}]: ").strip() or email
# #                 f.write(f"{new_name},{new_phone},{new_email}\n")
# #             else:
# #                 f.write(line)

# # while True:
# #     print("\n1. Add Contact")
# #     print("2. View all Contacts")
# #     print("3. Delete Contact")
# #     print("4. Update Contact")
# #     print("5. Exit")

# #     choice = int(input("Choice: "))

# #     match choice:
# #         case 1:
# #             AddContact()
# #         case 2:
# #             Viewall()
# #         case 3:
# #             DeletContact()
# #         case 4:
# #             UpdateContact()
# #         case 5:
# #             break
# #         case _:
# #             print("Invalid choice. Try again.")

# # *****************************************************************************

