from django.shortcuts import render
import requests

# Create your views here.

def mainpage(request):
    if request.method =='POST':
        username = request.POST['UserName']
        email = request.POST['email']
        password = request.POST['password']

        API_ENDPOINT = "http://fone.me/api/account/v1/register"
        data = {'UserName': username,
                 'Name': email,
                 'Password': password,
                 'CountryCode': "20",
                 'NumberWithOutCode': '14313124134143',
                   'PhoneNumber': '24555245245245',
                   "Email": email
                }


        r = requests.post(url=API_ENDPOINT, data=data)

    # extracting response text
        pastebin_url = r.text
        print("The pastebin URL is:%s" % pastebin_url)

    return render(request, 'login/login.html')



def profile(request):
    return render(request, 'login/profile.html')