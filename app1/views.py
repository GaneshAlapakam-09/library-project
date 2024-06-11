from django.shortcuts import render,redirect

from django.contrib.auth.models import User

from app1.models import BookManagement,Student

from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from datetime import datetime,date,timedelta


# Create your views here.

def home(request):
    return render(request,'home.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        staff = User.objects.filter(is_staff=True)
        for person in staff:
            temp = str(person)
            if temp == username:
                if user:
                    login(request,user)
                    return redirect('staff')
            
        if user is not None:
            login(request,user)
            return redirect('student')
        else:
            messages.info(request,"username and password doesn't match")
            return redirect('signin')
    return render(request,'signin.html')

def signup(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassowrd = request.POST['confirmpassword']
        users = User.objects.all()
        for user in users:
            temp = str(user)
            if username == temp:
                messages.info(request,'user :'+ username +' is already exist')
                return redirect('signup')
        if password == confirmpassowrd:
            person = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
            return redirect('signin')
        else:
            messages.info(request,'please enter same password')
            return redirect('signup')
        
    return render(request,'signup.html')

@login_required(login_url='signin')
def bookadd(request):
    staff = User.objects.filter(is_staff=True)
    current_user = request.user.username
    for person in staff:
        temp = str(person)
        if temp == current_user:
            if request.method == 'POST': 
                title = request.POST['title']
                author = request.POST['author']
                due = request.POST['publication']
                stock = request.POST['stock']
                publication =datetime.strptime(due,"%Y-%m-%d")
                current_date=datetime.today()
                if publication > current_date:
                    messages.info(request,'publication should be earlier to Today -OR- today')
                    return redirect('bookadd')
                BookManagement.objects.create(title=title,author=author,publication=publication,stock=stock,uid_id=request.user.id,available_stock=stock)
                return redirect('staff')
            return render(request,'bookadd.html')
    messages.info(request,'you are not staff to add books')
    return redirect('student')

@login_required(login_url='signin')
def bookremove(request,id):
    staff = User.objects.filter(is_staff=True)
    current_user = request.user.username
    for person in staff:
        temp = str(person)
        if temp == current_user:
            book = BookManagement.objects.filter(id=id).delete()
            return redirect('staff')
    messages.info(request,'you are not staff to remove books')
    return redirect('student')


@login_required(login_url='signin')
def staff(request):
    student = Student.objects.all()
    current_date=date.today()
    for record in student:
        if record.due < current_date and record.position == 'not returned':
            Student.objects.filter(due=record.due).update(status='overdue',fine=100)
    staff = User.objects.filter(is_staff=True)
    current_user = request.user.username
    for person in staff:
        temp = str(person)
        if request.method =="POST":
            book = request.POST['book']
            books = BookManagement.objects.all()
            if book:
                student = Student.objects.filter(book=book)
            context={'book':books,'student':student}
            return render(request,'staff.html',context)
        if temp == current_user:
            books = BookManagement.objects.all()
            student = Student.objects.all()
            context={'book':books,'student':student}
            return render(request,'staff.html',context)
    messages.info(request,'you are not staff')
    return redirect('student')

@login_required(login_url='signin')
def student(request):
    books = BookManagement.objects.all()
    student_table = Student.objects.all()
    current_date=date.today()
    data = Student.objects.all()
    for record in data:
        if record.due < current_date and record.position == 'not returned':
            Student.objects.filter(due=record.due).update(status='overdue',fine=100)
    duestatus=Student.objects.filter(position='returned').update(status='no due',fine = 0)
    for item in books:
        count = 0
        for books in student_table:
            if books.book == item.title and books.position == 'not returned':
                count+=1
            if count == item.stock:
                BookManagement.objects.filter(id=item.id).update(status='Unavailable')
            if count < item.stock:
                BookManagement.objects.filter(id=item.id).update(status='Available')
            BookManagement.objects.filter(id=item.id).update(available_stock = item.stock - count)
            
    
    books = BookManagement.objects.all()
    student = Student.objects.filter(uid_id=request.user.id,position='not returned')

    context={'book':books,'student':student}
    return render(request,'student.html',context)

@login_required(login_url='signin')
def get(request,id):
    if request.method == "POST":
        name = request.user.username
        book = BookManagement.objects.get(id=id)
        due = request.POST['due']
        htmldue = request.POST['due']
        due =datetime.strptime(htmldue, "%Y-%m-%d")
        current_date=datetime.today()
        if due <= current_date:
            messages.info(request,'due date should be after today')
            return redirect('get',id)
        Student.objects.create(book=book,due=due,name=name,uid_id=request.user.id)
        return redirect('student')
    return render(request,'due.html')
    
@login_required(login_url='signin')
def returned(request,id):
    Student.objects.filter(id=id).update(position='returned')
    return redirect('student')

@login_required(login_url='signin')
def returned_items(request):
    returneditems = Student.objects.filter(uid_id=request.user.id)
    return render(request,'returned_items.html',{'returneditems':returneditems})

def signout(request):
    logout(request)
    return redirect('signin')
