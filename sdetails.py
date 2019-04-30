#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, Student, Attendance, User

engine = create_engine('sqlite:///students.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create Dummy user
User1 = User(
    name="Chandu Siddartha",
    email="gsiddartha19@gmail.com",
    picture='https://lh5.googleusercontent.com/-8jCWuoDqb2I'
            '/AAAAAAAAAAI/AAAAAAAAAAc/m0qr01JjGFg/photo.jpg')
session.add(User1)
session.commit()

# Each Student details
student1 = Student(
    user_id = 1,
    name = "Ajay",
    rollno = "164g1a0501",
    gmail = "164g1a0501@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Alekhya",
    rollno = "164g1a0502",
    gmail = "164g1a0502@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Amrutha",
    rollno = "164g1a0503",
    gmail = "164g1a0503@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Anitha",
    rollno = "164g1a0504",
    gmail = "164g1a0504@srit.ac.in",
    phoneno = "987654321")

session.add(student1)

student1 = Student(
    user_id = 1,
    name = "Arbaaz",
    rollno = "164g1a0506",
    gmail = "164g1a0506@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Archana",
    rollno = "164g1a0507",
    gmail = "164g1a0507@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Ayesha",
    rollno = "164g1a0508",
    gmail = "164g1a0508@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bhanu",
    rollno = "164g1a0509",
    gmail = "164g1a0509@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bhanu Prakash",
    rollno = "164g1a0510",
    gmail = "164g1a0510@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bhargava",
    rollno = "164g1a0512",
    gmail = "164g1a0512@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bhargavi P",
    rollno = "164g1a0513",
    gmail = "164g1a0513@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bhargavi S",
    rollno = "164g1a0514",
    gmail = "164g1a0514@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bhavana",
    rollno = "164g1a0515",
    gmail = "164g1a0515@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Bushraanjum",
    rollno = "164g1a0516",
    gmail = "164g1a0516@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Chakrapani",
    rollno = "164g1a0517",
    gmail = "164g1a0517@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Chandrika",
    rollno = "164g1a0518",
    gmail = "164g1a0518@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Chandu Siddartha",
    rollno = "164g1a0519",
    gmail = "164g1a0519@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Damodar",
    rollno = "164g1a0520",
    gmail = "164g1a0520@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Dhenuka Datta",
    rollno = "164g1a0521",
    gmail = "164g1a0521@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Divya B",
    rollno = "164g1a0523",
    gmail = "164g1a0523@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Divya V",
    rollno = "164g1a0524",
    gmail = "164g1a0524@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Farhana",
    rollno = "164g1a0525",
    gmail = "164g1a0525@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Ganesh",
    rollno = "164g1a0526",
    gmail = "164g1a0526@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Gowthami",
    rollno = "164g1a0527",
    gmail = "164g1a0527@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Harika",
    rollno = "164g1a0528",
    gmail = "164g1a0528@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Harshitha",
    rollno = "164g1a0529",
    gmail = "164g1a0529@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Hemalatha",
    rollno = "164g1a0530",
    gmail = "164g1a0530@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Jaya Sree",
    rollno = "164g1a0532",
    gmail = "164g1a0532@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kaleem",
    rollno = "164g1a0534",
    gmail = "164g1a0534@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kalyan",
    rollno = "164g1a0535",
    gmail = "164g1a0535@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kavya Sree",
    rollno = "164g1a0536",
    gmail = "164g1a0536@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Keerthi M",
    rollno = "164g1a0537",
    gmail = "164g1a0537@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kishore Kumar",
    rollno = "164g1a0538",
    gmail = "164g1a0538@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Komala",
    rollno = "164g1a0539",
    gmail = "164g1a0539@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Koushika",
    rollno = "164g1a0540",
    gmail = "164g1a0540@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kranthi Kumar",
    rollno = "164g1a0541",
    gmail = "164g1a0541@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kumuda",
    rollno = "164g1a0542",
    gmail = "164g1a0542@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Kupendra",
    rollno = "164g1a0543",
    gmail = "164g1a0543@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Lakshmi D",
    rollno = "164g1a0544",
    gmail = "164g1a0544@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Lakshmi Madhav Krishna",
    rollno = "164g1a0545",
    gmail = "164g1a0545@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Lakshmi Prasanna",
    rollno = "164g1a0546",
    gmail = "164g1a0546@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Lavanya C",
    rollno = "164g1a0547",
    gmail = "164g1a0547@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Lavanya G",
    rollno = "164g1a0548",
    gmail = "164g1a0548@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Likhith Kumar",
    rollno = "164g1a0549",
    gmail = "164g1a0549@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Mallika",
    rollno = "164g1a0550",
    gmail = "164g1a0550@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Manasa",
    rollno = "164g1a0551",
    gmail = "164g1a0551@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Mani Chaitanya Sreenivasa",
    rollno = "164g1a0552",
    gmail = "164g1a0552@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Manisha",
    rollno = "164g1a0553",
    gmail = "164g1a0553@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Meena",
    rollno = "164g1a0555",
    gmail = "164g1a0555@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Mounika",
    rollno = "164g1a0556",
    gmail = "164g1a0556@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Nafiz",
    rollno = "164g1a0557",
    gmail = "164g1a0557@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Nandini",
    rollno = "164g1a0558",
    gmail = "164g1a0558@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Narasimhaiah",
    rollno = "164g1a0559",
    gmail = "164g1a0559@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Gangaraju",
    rollno = "174g5a0501",
    gmail = "174g5a0501@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Jaya Prakash",
    rollno = "174g5a0502",
    gmail = "174g5a0502@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Pavani",
    rollno = "174g5a0503",
    gmail = "174g5a0503@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

student1 = Student(
    user_id = 1,
    name = "Raghunath",
    rollno = "174g5a0504",
    gmail = "174g5a0504@srit.ac.in",
    phoneno = "987654321")

session.add(student1)
session.commit()

print "added Student Details!"
