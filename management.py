def inputNameAndSortedArray_OutPutRank_(Name,o,n):
    for i in range(0,n):
        if(Name==o[i]):
            return (i+1)

def sorting_student_marks(Arr,o): 

    for j in range(0,n):
        for k in range(j+1,n):
            if(Arr[k]>Arr[j]):
                t=Arr[k]
                Arr[k]=Arr[j]
                Arr[j]=t
                r=o[k]
                o[k]=o[j]
                o[j]=r
    print("first runner-rup",o[0],"total mark",Arr[0])
    print("---------------------------------------------------")
    print("second runner-up is",o[1],"total mark",Arr[1])
    return (o,Arr)


Total=[]
Name=[]
v=[]
b=[]
s=[]
x=[]
sub=[]
sub2=[]
subNam=['First Language(Bengali)','Second Language(English)','Math','Biology','Physics','Chemistry']
sub2Nam=['bengali presentation','english presentation','maths presentation ','biology lab','physics lab','chemistry lab']
print("--------------STUDENT MARK SHEET------------------")
r=int(input("class :  "))
n=int(input("total number of student is : "))
for i in range(0,n):
    print("---------------------------------------------------")
    name=str(input("name of the student: "))
    roll=int(input("enter the roll of the student:"))
    print("---------------------------------------------------")
    Name.append(name)
    x.append(roll)
    print("//enter the marks of subject//")
    print("written marks: 70             extra curriculum activity:30")

    sum=0
    for j in range(0,5):
        print(subNam[j],end=' ')
        p=int(input(" "))
        while(p>70):
            p=int(input("you cannot enter greater than 70 \n enter marks: "))
        print(sub2Nam[j],end=' ')
        sub.append(p)
        q=int(input(" "))
        while(q>30):
            q=int(input("you cannot enter greater than 30 \n enter marks: "))
        sub2.append(q)
        print("..........................................")      
        sum=sum+p+q
    print("option  number out of 600 : ",sum )
    print((sum/600)*100,"%")
    print("..........................................")
    
    
    Total.append(sum)

b,s= sorting_student_marks(Total,Name)



file = open("!!please enter your file path!!", 'w')

for i in range(0,n):
    q=inputNameAndSortedArray_OutPutRank_(Name[i],b,n)
    #print(q)
    file.write("|:::::::::::::::::::::::Mark Shit::::::::::::::::::|\n")
    file.write("|--------------------------------------------------|\n")
    file.write("|Written: 70          Extra curriculum activity: 30|\n")
    file.write("|            "+"Rank Optained:"+str(q)+"                       |\n")
    file.write("| Name: "+str(Name[i])+"             Roll No:"+str(x[i])+"      \n")
    file.write("|--------------------------------------------------|\n")
    file.write("| subjects                                  marks  |\n")
    file.write("|--------------------------------------------------|\n")
    for j in range(0,5):
        file.write("|"  +str("{:<38}".format(sub2Nam[j]))+"|        "+str(sub[j] )+"  |\n" )
        file.write("|"  +str("{:<38}".format(subNam[j])) +"|        "+str(sub2[j])+"  |\n" )
    file.write("|--------------------------------------------------|\n")
    file.write("| Total Marks:"+"                                  "+str(Total[i])+" |\n")
    file.write("|--------------------------------------------------|\n")
    file.write("                                                    \n")
file.close()