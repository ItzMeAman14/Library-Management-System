import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client.IT
coll = db.LMS
cursor = coll.find({})

while(True):

    print("*******************************************\n")
    print("Enter 1 for entry\n")
    print("Enter 2 for display\n")
    print("Enter 3 for any change\n")
    print("Enter 4 to convert your data in excel\n")
    print("Enter 5 for exit\n")
    print("*******************************************\n")

    while True:
        try:
            choice = int(input("Enter your Choice:"))
            break
        except:
            print("\x1b[31mInvalid Value Entered.Try Again...")
            print("\x1b[0m")

    print("*--------*--------*\n")
    
    if(choice == 1):
        try:
            id = int(input("Enter Book id:"))
            bn = input("Enter Book Name:")
            an = input("Enter Author Name:")
            iss = input("Enter Your Name:")
            bp = int(input("Enter Book's Price:"))
            data_to_send = {"Book Id":id,"Book Name":bn,"Author Name":an,"Issued By":iss,"Price":bp}
            coll.insert_one(data_to_send)

            print("\n")
            print("\x1b[32mData Stored SuccessFully...")
            print("\x1b[0m")
        except:
            print("\x1b[31mEnter Valid Data........")
            print("\x1b[0m")    

    elif(choice == 2):
            df = pd.DataFrame(coll.find({}))
            print(df)
    
    elif(choice == 3):
        while True:
            print("Enter 1 to change a single data\n")
            print("Enter 2 to delete the whole row\n")
            print("Enter 3 to go back\n")
            print("**********************************************************\n")
            print("Note:You cannot undo changes so write index carefully.\n")
            print("**********************************************************\n")
            try:
                inchoice = int(input("Enter what you want to do:"))
            except:
                print("\x1b[31mInvalid Value Entered.Try Again...")
                print("\x1b[0m")
            print("*---------*--------*----------*\n")
            if(inchoice == 1):
                print(df)
                try:
                    change = input("What you want to change(Column):")
                    id_update = int(input("Enter id:"))
                    newData = input("Enter new data:")
                    coll.find_one_and_update({"Book Id":id_update},{"$set":{change:newData}})

                    print("\n")
                    print("\x1b[32mSuccessfully Changed.")
                    print("\x1b[0m")
                except:
                    print("\x1b[31mEnter Valid Data.......")
                    print("\x1b[0m")

            elif(inchoice == 2):
                print(df)
                try:
                    id_delete = int(input("Enter id:"))
                    coll.find_one_and_delete({"Book Id":id_delete})

                    print("\n")
                    print("\x1b[32mRemoved Successfully.")
                    print("\x1b[0m")

                except:
                    print("\x1b[31mEnter Valid Data.......")
                    print("\x1b[0m")

            elif(inchoice == 3):
                break
            
            else:
                print("\x1b[31mInvalid Option.Try Again...")
                print("\x1b[0m")

    elif(choice == 4):
        csvname = input("Enter file name you want to save as:")
        df.to_csv(csvname+'.csv',index=False)
        
        print("\n")
        print("\x1b[32mSuccessfully Saved.")
        print("\x1b[0m")
    
    elif(choice == 5):
        print("Thank You For Using Us.......")
        break
    
    else:
        print(choice)
        print("\x1b[31mInvalid Option.Try Again....")
        print("\x1b[0m")
