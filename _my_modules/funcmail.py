"""
Script to prepare and send email
Develop: 30 May 2018
"""

# IMPORT PYTHON OBJECTS
import csv
import logging
import os
import configparser

# IMPORT OWN OBJECTS
from _my_modules import funcfile
from _my_modules import funcdatn
from _my_modules import funcdatn
from _my_modules import funcstr
from _my_modules import funcconf

""" FUNCTION INDEX
send_mail - Send mail from the S:/_external_data/000_mail.csv mail file.
replace_date_placeholders - Replace date placeholders. Used in send_mail.
send - Do the actual mail send.
"""


def send_mail(s_trigger, s_subject='', s_body='', file_path="S:/_external_data/000_mail.csv"):

    # Declare variables
    logging.info("DEFINITION: Send mail %s", s_trigger)
    l_debug: bool = False

    with open(file_path, "r") as co:
        co_reader = csv.DictReader(co)

        for row in co_reader:
            if row['TRIGGER'] != s_trigger:
                continue
            if row['ACTIVE'] == "X":
                continue
            if funcstr.isNotBlank(row['SCHEDULE']) and row['SCHEDULE'] not in [funcdatn.get_today_day_strip(), funcdatn.get_today_name()]:
                continue
            if l_debug:
                print(row)
            to_name = row['TO_NAME']
            to_address = row['TO_ADDRESS']
            mail_language = row['LANGUAGE']
            mail_subject = row['SUBJECT'] if s_subject == '' else s_subject
            mail_body = row['BODY'] if s_body == '' else s_body
            file_path = replace_date_placeholders(row['DIR'])
            file_name = replace_date_placeholders(row['FILE'])

            s_result = send(to_name, to_address, mail_language, mail_subject, mail_body, file_path, file_name)
            if l_debug:
                print(to_name)
                print(to_address)
                print(mail_language)
                print(mail_subject)
                print(mail_body)
                print(file_path)
                print(file_name)
                print(s_result)

            if s_result == "Successfully sent email":
                logging.info("MAIL SUCCESS: %s (%s)", to_address, to_name)
            else:
                logging.error("MAIL FAIL: %s (%s)", to_address, to_name)
                logging.error("FAIL REASON: %s", s_result)


def replace_date_placeholders(text):
    text = text.replace("%PYEAR%", funcdatn.get_previous_year())
    text = text.replace("%PMONTH%", funcdatn.get_previous_month())
    text = text.replace("%CYEAR%", funcdatn.get_current_year())
    text = text.replace("%CMONTH%", funcdatn.get_current_month())
    text = text.replace("%TODAY%", funcdatn.get_today_date_file())
    return text


