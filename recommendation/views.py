from django.http import HttpResponseRedirect
from django.shortcuts import render
from university.models import SavedItems, University, UniversitiesCount
from profiles.models import Profile


def recommendation(request):
    profile = Profile.objects.get(student=request.user)
    gaurdian_income = profile.gaurdian_income
    matric_marks = profile.matric_marks
    matric_grade = profile.matric_grade
    inter_marks = profile.inter_marks
    inter_grade = profile.inter_grade
    university_name = profile.university_name
    field_of_interest = profile.field_of_interest
    matric_marks_percentange = (matric_marks / 1100) * 30
    inter_marks_percentange = (inter_marks / 1100) * 70
    final_percentange = matric_marks_percentange + inter_marks_percentange

    query = University.objects.filter(program_abbreviation=field_of_interest, last_merit__lte=final_percentange)
    query2 = UniversitiesCount.objects.order_by('-count')[:5]
    # query3 = UniversitiesCount.objects
    # query4 = University.objects.filter(university_name=university_name, program_abbreviation=field_of_interest)
    # print(query4)
    # for value in query4:
    #     if university_name == "University of Education":
    #         print(value.last_merit)
    #         merit = value.last_merit
    #         print(final_percentange)
    #     #     GC mn test or 50% inter (cs) test 30 inter 70 (ee)
    #     #      itu 50 matric above 60 inter aboyve 60 (50% test)
    #     #     lc ecat (ee) (archi test based)
    #     else:
    #         print("no")
    query5 = University.objects.filter(program_abbreviation=field_of_interest, fee_structure__lte=gaurdian_income)

    return render(request, "recommendation.html",
                  context={'final_query': query, 'final_query2': query2, 'final_query5': query5})


def savedlinks(request):
    query = SavedItems.objects.filter(user=request.user)
    # if request.method == 'POST':
    #     query.delete()
    #     return HttpResponseRedirect ("/")
    return render(request, "saved.html", context={'query': query})


def aboutus(request):
    return render(request, "AboutUs.html")
