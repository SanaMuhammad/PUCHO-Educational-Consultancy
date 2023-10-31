from django.shortcuts import render
from .models import University,SavedItems,UniversitiesCount

def gcuni(request):
    uni_name = request.path.split('/')[1].upper()
    query = UniversitiesCount.objects.get(university_name__contains=uni_name)
    query.count = query.count + 1
    query.save()
    return render(request, "GCuni.html", context={'query':query,})

def gcdepts(request,deptname):
    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper()+ ' '+ page_url.split('/')[4])

    query = University.objects.filter(university_name__contains='Government College University Lahore',program_abbreviation__contains=deptname)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    query = SavedItems.objects.filter(item_page__contains=page_url,user=request.user)
    if query:
        context['saved'] = True
    if request.method == "POST":
        print("post request")
        query = SavedItems(user=request.user,item_page=page_url,item_name=page_name)
        query.save()
        return render(request, "GCdepartments.html",context)
    return render(request, "GCdepartments.html",context)
  
def ituuni(request):
    uni_name = request.path.split('/')[1].upper()
    query = UniversitiesCount.objects.get(university_name__contains=uni_name)
    query.count = query.count + 1
    query.save()
    return render(request, "ITUuni.html")

def itudepts(request,deptname):
    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper() + ' ' + page_url.split('/')[4])

    query = University.objects.filter(university_name__contains='Information Technology University',program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    query = SavedItems.objects.filter(item_page__contains=page_url,user=request.user)
    if query:
        context['saved'] = True
    if request.method == "POST":
        query = SavedItems(user=request.user,item_page=page_url,item_name=page_name)
        query.save()
        return render(request, "ITUdepartments.html",context)
    return render(request, "ITUdepartments.html",context)

def kcuni(request):
    uni_name = request.path.split('/')[1].upper()
    query = UniversitiesCount.objects.get(university_name__contains=uni_name)
    query.count = query.count + 1
    query.save()
    return render(request, "KCuni.html")

def kcdepts(request,deptname):
    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper() + ' ' + page_url.split('/')[4])

    query = University.objects.filter(university_name__contains="Kinnard College For Women University",program_abbreviation__contains=deptname)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    query = SavedItems.objects.filter(item_page__contains=page_url,user=request.user)
    if query:
        context['saved'] = True
    if request.method == "POST":
        query = SavedItems(user=request.user,item_page=page_url,item_name=page_name)
        query.save()
        return render(request, "KCdepartments.html",context)
    return render(request, "KCdepartments.html",context)
  
def lcwuuni(request):
    uni_name = request.path.split('/')[1].upper()
    query = UniversitiesCount.objects.get(university_name__contains=uni_name)
    query.count = query.count + 1
    query.save()
    return render(request, "LCWUuni.html")

def lcwudepts(request,deptname):
    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper() + ' ' + page_url.split('/')[4])

    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper() + ' ' + page_url.split('/')[4])

    query = University.objects.filter(university_name__contains='Lahore College for Women University') and University.objects.filter(program_abbreviation__contains=deptname)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    query = SavedItems.objects.filter(item_page__contains=page_url,user=request.user)
    if query:
        context['saved'] = True
    if request.method == "POST":
        query = SavedItems(user=request.user,item_page=page_url,item_name=page_name)
        query.save()
        return render(request, "LCWUdepartments.html",context)
    return render(request, "LCWUdepartments.html",context)

def uetuni(request):
    uni_name = request.path.split('/')[1].upper()
    query = UniversitiesCount.objects.get(university_name__contains=uni_name)
    query.count = query.count + 1
    query.save()
    return render(request, "UETuni.html")

def uetdepts(request,deptname):
    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper() + ' ' + page_url.split('/')[4])

    query = University.objects.filter(university_name__contains='University of Engineering and Technology',program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    query = SavedItems.objects.filter(item_page__contains=page_url,user=request.user)
    if query:
        context['saved'] = True
    if request.method == "POST":
        query = SavedItems(user=request.user,item_page=page_url,item_name=page_name)
        query.save()
        return render(request, "UETdepartments.html",context)
    return render(request, "UETdepartments.html",context)
  
def ueuni(request):
    uni_name = request.path.split('/')[1].upper()
    query = UniversitiesCount.objects.get(university_name__contains=uni_name)
    query.count = query.count + 1
    query.save()
    return render(request, "UEuni.html")

def uedepts(request,deptname):
    page_url = str(request._current_scheme_host + request.path)
    page_name = ((page_url.split('/')[3]).upper() + ' ' + page_url.split('/')[4])

    query = University.objects.filter(university_name__contains='University of Education',program_abbreviation__contains=deptname)
    print(query)
    for value in query:
        program_name = value.program_name
        eligibilty_criteria = value.eligibilty_criteria
        fee_structure = value.fee_structure
        last_merit = value.last_merit
    context = {'program_name': program_name,
    'eligibilty_criteria': eligibilty_criteria,
    'fee_structure': fee_structure,
    'last_merit': last_merit,
    }
    query = SavedItems.objects.filter(item_page__contains=page_url,user=request.user)
    if query:
        context['saved'] = True
    if request.method == "POST":
        query = SavedItems(user=request.user,item_page=page_url,item_name=page_name)
        query.save()
        return render(request, "UEdepartments.html",context)
    return render(request, "UEdepartments.html",context)
