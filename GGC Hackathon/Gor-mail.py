import csv
import sys
#import smtplib

#def send_email():
#    sender = "hello@demomailtrap.com"
#    receiver = "isaiahgorman090203@gmail.com"

#    message = f"""\
#    Subject: {subject}
#    To: {receiver}
#    From: {sender}

#    {response}"""

#    with smtplib.SMTP("live.smtp.mailtrap.io", 587) as server:
#        server.starttls()
#        server.login("api", "d8845204fc853b0784e1f0202e80eebb")
#        server.sendmail(sender, receiver, message)

global keyword
emails = {}
match = 0
searches = 0

def search(match, searches):
    searches = 0
    match = 0
    with open(r'C:\Users\isaia\Downloads\cleaned_email_data_with_messages.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        keyword = input("Keyword: ")
        for row in reader:
            message = row["Message"]
            searches += 1
            if keyword in message:
                match += 1
                emails.update({row["Email Address"]: row["Message"]})
        if match > 0:
            print(f"Keyword [{keyword}] was detected {match} times out of {searches} searches!")
        elif match < 1:
            print(f"Sorry there were no matches detected for your keyword {keyword}.")
        return match, searches
        
def review():
    try:
        answer = input("Would you like to review the emails with the detected keyword? (y/n)")
        if answer.lower().startswith("y"):
            for email, message in emails.items():
                print(f"{email} sent the following message: ")
                print(message)

                #as the data provided for the emails is fake i cannot execute this function as intended and as such i have made it a comment.
                #choice = input("Would you like to reply to this email?")
                #if choice == "yes"
                #send_email()
                #if this were being properly implimented i would have fully intergrated this function into the program.
                #i do have a working demo though.
                #i also planned to integrate that function with a proper save feature to where you can pull up your previously saved files from the .txt file
                #and then you could go back into those saved emails and use this function to email the sender.

                choice = input("Would you like to save this email? (y/n) ")
                if choice.lower().startswith("y"):
                    savedfile = open("saved_emails.txt", "a+")
                    savedfile.write(f"{email}\n")
                    savedfile.write(f"{message}\n")
                    savedfile.write(f" \n")
                    print("Email and message saved. ")
                elif choice.lower().startswith("n"):
                    choice = input("Understood. Would you like to exit the program, search again, or move onto the next email? \nPlease answer 1, 2, or 3. ")
                    if choice == "1":
                        savedfile.close
                        sys.exit()
                    elif choice == "2":
                        search(match, searches)
                    elif choice == "3":
                        print("Moving on...")
                        pass
                    else:
                        print("Moving on, enter a valid input next time.")
                else:
                    print("Moving on, enter a valid input next time.")
        else:
            choice = input("Understood. Would you like to exit the program or search again? Type 1 to end. Type 2 to pass. ")
            if choice == "1":
                sys.exit()
            elif choice == "2":
                pass

    except ValueError:
        print("how did you even do that? ")

while True:
    match, searches = search(match, searches)
    if match > 0 or searches > 0:
        review()
    else:
        match, searches = search(match, searches)
    