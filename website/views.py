from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import MedicalReport
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mediscanner.analyzer import analyze_medical_report


@login_required(login_url='website:result')
def reports_list(request):
    reports = MedicalReport.objects.filter(user=request.user)
    return render(request, "website/reports.html", {"reports": reports})

def upload_page(request):
    return render(request, "website/upload.html")

def result_page(request):
    return render(request, "website/result.html")

def analyze_report(request):
    if request.method == "POST":
        file = request.FILES.get("report")

        if not file:
            return render(request, "website/upload.html", {
                "error": "Please upload a file"
            })

        result = analyze_medical_report(file)
        MedicalReport.objects.create(
            user=request.user if request.user.is_authenticated else None,
            report_file=file,
            analysis=result
        )
        

        return render(request, "website/result.html", {
            "analysis": result
        })

    return render(request, "website/upload.html")



def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('website:signup')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('website:signin')

    return render(request, 'website/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('website:dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('website:signin')

    return render(request, 'website/signin.html')


@login_required(login_url='website:signin')
def dashboard(request):
    return render(request, 'website/dashboard.html')



def index(request):
    return render(request, 'website/index.html')

def ai_doctor(request):
    return render(request, 'website/ai-doctor.html')

def lab_test(request):
    return render(request, 'website/lab-test.html')

def second_opinion(request):
    return render(request, 'website/second-opinion.html')

def blog(request):
    return render(request, 'website/blog.html')

def symptoms_guide(request):
    return render(request, 'website/symptoms-guide.html')

def knowledge_base(request):
    return render(request, 'website/knowledge-base.html')

def glossary(request):
    return render(request, 'website/glossary.html')

def pricing(request):
    return render(request, 'website/pricing.html')

def forgot_password(request):
    return render(request, 'website/forgot-password.html')

