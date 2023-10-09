import pandas as pd
import random
import smtplib
import datetime 

# TODO-1: READ THE CSV 
dt = pd.read_csv("day32/birthdays.csv")

# TODO-1.1: EXTRACT THE CURRENT_DATE IN THIS FORMAT (YEAR.MONTH.DAY)
current_date = datetime.date.today()
current_year = current_date.year
current_month = current_date.month
current_day = current_date.day

# TODO-1.2: CHECK AND SELECT THE ONE THAT MATCHES CURRENT DATE TIME
matching_rows = dt[(dt["year"] == current_year) & (dt["month"] == current_month) & (dt["day"] == current_day)]

if not matching_rows.empty:
    # TODO-2: SELECT RANDOMLY ONE OF THE TEMPLATES
    file_names = [
        "day32/letter_templates/letter_1.txt",
        "day32/letter_templates/letter_2.txt",
        "day32/letter_templates/letter_3.txt"
    ]
    file_name = random.choice(file_names)
    
    with open(file_name) as template:
        letter = template.readlines()
        
        # TODO-2.1: REPLACE THE SELECTED ONE'S NAME IN THE SELECTED TEMPLATE LETTER
        name = matching_rows["name"].iloc[0]
        letter = [line.replace("[NAME]", name) for line in letter]
        modified_letter = ''.join(letter)
        
        # TODO-2.2: SELECT EMAIL
        email = matching_rows["email"].iloc[0]

    # TODO-3: SEND THE EMAIL
    try:
        with smtplib.SMTP("your_email_server.com") as connection:
            connection.starttls()
            connection.login(user="your_email@gmail.com", password="your_password")
            
            subject = "Subject: Your Losing Another Year of Your Life"
            body = f"Hello,\n\n{modified_letter}"
            
            connection.sendmail(from_addr="your_email@gmail.com", to_addrs=email, msg=subject + "\n\n" + body)
            
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
else:
    print("I will send your message on their birthdate.")
