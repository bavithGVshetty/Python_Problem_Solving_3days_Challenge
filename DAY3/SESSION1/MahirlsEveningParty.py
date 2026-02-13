def partySuccessCheck(day,attendees):
    days=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    # Input constraint
    if day not in days or attendees<0:
        return "Invalid Input"

    if day in ["FRI","SAT","SUN"]:
        if attendees>=1500:
            return "Successfull"
        else:
            return "Unsuccessfull"
    else:
        if 700<=attendees<=1000:
            return "Successful"
        else:
            return "Unsuccesful"
 
# MAIN()
day= input("Enter the day: ").strip().upper()
attendees=int(input("Enter the number of attendees: ").strip())

CheckSuccess=partySuccessCheck(day,attendees)
print(CheckSuccess)