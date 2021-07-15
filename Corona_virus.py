def risk():
    return age > 75 and chronic == "yes" and immune == "yes"


while True:
    age = int(input("Are you a cigarette addict older than 75 years old?:\n('Please enter your age)\n"
                    "Enter '0' to quit"))
    if age == 0:
        print("Program sonlandırılıyor...")
        break
    else:
        chronic = input("Do you have a severe chronic disease?:\n(Please enter just 'Yes' or 'No')").lower().strip()
        immune = input("Is your immune system too weak?:\n(Please enter just 'Yes' or 'No')").lower().strip()
        if risk():
            print("You are in risky group.")
        else:
            print("You are not in risky group.")
