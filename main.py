import time
import random
import string

def main():
    x = {
        "Hugo Burton": ["009090", "band 7","NO123"],
        "Jane Smith": ["009091", "band 6","FO234"],
        "John Fisher": ["1", "band 6", "FT567"],
    }
    
    job_applications = {

    
    }
    
    admin_name = ["Admin 34"]
    admin_id = ["111"]
    
    contact_phone = {

    }
    
    contact_email = {

    }


    print("--------------------------------------------------------NHS SYSTEM---------------------------------------------------------")
    mode = input("Worker - 1 / Admin - 2 / Job application - 3/ Making a NHS account and cant think of a safe ID? - 4/Band salary hub - 5/Contact us - 6/ end: ")
    while mode != "1" and mode != "2" and  mode != "3" and mode != "4" and mode != "5" and mode != "6" and mode != "end":
        mode = input("Oops....option not found try again Worker - 1 / Admin - 2 / Job application - 3/ Making a NHS account and cant think of a safe ID? - 4/Band salary hub - 5/Contact us - 6/ end: ")
    if mode == "end":
        print("Turning off.............")
        time.sleep(2)

    elif mode == "1":
        while mode != "end":
            options = input("Enter what you would like to do  (check my band/profile/ID check/main): ")
            if options != "check my band" and options != "profile" and options != "main" and options != "ID check":
                options = input("Oops....option not found try again (check my band/profile/ID check/main): ")

            
            if options == "check my band":
                name = input("Your name: ")
                if name in x:
                    id = input("Enter the ID on your lanyard: ")
                    if id == x[name][0]:
                        print(f"You are {x[name][1]}")
                        main()
                        break
                    else:
                        break

            elif options == "profile":
                name = input("Enter your name: ")
                id = input("Enter your ID on your lanyard: ")
                band = input("Enter your band: ")
                x[name] = [id, band]
                print(x)
                main()
                break
            
            elif options ==  "ID check":
                name = input("Enter your name: ")
                if name in x:
                    get = input("Enter your health insurance passcode: ")
                    if get == x[name][2]:
                        print(f"Your id is {x[name][0]}")
                else:
                    main()
                    break
            
            elif options == "main":
                main()
                break

    elif mode == "2":
        admin_n = input("Enter Admin name: ")
        admin_idd = input("Enter you Admin ID: ")    
        if admin_n in admin_name and admin_idd in admin_id:
            while True:
                options = input("Pick option(check my band/profile/remove/change/a/jobs/contact/database/ID check/main/end): ")
                if options != "check my band" and options != "profile" and options != "ID check"and options != "remove" and options != "change" and options != "a" and options != "jobs" and options != "end" and options != "database" and options != "contact" and options != "main":
                    options = input("Oops....option not found try again (check my band/profile/remove/change/a/jobs/database/ID check/main/end): ")
            
                if options == "check my band":
                    name = input("Your name: ")
                    if name in x:
                        id = input("Enter the ID on your lanyard: ")
                        if id == x[name][0]:
                            print(f"You are {x[name][1]}")
                            main()
                            break
                        else:
                            print("Error: Invalid ID")
                            break
                elif options == "profile":
                    name = input("Enter your name: ")
                    id = input("Enter your ID on your lanyard: ")
                    band = input("Enter your band: ")
                    x[name] = [id, band]
                    print(x)
                    main()
                    break
                elif options == "database":
                    password = input("Enter password: ")
                    if password == "noodleman1234":
                        print(x)
                    else:
                        print("Error")
                        main()
                        break

                elif options == "remove":
                    name = input("Enter your name: ")
                    id = input("Enter your ID on your lanyard: ")
                    if name in x and id == x[name][0]:
                        x.pop(name)
                        print(x)
                        print("successfully removed")
                        main()
                        break
                    else:
                        print("Error: Invalid name or ID")
                        main()
                        break
                elif options == "change":
                    name = input("Enter your name: ")
                    id = input("Enter ID: ")
                    if name in x and id == x[name][0]:
                        choice = input("Enter choice(BAND/ID): ")
                        if choice == "ID":
                            x[name][0] = ""
                            new_id = input("Enter your new id: ")
                            x[name][0] = new_id
                            print(x)
                            main()
                            break
                        elif choice == "BAND":
                            x[name][1] = ""
                            new_band = input("Enter your new band: ")
                            x[name][1] = new_band
                            print(x)
                            main()                            
                            break
                elif options == "a":
                    name = str(input("Enter Admin name: "))
                    id_n = str(input("Enter Admin ID: "))
                    email = str(input("Enter Admin email: "))
                    address = str(input("Enter Admins address: "))
                    x[name] = [id_n, email, address]
                    admin_name.append(name)
                    admin_id.append(id_n)
                    print(admin_id)
                    print(admin_name)
                    print(x)
                    break
                        
                elif options == "ID check":
                    name = input("Enter name of person you would like to find out their health insurance number: ")
                    if name in x:
                            print(f"This is {name} in database health insurance: {x[name][2]}")
                    else:
                        print("Error.")
                        main()
                        break
                        

                
                elif options == "jobs":
                    print("Checking new applications......")
                    time.sleep(5)
                    file = open("jb.txt", "r")
                    for i in file.readlines():
                        print(i)

                
                elif options == "contact":
                    print("Checking for requests.....")
                    time.sleep(2)
                    file = open("phone.txt", "r")
                    fi = open("email.txt", "r")
                    for i in file.readlines():
                        print(i)
                    for x in fi.readlines():
                        print(x)
                        
                    
            
            
                elif options == "end":
                    print("Turning off.......")
                    time.sleep(2)
                    break
                
                elif options == "main":
                    main()
                    break
        else:
            print("ERROR.")
            main()

    elif mode == "3":
        print("APPLY FOR NHS JOB")
        while mode != "end":
            role = input("Enter the number for which job you would like to apply for: Nurse-1, Doctor-2 , IT-3 , Cleaner-4 , Cafe-5, end, main: ")
            if role != "1" and  role != "2" and  role != "3"and  role != "4" and  role != "5" and role != "end" and role != "main":
                role = input("Ooops...role not found try again  Nurse-1, Doctor-2 , IT-3 , Cleaner-4 , Cafe-5, end or main: ")

            if role == "1":
                name = str(input("Please enter your full legal name: "))
                number = str(input("Please enter your contact number: "))
                email = str(input("Please enter your email: "))
                info = str(input("Enter some interesting things about you: "))
                job_applications[name] = [number, email, info, "NURSE APPLICATION"]
                x = str(job_applications)
                with open("jb.txt", "a") as file:
                    file.write(x + "\n")
                print("Application has been completed")

    
            elif role == "2":
                name = str(input("Please enter your full legal name: "))
                number = str(input("Please enter your contact number: "))
                email = str(input("Please enter your email: "))
                info = str(input("Enter some interesting things about you: "))
                job_applications[name] = [number, email, info, "DOCTOR APPLICATION"]
                x = str(job_applications)
                with open("jb.txt", "a") as file:
                    file.write(x + "\n")
                print("Application has been completed")

    
            elif role == "3":        
                name = str(input("Please enter your full legal name: "))
                number = str(input("Please enter your contact number: "))
                email = str(input("Please enter your email: "))
                info = str(input("Enter some interesting things about you: "))
                job_applications[name] = [number, email, info, "IT APPLICATION"]
                x = str(job_applications)
                with open("jb.txt", "a") as file:
                    file.write(x + "\n")
                print("Application has been completed")

        
            elif role == "4":
                name = str(input("Please enter your full legal name: "))
                number = str(input("Please enter your contact number: "))
                email = str(input("Please enter your email: "))
                info = str(input("Enter some interesting things about you: "))
                job_applications[name] = [number, email, info, "Cleaner APPLICATION"]
                x = str(job_applications)
                with open("jb.txt", "a") as file:
                    file.write(x + "\n")
                print("Application has been completed")

    
            elif role == "5":
                name = str(input("Please enter your full legal name: "))
                number = str(input("Please enter your contact number: "))
                email = str(input("Please enter your email: "))
                info = str(input("Enter some interesting things about you: "))
                job_applications[name] = [number, email, info, "Cafe worker APPLICATION"]
                x = str(job_applications)
                with open("jb.txt", "a") as file:
                    file.write(x + "\n")
                print("Application has been completed")

            
            elif role == "end":
                print("Turning off")
                time.sleep(2)
                break
            
            elif role == "main":
                main()
                break

    elif mode == "4":
        num = int(input("Enter how long you would like your id to be: "))    
        def password(length=num):
                characters = string.ascii_letters + string.digits
                return ''.join(random.choice(characters)for _ in range(num))
        gen = password(num)
        print("Your generated ID is :" + gen)
        password(length=num)
        main()

    


    elif mode == "5":
        print("--Welcome to the NHS salary hub--")
        band = input("Enter what band in nhs would you like to find out about: ")
        band = int(band)
        if 1 <= band <= 10:
            if band == 10:
                print("Doctors and Head managers of hospitals earn this type of salaries:")
                print("£87,900 - £120,000 per annum")
                main()
            elif band == 9:
                print("Matrons and head of wards can earn this type of salary:")
                print("£61,500 - 87,900 per annum")
                main()
            elif band == 8:
                print("Chief nurses can earn this type of salaries:")
                print("£54,600 - £61,500")
                main()
            elif band == 7:
                print("Nurses with over 7 years experience can earn this type of salary:")
                print("£48,560 - £54,600")
                main()
            elif band == 6:
                print("Nurse with over 3 years of experience can ear this type of salary:")
                print("£41,670 - £48,560 per annum")
                main()
            elif band < 6:
                ("This band is generally the salaries for most workers of are hospital:")
                print("£22,780 - £41,670 per annum")
                main()
        else:
            print("ERROR: Band number must be between 1 and 10.")
            main()
            
    elif mode == "6":
        print("Want to contact us ?")
        choice = input("Choose if you would like to contact us through email/phone call/main/end: ")
        if choice == "email": 
            first = str(input("Enter your email please: "))
            qu = str(input("Please enter your question?: "))
            contact_email[first] = [qu]
            x = str(contact_email)
            with open("email.txt", "a") as file:
                    file.write(x + "\n")
                    print("Request has been sent.")
                    main()


        elif choice == "phone call":
            first = str(input("Enter your phone number please: "))
            qu = str(input("Please enter your question?: "))
            contact_phone[first] = [qu]
            m = str(contact_phone)
            with open("phone.txt", "a") as file:
                file.write(m + "\n")
                print("Request has been sent.")
                main()

                
        elif choice == "main":
            main()
        elif choice == "end":
            print("Turning off")
            time.sleep(2)
        else:
            main()

main()
