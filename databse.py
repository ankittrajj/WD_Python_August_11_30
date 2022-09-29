import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Ankit@8285',
                database ='ironman')


cursor = con.cursor()

# if con.is_connected():
#     print("Connection Successfully!!")
while True:
    
        name = input("Enter the name")
        age = int(input("Enter the age"))
        marks = int(input('Enter the marks'))

        query = "Insert into jarvis values('{}',{},{})".format(name,age,marks)
        cursor.execute(query)
        con.commit()

    # choice = 2
    # if choice == 2:
    #     break
    # print("Data entered successfully!!")