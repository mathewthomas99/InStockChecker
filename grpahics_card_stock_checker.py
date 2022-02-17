import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl

#link to product that is being checked
url = 'https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?Item=N82E16814137600'

#loop to check if its out of stock still will send email if it is in stock
while True:
    hmtl_content = requests.get(url).text

    soup = BeautifulSoup(html_content, 'lxml')
    str=soup.body.text
    print(str)
    if(str.find('OUT OF STOCK') != -1):
        time.sleep(1800)
        continue
    else:
        

# Create a secure connection and send email
        context = ssl.create_default_context()

        smtp_server="outlook.office365.com"
        port=587
        sender_email="mathewthomas99@hotmail.com"
        password="Iwasborn7-19-99"
        recieving_email="thomasm99@hotmail.com"
        message="""\
        subject:grpahics card

        go buy msi graphics card at https://www.newegg.com/msi-geforce-rtx-3080-rtx-3080-ventus-3x-10g/p/N82E16814137600?Item=N82E16814137600 ."""

        context=ssl.create_default_context()
        try:
            server=smtplib.SMTP(smtp_server, port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            server.sendmail(sender_email, recieving_email, message)
        except Exception as e:
            print(e)
        finally:
            server.quit()
        break