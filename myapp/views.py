from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random

def sayhello(request):
    return HttpResponse('sayhello....')

def hello2(request, username):
    now = datetime.now()
    return render(request, 'hello3.html', locals())
 
def hello4(request, username):
    now = datetime.now()
    return render(request, 'hello4.html', locals())
    
def test_dict(request):
    dict1 = {'key1': 123, 'key2': 456}
    return render(request, 'hello4.html', dict1)
    
def dice(request):
    no = random.randint(1, 6)
    return render(request, "dice.html", {"no":no})
    
def dice2(request):
    no1 = random.randint(1, 6)
    no2 = random.randint(1, 6)
    no3 = random.randint(1, 6)
    return render(request, "dice2.html", locals())
    
times = 0
def dice3(request):
    global times
    times = times + 1
    local_times = times
    username = "雪雪"
    dict_no = {"no":random.randint(1,6)}
    return render(request, "dice3.html", locals())
  
def show(request):
    person1={"name":"雪雪", "phone":"049-1234567", "age":20}
    person2={"name":"雪雪2","phone":"02-4455666", "age":25}
    person3={"name":"3333", "phone":"04-9876543", "age":17}
    persons=[person1, person2, person3]
    return render(request, "show.html", locals())
    
    #Todo 9*9 multiplication table
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{j} x {i} = {j * i}', end = '\t')
        print('')
    return render(request, "show.html", locals())    
  