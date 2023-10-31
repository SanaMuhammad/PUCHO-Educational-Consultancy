from django.shortcuts import render,redirect

from feedback.models import Feedback
from .models import Profile


def form(request):
    data = Profile.objects.filter(student = request.user).exists()
    if data:
        return redirect("/recommendation")

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        religion = request.POST.get("religion")
        nationality = request.POST.get("nationality")
        gaurdian_name = request.POST.get("gaurdian_name")
        gaurdian_income = request.POST.get("gaurdian_income")
        name_of_school = request.POST.get("name_of_school")
        matric_marks = request.POST.get("matric_marks")
        year_of_matric = request.POST.get("year_of_matric")
        matric_grade = request.POST.get("matric_grade")
        matric_board = request.POST.get("matric_board")
        name_of_college = request.POST.get("name_of_college")
        inter_marks = request.POST.get("inter_marks")
        year_of_inter = request.POST.get("year_of_inter")
        inter_grade = request.POST.get("inter_grade")
        inter_board = request.POST.get("inter_board")
        university_name = request.POST.get("university_name")
        field_of_interest = request.POST.get("field_of_interest")
        print(field_of_interest)
        query = Profile(full_name=full_name, email=email, phone_number=phone_number, address=address, city=city, gender=gender, age=age,religion=religion, nationality=nationality, gaurdian_name=gaurdian_name, gaurdian_income=gaurdian_income, name_of_school=name_of_school, matric_marks=matric_marks, year_of_matric=year_of_matric, matric_grade=matric_grade, matric_board=matric_board, name_of_college=name_of_college, inter_marks=inter_marks, year_of_inter=year_of_inter, inter_grade=inter_grade,  inter_board=inter_board, university_name=university_name, field_of_interest=field_of_interest,student=request.user)
        query.save()
        return redirect("/recommendation")
    return render(request, "form.html")


def profile(request):
    query = Profile.objects.get(student=request.user)
    return render(request, "profile.html", {"query":query})


def home(request):
    query = Feedback.objects.all()
    return render(request, "home.html", {"feedback_query":query})


def edit(request):
    query = Profile.objects.get(student=request.user)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
        city = request.POST.get("city")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        religion = request.POST.get("religion")
        nationality = request.POST.get("nationality")
        gaurdian_name = request.POST.get("gaurdian_name")
        gaurdian_income = request.POST.get("gaurdian_income")
        name_of_school = request.POST.get("name_of_school")
        matric_marks = request.POST.get("matric_marks")
        year_of_matric = request.POST.get("year_of_matric")
        matric_grade = request.POST.get("matric_grade")
        matric_board = request.POST.get("matric_board")
        name_of_college = request.POST.get("name_of_college")
        inter_marks = request.POST.get("inter_marks")
        year_of_inter = request.POST.get("year_of_inter")
        inter_grade = request.POST.get("inter_grade")
        inter_board = request.POST.get("inter_board")
        university_name = request.POST.get("university_name")
        field_of_interest = request.POST.get("field_of_interest")
        print(field_of_interest, university_name, inter_grade, inter_board)

        query.full_name = full_name
        query.email = email
        query.phone_number = phone_number
        query.address = address
        query.city = city
        query.gender = gender
        query.age = age
        query.religion = religion
        query.nationality = nationality
        query.gaurdian_name = gaurdian_name
        query.gaurdian_income = gaurdian_income
        query.name_of_school = name_of_school
        query.matric_marks = matric_marks
        query.year_of_matric = year_of_matric
        query.matric_grade = matric_grade
        query.matric_board = matric_board
        query.name_of_college = name_of_college
        query.inter_marks = inter_marks
        query.year_of_inter = year_of_inter
        query.inter_grade = inter_grade
        query.inter_board = inter_board
        query.university_name = university_name
        query.field_of_interest = field_of_interest
        query.save()
    return render(request, "edit.html",{"query":query})