def send(to_name, to_addr, mail_lang, mail_subject, mail_body, file_path, file_name):
    """
    Mail parameters
    :param to_name: Name of the recipient
    :param to_addr: Email address of the recipient
    :param mail_lang: Language indicator A=Afrikaans Else=English
    :param mail_subject: Email subject
    :param mail_body: Email body
    :param file_path: Attachment path
    :param file_name: Attachment name
    :return: Text message to indicate successful mail sending
    """

    import smtplib
    # from smtplib import SMTP  # Standard connection
    from smtplib import SMTP_SSL as SMTP  # SSL connection
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email import encoders

    # Read from the configuration file
    config = configparser.ConfigParser()
    config.read('.config.ini')
    if funcconf.l_tel_use_nwu:
        from_address = config.get('MAIL', 'from_nwu')
        host = config.get('MAIL', 'host_nwu')
        port = config.get('MAIL', 'port_nwu')
        user = config.get('MAIL', 'user_nwu')
        password = config.get('MAIL', 'password_nwu')
    else:
        from_address = config.get('MAIL', 'from_albert')
        host = config.get('MAIL', 'host_albert')
        port = config.get('MAIL', 'port_albert')
        user = config.get('MAIL', 'user_albert')
        password = config.get('MAIL', 'password_albert')

    # Declare variables
    s_return = ""

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_addr
    msg['Subject'] = mail_subject

    if mail_lang == "A":
        body = "Hallo " + to_name + "\n\n" + mail_body + "\n\nVriendelike groete\nCaria (Continuous Audit Robot Internal Audit)"
    else:
        body = "Hallo " + to_name + "\n\n" + mail_body + "\n\nKind regards\nCaria (Continuous Audit Robot Internal Audit)"

    msg.attach(MIMEText(body, 'plain'))

    if file_name != "":
        attachment = open(file_path + file_name, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
        msg.attach(part)

    server_connect = False
    try:

        # Server
        server = SMTP(host, port)
        server.login(user, password)
        server.ehlo_or_helo_if_needed()
        # server.starttls()
        server_connect = True

        # gmail from work
        # server = SMTP('smtp.gmail.com', '465')
        # server.login("nwu.internal.audit@gmail.com", "eab3edaed28ea35bcf68d722a72f7e92879f755c5b3962c9f827eed53b9d2dbf")

        # gmail from home
        # server = SMTP('smtp.gmail.com', '568')
        # server.login("nwu.internal.audit@gmail.com", "eab3edaed28ea35bcf68d722a72f7e92879f755c5b3962c9f827eed53b9d2dbf")

    except smtplib.SMTPHeloError as e:
        s_return = "Server did not reply"
    except smtplib.SMTPAuthenticationError as e:
        s_return = "Incorrect username/password combination"
    except smtplib.SMTPException as e:
        s_return = "Authentication failed"

    if server_connect:
        try:
            server.sendmail(from_address, to_addr, msg.as_string())
            s_return = "Successfully sent email"
        except smtplib.SMTPException as e:
            s_return = "Error: unable to send email", e
        finally:
            server.close()

    return s_return


"""python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, message, attachments):
    # Setup the email header information
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    for attachment_filepath in attachments:
        # Open the file in bynary
        with open(attachment_filepath, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_filepath}",
        )

        # Add attachment to message and convert message to string
        msg.attach(part)

    # Connect to the email server using SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)

    # Disconnect from the server
    server.quit()

# Example usage
sender_email = "your_email@gmail.com"
sender_password = "your_password"
receiver_email = "receiver_email@example.com"
subject = "Python Email with Attachments"
message = "This email has attachments."

# List of file paths for attachments
attachments = ["attachment1.txt", "attachment2.pdf"]

send_email(sender_email, sender_password, receiver_email, subject, message, attachments)

Make sure to replace the `sender_email` and `sender_password` variables with your own Gmail credentials. Also, update `receiver_email`, `subject`, `message`, and `attachments` variables according to your requirements.

Note: For this script to work, you need to have the `smtplib` and `email` packages installed. You can install them using pip:

```
pip install secure-smtplib
pip install email
```

Additionally, make sure to enable the "Less secure app access" in your Gmail account settings to allow the script to send emails using your account.

"""

def mail_old(s_trigger, s_subject='', s_body=''):
    """
    Function to PREPARE email using parameters from 000m_Mail.csv
    :rtype: str
    :param s_trigger: Mail function trigger
    :param s_subject: Mail subject
    :param s_body: Mail body
    :return: Text message to indicate successful mail send
    """

    # OPEN THE SCRIPT LOG FILE
    funcfile.writelog("%t DEFINITION: Send mail " + s_trigger)

    # DECLARE VARIABLES
    sl_path = "S:/_external_data/"

    print("Send email " + s_trigger)

    # Read the mail parameters from the 000_Mail.csv file """
    co = open(sl_path + "000_mail.csv", "r")
    co_reader = csv.reader(co)

    # Read the COLUMN database data
    for row in co_reader:

        # Populate the local variables
        send_mail_trigger = False

        # Populate the column variables
        if row[0] != s_trigger:
            continue
        elif row[1] == "X":
            continue
        elif funcstr.isNotBlank(row[9]):
            if row[9] == funcdatn.get_today_day_strip():
                send_mail_trigger = True
            elif row[9] == funcdatn.get_today_name():
                send_mail_trigger = True
        else:
            send_mail_trigger = True

        if send_mail_trigger:

            # Build the mail parameters from the 000m_Mail.csv file
            to_name = row[2]
            to_address = row[3]
            mail_language = row[4]
            if s_subject == '':
                mail_subject = row[5]
            else:
                mail_subject = s_subject
            if s_body == '':
                mail_body = row[6]
            else:
                mail_body = s_body
            file_path = row[7]
            file_path = file_path.replace("%PYEAR%", funcdatn.get_previous_year())
            file_path = file_path.replace("%PMONTH%", funcdatn.get_previous_month())
            file_path = file_path.replace("%CYEAR%", funcdatn.get_current_year())
            file_path = file_path.replace("%CMONTH%", funcdatn.get_current_month())
            file_path = file_path.replace("%TODAY%", funcdatn.get_today_date_file())
            file_name = row[8]
            file_name = file_name.replace("%PYEAR%", funcdatn.get_previous_year())
            file_name = file_name.replace("%PMONTH%", funcdatn.get_previous_month())
            file_name = file_name.replace("%CYEAR%", funcdatn.get_current_year())
            file_name = file_name.replace("%CMONTH%", funcdatn.get_current_month())
            file_name = file_name.replace("%TODAY%", funcdatn.get_today_date_file())

            # Send the mail
            s_result = send(to_name, to_address, mail_language, mail_subject, mail_body, file_path, file_name)

            # Mail result log
            if s_result == "Successfully sent email":
                print("MAIL SUCCESS: " + to_address + " (" + to_name + ")")
                funcfile.writelog("%t MAIL SUCCESS: " + to_address + " (" + to_name + ")")
            else:
                print("MAIL FAIL: " + to_address + " (" + to_name + ")")
                print("FAIL REASON: " + s_result)
                funcfile.writelog("%t MAIL FAIL: " + to_address + " (" + to_name + ")")
                funcfile.writelog("%t REASON FAIL: " + s_result)

    # Close the imported data file
    co.close()
