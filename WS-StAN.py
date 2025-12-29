import requests
from bs4 import BeautifulSoup
import smtplib
from email.message import EmailMessage

def sendEmail():
    msg = EmailMessage()
    msg.set_content("Es sind neue Termine für die Eheschließung im Standesamt Ansbach verfügbar. Bitte überprüfen Sie die Website für weitere Details.")

    msg['Subject'] = 'Neue Termine im Standesamt Ansbach verfügbar'
    msg['From'] = 'julialippert912@gmail.com'
    msg['To'] = 'julialippert912@icloud.com'
    
    # Use Gmail's SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    # Replace with your Gmail address and app password
    s.login('julialippert912@gmail.com', 'tccybpwstyvbbton')
    s.send_message(msg)
    s.quit()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

page = requests.get('https://www.ansbach.de/Bürger/Rathaus-Service/Bürgerservice-Online-Dienste/Standesamt/Eheschließung/', headers=headers)

soup = BeautifulSoup(page.text, 'html.parser')

# get the accordion
appointmentsBody = soup.find(id='sect-1-3')
if appointmentsBody is None:
    h2Tags = soup.find_all('h2')
else:
    h2Tags = appointmentsBody.find_all('h2')

for h2 in h2Tags:
    if '2026' in h2.text:
        sendEmail()
        
        

