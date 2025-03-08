import smtplib
import getpass
import time

print("\n################## gee-mail sender ###################")
time.sleep(1.5)
print("\nRemember to use an 'App Password' instead of your Gmail password, \nas 'Less secure app access' is no longer supported.")

def final():
    ending = input("\nDo you want to send another email? (y/n): ").strip().lower()
    if ending == "n":
        print("\n##############################")
        print("\nBye bye!")
        time.sleep(1)
        print("\nSee you next time!")
        time.sleep(1)
        print("\n     Uriel-SG")
        print("\n##############################")
        exit()
    elif ending == "y":
        email_sending()
    else:
        print("\nInvalid option. Try again.")
        final()


def email_sending():
    number = int(input("\nHow many e-mails do you want to send? "))
    n = 0
    
    confirm = input(f"\nAre you sure you want to send {number} emails? (y/n) ")
    if confirm.upper() == "N":
        email_sending()
    elif confirm.upper() == "Y":
        pass
    else:
        print("\nPlease, 'y' or 'n'")
        email_sending()

    mail_subject = input("\nSubject: ").strip()
    mail_content = input("\nContent: ").strip()

    # Intestazioni corrette
    mail_user = input("\nYour username (without @gmail.com): ").strip()
    mailreceiver = input("\nReceiver: ").strip()

    mailsender = f"{mail_user}@gmail.com"
    message = f"From: {mailsender}\nTo: {mailreceiver}\nSubject: {mail_subject}\nContent-Type: text/plain; charset=utf-8\n\n{mail_content}"

    try:
        email = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        
        user_pass = getpass.getpass("\nYour App Password: ")

        email.login(mailsender, user_pass)

        while n <= number:
            email.sendmail(mailsender, mailreceiver, message.encode("utf-8"))
            n += 1

        email.quit()

        print("\nEmails sent successfully!")

    except Exception as e:
        print("\nFailed to send email.")
        print("Error:", e)

email_sending()

final()
