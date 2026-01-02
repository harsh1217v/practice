films = {
    2023: {
        "Jawan": ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi", "Deepika Padukone"],
        "Pathaan": ["Shah Rukh Khan", "Deepika Padukone", "John Abraham", "Dimple Kapadia"],
        "Animal": ["Ranbir Kapoor", "Anil Kapoor", "Rashmika Mandanna", "Bobby Deol"],
        "Gadar 2": ["Sunny Deol", "Ameesha Patel", "Utkarsh Sharma", "Manish Wadhwa"]
    },

    2024: {
        "Fighter": ["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor", "Karan Singh Grover"],
        "Kalki 2898 AD": ["Prabhas", "Deepika Padukone", "Amitabh Bachchan", "Kamal Haasan"],
        "Singham Again": ["Ajay Devgn", "Kareena Kapoor", "Akshay Kumar", "Ranveer Singh"],
        "Pushpa 2": ["Allu Arjun", "Rashmika Mandanna", "Fahadh Faasil", "Jagapathi Babu"]
    },

    2025: {
        "War 2": ["Hrithik Roshan", "Jr NTR", "Kiara Advani", "Anil Kapoor"],
        "Tiger vs Pathaan": ["Salman Khan", "Shah Rukh Khan", "Deepika Padukone", "Katrina Kaif"],
        "Don 3": ["Ranveer Singh", "Kiara Advani", "Vikrant Massey", "Boman Irani"],
        "Brahmastra 2": ["Ranbir Kapoor", "Alia Bhatt", "Amitabh Bachchan", "Nagarjuna"]
    }
}


            
def film_cast(d):
    
    movies=[]        
    for year_dict in d.values():
        for m, c in year_dict.items():
            if "Shah Rukh Khan" in c:
                movies.append(m)
    return movies 
            
m=film_cast(films)
print(m)

print(m[0])





