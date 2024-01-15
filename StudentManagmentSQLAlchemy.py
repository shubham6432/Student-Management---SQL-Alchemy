#This is a menu driven mini project in SQLAlchemy

from sqlalchemy import *
from sqlalchemy.orm import declarative_base, sessionmaker
DB_URL= "mysql://root:root@localhost:3306/db2"
ENG= create_engine(DB_URL)

Base= declarative_base()

class Student(Base):
    __tablename__="Student_Tbl"
    rn=Column(Integer, primary_key=True)
    name=Column(String(20))
    marks= Column(Float)

Base.metadata.create_all(ENG)
Session=sessionmaker(bind=ENG)
sess=Session()

while True:
    ch= int(input("\nEnter Choice: \n1. Add Student. \t2. Update A Student\n3. Delete A Student. \t4. Show All Students\n5. Exit"))
    match ch:
        case 1:
            print("\n Add a Student")
            r=int(input("Enter Roll Number: "))
            n=input("Enter Name: ")
            m=float(input("Enter Marks: "))
            s1= Student(rn=r, name= n, marks=m)
            sess.add(s1)
            sess.commit()
            print("Student Added Successfully! ")
        case 2:
            print("\nUpdate a Student")
            r=int(input("Enter Roll Number To Update: "))
            m=float(input("Enter Updated Marks: "))
            x=sess.query(Student).filter(Student.rn==r).update({Student.marks:m})
            if x==0:
                print("\nInvalid Roll No, No Student Found with That Roll No")
            else:
                sess.commit()
                print("\nStudent Updated Successfully! ")            
        case 3:
            print("\nDelete a Student")
            r=int(input("Enter Roll Number To Delete: "))
            x=sess.query(Student).filter(Student.rn==r).delete()
            #print(x)
            if x==0:
                print("\nInvalid Roll No, No Students Found")
            else:
                sess.commit()
                print("\nStudent Deleted Successfully! ")
        case 4:
            print("\nShow All  Students")
            students=sess.query(Student)
            #print(students.count())
            if students.count() == 0:
                print("\nEmpty Table, no Students Found")
            else:
                for stu in students:
                    print(stu.rn,'\t', stu.name,'\t', stu.marks)
        case 5:
            print("\nExiting....")
            break
        case _:
            print("Invalid Choice...") 
