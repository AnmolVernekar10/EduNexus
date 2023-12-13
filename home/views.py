from django.http import JsonResponse
from django.shortcuts import render,HttpResponse
from .models import Files,file_name_against_keyword,keyword_against_file_name
import pyrebase
from django.contrib import auth
from django.contrib.auth import authenticate
from collections import OrderedDict
# Create your views here.
#API CREDENTIALS
config={
    "apiKey": "AIzaSyA-0Ej92Ijqp6QWBdIeOLkYu9SV_pkegsQ",
    "authDomain": "test1-3a1ac.firebaseapp.com",
    "projectId": "test1-3a1ac",
    "databaseURL": "https://test1-3a1ac-default-rtdb.firebaseio.com",
    "storageBucket": "test1-3a1ac.appspot.com",
    "messagingSenderId": "1079616842106",
    "appId": "1:1079616842106:web:6bb007499e14b610dacec3",   
}
firebase=pyrebase.initialize_app(config)
#authe=firebase.auth()
authe=firebase.auth()
database=firebase.database()
def signin(request):
    print("signin")
    return render(request,"signin.html")
def postsignin(request):
    print("hi")
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        print("iriroorrkn")
        user=authe.sign_in_with_email_and_password(email,passw)
    except:
        print("hello")
        message="Invalid Credentials"
        return render(request,"signin.html",{"messe":message})
    print("hi1")
    session_id= user['idToken']   
    request.session['uid']=str(session_id)    
    #nm=database.child('Data').child('Name').get().val()
    return render(request,'home_page.html')

def modalTest(request):
    print("Modal Test")
    return render(request,'modalTest.html',{
         "name":"nm",        
    })

def searchfile(request):
    file_list = [
        {'name': 'File 1', 'link': '/media/file1.pdf'},
        {'name': 'File 2', 'link': '/media/file2.pdf'},
        {'name': 'File 3', 'link': '/media/file3.pdf'},
    ]

    return render(request,'searchfile.html',{'l':file_list})
def home_page(request):
    print("signin")
    return render(request,"home_page.html")
def main_page(request):
    if request.method=='POST':
        if 'Upload' in request.POST:
            print("Main Page Post request")
            file2=request.FILES['document']
            document1=Files(file=file2)
            document1.save(file2)
            file_name = document1.filename()

            upload_file(file_name)

            link = download_file(file_name)
            
            s=document1.extract_keyword()
            fileObject=file_name_against_keyword.objects.filter(filename=file_name)
            print("Objects here: ", fileObject)
            print("Document word:",s)

            file_name_against_keyword(filename=file_name, keyword=s).save()
            

            
            extractedKeyWordsList=eval(s)            
            
            for word in extractedKeyWordsList:
                keyWordObj=keyword_against_file_name.objects.filter(keyword=word)
                if keyWordObj.exists():
                    keyObj = keyword_against_file_name.objects.get(keyword=word)
                    files = eval(keyObj.filename)
                    files.append(file_name)
                    files = str(files)
                    keyObj.save()
                else:
                    keyword_against_file_name(keyword = word, filename = f"['{file_name}']").save()

            print(file_name)
            return render(request,'main_page.html') 
        else:
            print("Main Page Post Else")

    nm=database.child('Data').child('Name').get().val()
       
    return render(request,"main_page.html",{
         "name":nm,        
    })


def clear(request):
    keyword_against_file_name.objects.all().delete()
    file_name_against_keyword.objects.all().delete()
    Files.objects.all().delete()

    return JsonResponse({"message":"Cleared"})

def searchTest(request):
    # aaaa
    try:
        temp = request.GET['search']
        mydata = list(keyword_against_file_name.objects.filter(keyword__contains=temp).values())
        keyNameLinkList = []
        for file in mydata:
            print(file["filename"])
            fileNames = eval(file['filename'])
            for fileName in fileNames:
                keyNameLinkList.append([fileName, download_file(fileName)])
        
    except:
        keyNameLinkList = ["No data found"]
    try:
    # if True:
        fileName = list(file_name_against_keyword.objects.filter(filename__contains=temp).values())
        fileNameLinkList = []
        for file in fileName:
            fileNameLinkList.append([file["filename"],download_file(file['filename'])])

        fileNameLinkList.extend(keyNameLinkList)
    except:
        fileNameLinkList = keyNameLinkList
    fileNameLinkList = list(OrderedDict((item[1], item) for item in fileNameLinkList).values())

    return JsonResponse({"fileData":fileNameLinkList})

def searchBar(request):
    return render(request,'searchBar.html')

def logout(request):
    auth.logout(request)
    return render(request,'signin.html')
def signup(request):
    return render(request,'signup.html')
def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    
    try:
        user=authe.create_user_with_email_and_password(email,passw)
    except:
        message="unable to create account try again"
        return render(request,"signup.html",{"messg":message})
    uid=user['localId']
    data={"name":name,"status":"1"}
    database.child("users").child(uid).child("details").set(data)   
    return render(request,"signin.html")

def upload_file(file_name):
    storage = firebase.storage()
    storage.child(f"/Media/{file_name}").put(f"media/{file_name}")

def download_file(file_name):
    storage = firebase.storage()
    return storage.child(f"/Media/{file_name}").get_url(token=None)

def readmore(request):
    print("hi")
    return render(request,"readmore.html")



