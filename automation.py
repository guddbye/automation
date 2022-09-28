import re

def find_phone_nums(file):
    with open(file) as f:
        file_text = f.read()

    reg = r"(\d{3}-|\(\d{3}\)-|)(\d{3}-\d{4})"
    scrambled_phone_num = re.findall(reg, file_text)
    scrambled_phone_num = [''.join(phone) for phone in scrambled_phone_num]
    arranged_phone_num = list(map(format_phone, scrambled_phone_num))
    arranged_phone_num = set(arranged_phone_num)

    with open("assets/phone_numbers.txt", "w") as f:
        for phone in arranged_phone_num:
            f.write(f"{phone}\n")

def format_phone(phone):
    if len(phone) == 8:
        prefix = "206-"
        phone = prefix + phone
        return phone
    else:
        return phone

def find_emails(file):
    with open(file) as f:
        file_text = f.read()

    reg = r"([\w\d-]*@[\w\d-]*\.)(com|org|net|gov|edu)"
    emails = re.findall(reg, file_text)

    formatted = [''.join(email) for email in emails]
    formatted = set(formatted)
    email_str = '\n'.join(formatted)

    with open("assets/emails.txt", 'w') as f:
        f.write(email_str)

def find_phone_email(file):
    find_emails(file)
    find_phone_nums(file)

find_phone_email("assets/potential-contacts.txt")