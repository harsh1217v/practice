class player:
     def __init__(self,pn, jn, r, wk, tn):
           self.player_name =pn
           self.jersey_no = jn
           self.runs = r
           self.wickets = wk
           self.team_name = tn
           
     def display(self):
             print("player name:",self.player_name)
             print("Jersey No:", self.jersey_no)
             print("Runs:", self.runs)
             print("Wickets:", self.wickets)
             print("Team Name:", self.team_name)
             print("______________________________________________")
p1 = player("Virat Kohli", 18, 8000, 0, "RCB")
p2 = player("Phil Salt", 28, 2500, 0, "RCB")
p3 = player("Devdutt Padikkal", 24, 3000, 0, "RCB")
p4 = player("Rajat Patidar", 97, 2000, 0, "RCB")
p5 = player("Jitesh Sharma", 6, 1200, 0, "RCB")
p6 = player("Tim David", 19, 1500, 0, "RCB")
p7 = player("Romario Shepherd", 92, 800, 0, "RCB")
p8 = player("Krunal Pandya", 24, 1500, 0, "RCB")
p9 = player("Bhuvneshwar Kumar", 15, 500, 0, "RCB")
p10 = player("Josh Hazlewood", 38, 400, 0, "RCB")
p11 = player("Yash Dayal", 13, 200, 0, "RCB")


(p1.display())
(p2.display())
(p3.display())
(p4.display())
(p5.display())  
(p6.display())
(p7.display())
(p8.display())
(p9.display())
(p10.display())
(p11.display())

RCB_TEAM =[]
RCB_TEAM.append(p1)
RCB_TEAM.append(p2) 
RCB_TEAM.append(p3)
RCB_TEAM.append(p4)
RCB_TEAM.append(p5)
RCB_TEAM.append(p6)
RCB_TEAM.append(p7)
RCB_TEAM.append(p8)
RCB_TEAM.append(p9)
RCB_TEAM.append(p10)
RCB_TEAM.append(p11)

print("RCB Team Players:")
for player in RCB_TEAM:
    print(player.player_name)
    


