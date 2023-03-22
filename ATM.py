n=str(input("Please enter your name --> "))
print("The Rajpura Branch of CUIET Bank is at your service and This ATM works 24*7")
print("Welcome",n)
print("Please put your card here")
print("This ATM works only in numeric values,Kindly enter respective values of the action you want to perform!!")
while True: 
    a = str(input(" Please Set your 4 digit pin for the transaction ="))
    i = (len(a))
    
    if len(a) > 4 or len(a) <4:
        print("Kindly enter a valid 4 digit code: ")
        continue
    else:
        break
j = str(input("enter your pin ="))
a = int(a)
j = int(j)    
if j == a:
    print("Welcome")
else:
    print(" Please check your pin and try again..You have used your 1/2 tries!")

    j = int(input("Again enter your correct  pin ="))
                
if j== a:
    print("Welcome")
else:
    print("You have entered wrong pin 2 times , Kindly try again after some time..An automated message has been sent to your phone, kindly cooperate and respond if it's not you in the ATM ")
quit()
x='221099023920'
o='986XXXXX02'
 
print("The account registered with the above given pin is => ",x)
print("The contact number of the account holder is =>",o)

print("""Choose Your Account type ==>
      
      
                  (1)Savings account
                  (2)Current account
                  (3)Reccuring Deposit
                  (4)Fixed Deposit
      
      """)
      
v=int(input("Enter your account type==>"))
if v==1:
      print("you have chosen savings account","Please press enter for further progress")
    
if v==2:
      print("you have chosen current account","Please press enter for further progress")

if v==3:
      print("you have chosen reccuring deposit account","Please press enter for further progress")
      
if v==4:
      print("you have chosen fixed deposit account","Please press enter for further progress")
      
else:
    print("Please choose from the above available option")
quit()
m = 50000
print("""                  


                      (1) If you want to check your balance,Kindly put 1 in the dialogue box
                      (2) If you want to deposit money in your account,Kindly put 2 in the dialogue box
                      (3) If you want to withdraw money in your account,Kindly put 3 in the dialogue box
                      


     """)
c = int(input("Enter your desired option="))

if c==1:
    w = 1
    print("your remaining balance",{m})
    new_balance = m

if c==2:
    w = 2
    print("deposit money in your chosen account")
    d = int(input("enter your money deposit ="))
    print("total money in your account after the above deposit",{m+d})
    new_balance = m+d

if c==3:
    w = 3
    print("You have chosen to withdraw money from your chosen account type")
    e = int(input("Enter the amount you want to withdraw="))

    if m<e:
        print("The amount you have requested is more than the balance in your account")
    else:
        print("Your final balance after the above withdrawl transaction",{m-e})
    new_balance = m-e
if c==4:
    print("Kindly choose from the above options")
    
print("Thank You for using CUIET Bank ATM!!")
print("""  


           kindly press Yes for a reciept or No for ending the following transaction,"
                         "(1)Yes"
                         "(2)No"
     
               """)
                                              
r=int(input("Please enter you desired option="))
from datetime import date
today=date.today()
y=("The following transaction was made by the user ~>",n)
print("              ",y)
u=(f"""            TERM ID: CHOD2445
                   
                  LOCATION: CHANDIGARH - CHITKARA UNIVERSITY
                  CARD NO. : 4568XXXXXXXX9076
                  Remaining balance in your account = {new_balance} 
            
                  RECORD NO. :llk 577697
Thank you for using CUIET ATM , Kindly rate our service on our website!!--> www.cuietbank.in!
    
""")
if w==1:
    print("Your remaining balance is: ",{m})
    print("No transaction or deposition of money too place !")
if w ==2:
    print(f"Rs {d}/- has been deposited in your bank account. ")
    print("total money in your account after the above deposit",{m+d})
if w==3:
    print(f"Rs {e}/- amount of money has been withdrawn from your account.")
    print(f"Your final balance after the above transaction is Rs {m-e}/-")
print(today)
if r==1:
          print(u)
if r==2:
    print("Got it! Thank you for saving paper..Thank you for using this ATM , Kindly rate our service on our website "www.chitkarabank.in")
