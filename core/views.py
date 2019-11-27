from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login as dj_login

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
User = get_user_model()

def indexx(request):
     return render(request, 'index.html') 


def index(request):
    try:
        a=PhoneDevice.objects.filter(user=request.user)
        if a:
            return render(request, 'index.html')
        else:
            return render(request, 'index.html')

    except PhoneDevice.DoesNotExist:
        a = None

def signup(request):
    if request.method == 'POST':
        print("asdas")
        form = SignUpForm(request.POST)
        # print("dsaf")
        if form.is_valid():
            print("dsaf")
            form.save()
            username= form.cleaned_data['username']
            email = form.cleaned_data['email']
            phone= form.cleaned_data['phone']
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            return redirect('indexx')
    else:
         form = SignUpForm()    
    return render(request, "registration/signup.html", {'form': form})       


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         user = authenticate(username=request.POST['username'] ,password=request.POST['password'])

#         if user is not None:
#             if user.is_active:
#              dj_login(request, user)
#              return redirect('startt') 
#     else:
#         form = LoginForm()   
        
#     return render(request, "registration/login.html", {'form': form})        


def error(request):
    return render(request, "error.html")        

def start_quiz(request):
    user = request.user
    user1 = User.objects.get(id=user.id)
    users = Uscore.objects.filter(student_id=user1.id)
    form = StartForm(request.POST)
    if form.is_valid():
        if not users:
            uid= form.cleaned_data['username']
            request.session["user"] =uid
            request.session['ans'] = ""
            request.session['exclude_id'] = ""
            request.session['score'] = 0
            return redirect("questions")
        else:
            return redirect('error')     
    return render(request, "start.html", {'form': form})
               

def question_view(request):
    # imprt ipdb; ipdb.set_trace()
    answer = request.POST.get('ans')
    # print("ans = ", answer)
    if answer:
        request.session['ans'] = f"{request.session['ans']},{answer}"
        
    exclude_ids = request.session['exclude_id'].split(",")
    exclude_ids = [int(x) for x in exclude_ids if x]
    questions = Question.objects.exclude(id__in=exclude_ids)
    if questions.exists():
        question = questions.first()
        request.session['exclude_id'] = f"{request.session['exclude_id']},{question.id}"
        return render(request, "startq.html", {'question':question, 'id':question.id})
    return redirect('answers')



def submit_quiz(request):
    data = request.session.get('ans')
    # import ipdb; ipdb.set_trace()
    if data:
        data = data.split(',')
        data = [x for x in data if x]
    questions_id = request.session['exclude_id'].split(',')
    print(questions_id)
    questions_id = [int(x) for x in questions_id if x]
    print(questions_id)
    score = 0
    for i, ques in enumerate(questions_id):
        print(i)
        print(ques)
        if i >= 0:
            result = Question.objects.filter(id=ques,answer=data[i])
            
            if result.exists():
                print(result)
                score = str(int(score)+5)
    data=(', '.join(data))  
    s= Uscore.objects.create(score=score,answer1=data)
    s.save()
    s.student = User.objects.get(username=request.user)
    s.save()
    return render(request,'answer.html',{'score':score})
  

  
def check_answer(request,student_id):
    adr=Question.objects.all()
    adrr=Uscore.objects.filter(student_id=student_id)
    context = {
            'adr':adr, 
            'adrr':adrr, 
    }
    return render(request,'checkans.html',context=context)










