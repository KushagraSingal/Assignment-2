Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
SID = int(input('Enter SID: '))
Enter SID: 21102039
Name = str(input('Enter name: '))
Enter name: Kushagra Singal
Gender = str(input('Enter Gender(F, M, or U for Unknown): '))
Enter Gender(F, M, or U for Unknown): M
Course_Name = str(input('Enter Course_Name: '))
Enter Course_Name: CIVIL ENGINEERING
CGPA = float(input('Enter CGPA: '))
Enter CGPA: 9.8
while CGPA>10 or CGPA<0:
    print('Invalid CGPA Value, try again\n')
    CGPA = float(input('Enter CGPA: '))

    
Student = [SID,Name,Gender,Course_Name,CGPA]
print('Your data is:',Student)
Your data is: [21102039, 'Kushagra Singal', 'M', 'CIVIL ENGINEERING', 9.8]
