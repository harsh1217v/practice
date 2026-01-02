
#list function
rcb = ["Virat Kohli"," Phil Salt"," Devdutt Padikkal"," Rajat Patidar"," Liam Livingstone", "Jitesh Sharma", "Tim David"," Krunal Pandya", "Bhuvneshwar Kumar", "Josh Hazlewood", "Yash Dayal"]

mi = ["Rohit Sharma", "Ryan Rickelton", "Suryakumar Yadav", "Tilak Varma", "Hardik Pandya", "Will Jacks", "Naman Dhir", "Mitchell Santner", "Jasprit Bumrah", "Trent Boult", "Karn Sharma"]

pbsk = ["Prabhsimran Singh", "Priyansh Arya", "Shreyas Iyer", "Shashank Singh", "Marcus Stoinis", "Glenn Maxwell", "Suryansh Shedge", "Azmatullah Omarzai", "Marco Jansen", "Arshdeep Singh", "Yuzvendra Chahal"]

gt = ["Shubman Gill", "Jos Buttler", "Sai Sudharsan", "Shahrukh Khan", "Rahul Tewatia", "Sai Kishore", "Arshad Khan", "Rashid Khan", "Kagiso Rabada", "Mohammed Siraj", "Prasidh Krishna"]

print(rcb,mi,gt,pbsk )

def pop(listname,index):
    bin = listname.pop(index)
    return bin

a =pop(rcb,2)
print(f"popped element : {a}")

def append(listname,player):
    listname.append(player)
    return listname

b =append(rcb,"harsh dongare")
print(b)

def insert(listname,player,index):
    listname.insert(index,player)
    return listname

c =insert(rcb,"rinal gurnule",2)
print(c)