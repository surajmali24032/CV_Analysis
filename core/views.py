from django.shortcuts import redirect, render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from core.models import Question
from core.models import Skill
import docx2txt
import os
from pathlib import Path
import sys
# from core.models import showGraph


# ml 
import math
from textblob import TextBlob as tb
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# from . import forms
from .  import models
BASE_DIR = Path(__file__).resolve().parent.parent




# upload function
def upload(request):

    if request.method == 'POST':
        # Passing docx file to process function
        # fileloc = os.path.join(BASE_DIR,'core\static\downloads\cv template.docx')
        # uploaded_file = request.FILES['file']
        # text = docx2txt.process("C:/Users/Pratik/Desktop/CV Analysis/CV Analysis/cv's/cvtemplate.docx")
        text = docx2txt.process(request.FILES['file'])
        # fs = FileSystemStorage()
        # fs.save(uploaded_file.name, uploaded_file)
        with open("core/cv.txt", "w") as text_file:
	        print(text, file=text_file)


# TF-IDF Algorithm

    def tf(word, blob):
        return blob.words.count(word) / len(blob.words)

    def n_containing(word, bloblist):
        return sum(1 for blob in bloblist if word in blob.words)

    def idf(word, bloblist):
        return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

    def tfidf(word, blob, bloblist):
        return tf(word, blob) * idf(word, bloblist)

    script_dir = os.path.dirname(__file__)
    rel_path = "cv.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, 'r') as file:
        data = file.read().replace('\n', ' ')
# txtdata = pd.read_table('C:/Users/Pratik/Desktop/CV Analysis/CV Analysis/cv.txt')
# document1 = tb("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of python program maintenance. Python supports modules and packages, which python encourages program modularity and code reuse.")

    document2 = tb("")
    print(data)

    lematized_data_token = word_tokenize(data)
    tokens_without_sw = [word for word in lematized_data_token if not word in stopwords.words()]
    # print(tokens_without_sw)
    filtered_sentence = (" ").join(tokens_without_sw)
    filtered_sentence = filtered_sentence.upper()
    # print(filtered_sentence.upper())
    doc2 = tb('"'+filtered_sentence+'"')
    print(doc2)
    # docs2 = doc2.upper()

    document3 = tb("")

    bloblist = [doc2, document2, document3]

    lst = []
    nlst = []

    for i, blob in enumerate(bloblist):
        print("Top words in document" .format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key = lambda x: x[1], reverse = True)
        for word, score in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}" .format(word, round(score, 5)))
            lst.append(word)
            nlst.append(score)
            
            # lst = sorted_words[:3]
    # print(lst)
    s1 = lst[0]
    s2 = lst[1]
    s3 = lst[2]

    sv1 = nlst[0]
    sv2 = nlst[1]
    sv3 = nlst[2]


    user = request.user
    models.Skill.objects.create(user=user, s1=s1, s2 = s2, s3 = s3, sv1 = sv1, sv2 = sv2, sv3 = sv3)
    return render(request, 'core/loggedIn.html')




def home(request):
    return render(request, 'core/home.html', {'navbar': 'home'})

def aboutus(request):
    return render(request, 'core/aboutus.html', {'navbar': 'aboutus'})

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        # skills = ("")

        if pass1 != pass2:
            messages.warning(request, 'Password Does not match')    
            return redirect('register')

        elif User.objects.filter(username = uname).exists():
               messages.warning(request,'username already exists')
               return redirect('register')

        elif User.objects.filter(email = email).exists():
               messages.warning(request,'email already exists')
               return redirect('register')       

        else:
            user = User.objects.create_user(first_name=fname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request, 'User has been Registered successfully')
            return redirect('login')

    return render(request, 'core/register.html', {'navbar': 'register'})

def loggedIn(request):
    messages.success(request, "Logged in successfully!")
    return render(request, 'core/loggedIn.html')

def start_apti(request):
    return render(request, 'core/start_apti.html')





def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('loggedIn')

        else:
            messages.warning(request,'Invalid credentials')
            return redirect('register')
    return render(request, 'core/login.html', {'navbar': 'login'})


def user_logout(request):
    logout(request)
    messages.warning(request, "Logged out successfully!")
    return redirect('/')

    





def apti(request):
    question = models.Question.objects.filter().order_by('id').first()
    return render(request, 'core/apti.html', {"question": question})




def submit_answer(request, quest_id):
    if request.method == 'POST':
        question = models.Question.objects.filter(id__gt=quest_id).exclude(id=quest_id).order_by('id').first()   
        if 'skip' in request.POST:
            if question:
                quest = models.Question.objects.get(id=quest_id)
                user = request.user
                answer = 'not Submitted'
                models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)
                return render(request,'core/apti.html', {'question':question})


        else:
            quest = models.Question.objects.get(id=quest_id)
            user = request.user
            answer = request.POST['answer']
            models.UserSubmittedAnswer.objects.create(user=user, question=quest, right_answer=answer)        
        if question:
            return render(request, 'core/apti.html', {"question": question})

        else:
            result = models.UserSubmittedAnswer.objects.filter(user=request.user)
            skipped = models.UserSubmittedAnswer.objects.filter(user=request.user, right_answer='Not Submitted').count()
            attempted = models.UserSubmittedAnswer.objects.filter(user=request.user).exclude(right_answer='Not Submitted').count()
            rightAns = 0
            percentage = 0
            for row in result:
                if row.question.right_opt == row.right_answer:
                    rightAns += 1
            percentage = (rightAns * 100)/result.count() 

            return render(request, 'core/result.html', {"result": result, 'total_skipped':skipped, 'attempted':attempted, 'rightAns':rightAns, 'percentage':percentage,})

            # return HttpResponse("No more questions")

    else:
        return HttpResponse('Method not allowed!!')    



