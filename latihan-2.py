import re
import random
import string

def buat_password(panjang):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(panjang))

def proses_emails(emails):
    email_pattern = r'(\S+@\S+\.\S+) dimiliki oleh (\S+)'
    matches = re.findall(email_pattern, emails)
    
    for email, username in matches:
        password = buat_password(8)
        print(f"{email} username: {username} , password: {password}")

emails = """
Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari
"""

proses_emails(emails)