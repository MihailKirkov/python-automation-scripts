import smtplib
import email_text
import pandas as pd

def get_email(): # this function gets the email text and subjects (from the email_text.py) that will be sent
    message = email_text.TEXT
    subject = email_text.SUBJECT
    return f"Subject: {subject}\n\n{message}"

def get_recievers(): # this function returns all accounts that should recieve the emails, reading them from the Email column in emails.xlsx
    df = pd.read_excel('emails.xlsx') # read excel file with pandas
    emails = df['Emails'].tolist() # get Emails column
    return emails

def send_email(sender_email, sender_password, reciever_email, email): # this function sends an email
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, reciever_email, email)
    except:
        print(f'Error sending email to {reciever_email}!')

def input_sender_data(): # this function reads and returns the sender details
    sender_email = input("Sender email: ")
    sender_password = input("Sender App password: ") # Does not require email account password, uses google app password
    return (sender_email, sender_password)

def main():
    print("If you want to change the email text and subject, edit email_text.py.\nIf you want to add/remove recievers edit emails.xlsx\n")
    
    try:
        email = get_email()
        reciever_emails = get_recievers()
    except:
        reciever_emails = None
        print("Error reading data from email_text.py or emails.xlsx!")
        return

    sender_email, sender_password = input_sender_data()

    print("Sending emails...")
    for reciever_email in reciever_emails:
        send_email(sender_email, sender_password, reciever_email, email)
    print("done")

if __name__ == "__main__":
    main()