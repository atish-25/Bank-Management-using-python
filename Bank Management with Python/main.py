import json
import random
import string
from pathlib import Path

class Bank:
    database ='database.json'
    data=[]
    try:
        if Path(database).exists():
            with open(database,'r') as fs:
                data = json.loads(fs.read())
        else:
            print("no such file exist")
    except Exception as err:
        print(f"an exception occured as {err}")
        
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs :
            fs.write(json.dumps(Bank.data))
        
    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
   
        
    def Createaccount(self):
        
        info= {
            "name": input("Tell your name: "),
            "age": int(input("Tell your age: ")),
            "email": input("Tell your email: "),
            "pin": int(input("tell your 4 no. pin: ")),
            "accountNo.": Bank.__accountgenerate(),
            "balance": 0
            
        }
        
        if info['age']<18 or len(str(info['pin'])) !=4:
            print("sorry you cannot create account")
        else:
            print("Account created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down you account number")
            
            
            
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin: "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if not userdata:
            print("Sorry no data found")
            
        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount > 10000 or amount < 0:
                print("Sorry the amount is too high, you can deposit below 10000 and above 0")
            else:
                
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")
        

    
    def withdrawmoney(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin: "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Sorry no data found")
            
        else:
            amount = int(input("Enter the amount you want to withdraw: "))
            if userdata[0]['balance'] < amount :
                print("Sorry not sufficient balance")
            else:
            
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully")
                
    def showdetails(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin: "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        print("Your details are ")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def updatedetails(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin: "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Sorry no data found")
            
        else:
            print("you cannot change the age,account number,balance")
            
                
            print("Enter the details you want to update")
            newdata = {
                "name" : input("Name: "),
                "email":input("Email: "),
                "pin" : input("Pin: "),
            
            }
            if newdata["name"] =="":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] =="":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] =="":
                newdata["pin"] = userdata[0]['pin']
                
            newdata['age'] = userdata[0]['age']
            
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']
            
            # if newdata['pin'] == str:
            #     newdata['pin'] = int(newdata['pin'])
            if isinstance(newdata['pin'], str):
                newdata['pin'] = int(newdata['pin'])
 
                
                
                
            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]
                
            Bank.__update()
            print("Details updated successfully")
            
            
    def Delete(self):
        accnumber = input("Please tell your account number : ")
        pin = int(input("Please tell your pin: "))
        
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        
        if userdata == False:
            print("Sorry no data found")
        else:
            check = input("Press Y if you want to delete account or Press N")
            if check == 'n' or check == 'N':
                print("Account not deleted")
            else :
                index = Bank.data.index(userdata[0]) 
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()      
            
          
user = Bank()
print("Press 1 for creating an account")
print("Press 2 for depositing the money in bank")
print("Press 3 for withdrawing the money from bank")
print("Press 4 for details")
print("Press 5 for updating the details")
print("Press 6 for deleting the account")
check = int(input("Enter your choice: "))


if check == 1:
    user.Createaccount()
    
if check ==2:
    user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()
