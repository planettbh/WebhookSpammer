import requests
import json
import threading
import time

spam = input("Message to spam: ")
outputspam = spam + " | https://dsc.gg/hill"

url1 = 'https://discord.com/api/webhooks/1091283955837317252/rjYdgS875iShhO0ix7ALmtJCZwuU67RCJPuOhTdOykU9hxAQAMSGOOc_lf1hcS7Vt4J-'
url2 = 'https://discord.com/api/webhooks/1091283965056389140/uuEteqinOGwiU11PKgLXai5IulzwA530nbKJV94VcQmpeblp9fJq5Lc5UGXVZCcXCp6J'
url3 = 'https://discord.com/api/webhooks/1091283967006740592/7oLmEuSj93VsYVH5B980AlW5hqEjtUmhonaU9VT8PqwlFhtEg4hyLODXUZKZWVpt3q8v'
url4 = 'https://discord.com/api/webhooks/1091283968722215023/W9Mif2aNUbtMb9rKIQM1R88gUjnAz0DrRv4xByO7PlloYsOXhrSP0dJ55hA_OSED5TV5'
url5 = 'https://discord.com/api/webhooks/1091283970374774814/C6KqO35vOdQfhi9pFHL7GS-bhcJyx1dodcwwQF9YdojWnvGb_uhhHAFgNH-t-A_2BIiQ'
url6 = 'https://discord.com/api/webhooks/1091283971960221737/qF0yJi53RYH8v5JJER1WxnW20aFgZGvjoDgYCSxlJN9N36bJRyONliQiziPyxCQ1eKE4'
url7 = 'https://discord.com/api/webhooks/1091283973923151882/OCNtwYSMAYESLgNwL6QYiEwH-rGXvMelrpz_TpQ1kwbl3rMaw4huyvzHpYBPpT0c31Ln'
url8 = 'https://discord.com/api/webhooks/1091283975940608041/fJ9_QtHh7VoYjaik0UhibSALauBueoiuw9Cy9AVCa34mNgE4ipA0M7U-2fgJer4YHcSy'
url9 = 'https://discord.com/api/webhooks/1091283978587213855/1G2XObWgoTrS2qgd3OVafe1t1iRiVZgjMAhQP57Wy9_TZEQvbwL2TKoTJgXXGNOeHv4W'
url10 = 'https://discord.com/api/webhooks/1091283980596289547/jQr50Pm9nOZsER4pDR1Xkoj79e4oncONoBWVAiOXnR5pdjjUmy4bY6m9LMI-OAQcoQu5'
url11 = 'https://discord.com/api/webhooks/1091283982617952346/Bys7RnRSWPhvDAcGYD9T8Fd5YPC_0TjLaFgdLoQGTsknWQvULdzZqB7bIyJjd5_IcF34'
url12 = 'https://discord.com/api/webhooks/1091283984132079669/iPRbcNU6NjShIz6XzstNnUI1Od_YCjfB97SCOmD6mFfaz4c5xfHUsB2u98gFq7xpmcNg'
url13 = 'https://discord.com/api/webhooks/1091283988301234176/Xxz3QJxFxlXVFU9_6fmUFqnJqzBEbsHDwX2EAKfIg00ha-4sBWcNWVXqDXga2egJlBuB'
url14 = 'https://discord.com/api/webhooks/1091283990507421748/VeVKCi9vIi5ymLETtUn-Y8vyZiTxifOU54jhsJqEj_IAm4Ophie6KKsyu3OGqBInOnkb'
url15 = 'https://discord.com/api/webhooks/1091283992797532170/7iE2hLPsk-ScHuciMEVOAg3I9m9hKBjVopVytuPCAcqTrbZ-UYuQBmoqNf6mKkvDXoAQ'


message = {
    'content': f'{outputspam}'
}

headers = {
    'Content-Type': 'application/json'
}

def wh1():
    response = requests.post(url1, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url2, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url3, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url4, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url5, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url6, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url7, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url8, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url9, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url10, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url11, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url12, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url13, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url14, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")
    response = requests.post(url15, headers=headers, data=json.dumps(message))
    if response.status_code == 204:
        print(f"[>] Successfully sent message '{outputspam}'")

# Call send_message every 5 seconds using threading
def repeat_action(interval, action):
    while True:
        threading.Timer(interval, action).start()
        time.sleep(interval)

repeat_action(0, wh1)