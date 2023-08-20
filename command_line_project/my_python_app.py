from asciiAndItineraries import holiday, kohsamui_adventure, kohsamui_culture, kohsamui_relax, london_adventure, london_culture, london_relax, malta_adventure, malta_culture, malta_relax, menorca_adventure, menorca_culture, menorca_relax, milan_adventure, milan_culture, milan_relax

def insideholidayplanner():
        planholiday = ""
        while planholiday != "yes" and planholiday != "no":
            planholiday = input("\nWould you like some help with planning your next holiday? (yes/no): ")
            if planholiday == "yes":
                print("\nAmazing, let's start building your dream holiday!")
            elif planholiday =="no":
                print("\nOh okay then...Come back when you need help with planning your next holiday :)")
                return "no"
            else:
                print("\nSorry, I didn't get that.")
          
        destination = ""
        holidaytype = ""
        while destination != "Koh Samui" and destination != "London" and destination != "Malta" and destination != "Menorca" and destination != "Milan":
            destination = input("\nWhere would you like to go? (Koh Samui/London/Malta/Menorca/Milan): ")

            if destination == "Koh Samui":
              print("Amazing, one of my favourite places!")
              while holidaytype != "Adventurous" and holidaytype != "Cultural" and holidaytype != "Relaxing":
                    holidaytype = input("\nWould you prefer an adventurous, cultural or relaxing holiday? (adventurous/cultural/relaxing): " )

                    if holidaytype == "adventurous":
                      print(kohsamui_adventure)
                    elif holidaytype == "cultural":
                      print(kohsamui_culture)
                    elif holidaytype == "relaxing":
                      print(kohsamui_relax)
                    else:
                        print("\nSorry, I didn't get that...")
                    return "yes"
        
            elif destination == "London":
              print("Great choice!")
              while holidaytype != "adventurous" and holidaytype != "cultural" and holidaytype != "relaxing":
                    holidaytype = input("\nWould you prefer an adventurous, cultural or relaxing holiday? (adventurous/cultural/relaxing): " )

                    if holidaytype == "adventurous":
                      print(london_adventure)
                    elif holidaytype == "cultural":
                      print(london_culture)
                    elif holidaytype == "relaxing": 
                      print(london_relax)  
                    else:
                        print("\nSorry, I didn't get that...")
                    return "yes"

            elif destination == "Malta":
              print("Brilliant choice!")
              while holidaytype != "adventurous" and holidaytype != "cultural" and holidaytype != "relaxing":
                    holidaytype = input("\nWould you prefer an adventurous, cultural or relaxing holiday? (adventurous/cultural/relaxing): " )

                    if holidaytype == "adventurous":
                      print(malta_adventure)
                    elif holidaytype == "cultural":
                      print(malta_culture)
                    elif holidaytype == "relaxing": 
                      print(malta_relax)  
                    else:
                        print("\nSorry, I didn't get that...")
                    return "yes"

            elif destination == "Menorca":
              print("Muy bueno!")
              while holidaytype != "adventurous" and holidaytype != "cultural" and holidaytype != "relaxing":
                    holidaytype = input("\nWould you prefer an adventurous, cultural or relaxing holiday? (adventurous/cultural/relaxing): " )

                    if holidaytype == "adventurous":
                      print(menorca_adventure)
                    elif holidaytype == "cultural":
                      print(menorca_culture)
                    elif holidaytype == "relaxing": 
                      print(menorca_relax)  
                    else:
                        print("\nSorry, I didn't get that...")
                    return "yes"
        
            elif destination == "Milan":
              print("Perfetto!")
              while holidaytype != "adventurous" and holidaytype != "cultural" and holidaytype != "relaxing":
                    holidaytype = input("\nWould you prefer an adventurous, cultural or relaxing holiday? (adventurous/cultural/relaxing): " )

                    if holidaytype == "adventurous":
                      print(milan_adventure)
                    elif holidaytype == "cultural":
                      print(milan_culture)
                    elif holidaytype == "relaxing": 
                      print(milan_relax)  
                    else:
                        print("\nSorry, I didn't get that...")
        return "yes"


def holidayplanner():
    print(holiday)
    print("\nWelcome to your holiday planner!")
  
    anythingElse = insideholidayplanner()
    while anythingElse != "no":
        anythingElse = input("\nCan I help plan another holiday for you? (yes/no): ")
        if anythingElse == "yes":
            anythingElse = insideholidayplanner()
        elif anythingElse == "no":
            print("\nIn that case, I hope you have an amazing holiday!")
        else:
            print("Sorry, I didn't get that...")

    print("Have a nice day! :)")


holidayplanner()