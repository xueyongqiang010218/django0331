from django.shortcuts import render,redirect
from app.models import user,department,company
# Create your views here.


def show(request):
    u_all = user.objects.all()
    return render(request, 'index.html', {'u_all':u_all})



def add(request):
    compsny_all = company.objects.all()
    department_all = department.objects.all()
    if request.method == 'GET':
        return render(request, 'add.html',{"compsny_all":compsny_all,"department_all":department_all})
    else:
        username = request.POST.get('username')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        dep_id = request.POST.get('dep_id')
        compsny_id = request.POST.get('company_id')
        d = department.objects.filter(id = dep_id).first()
        c = company.objects.filter(id = compsny_id).first()
        user_e = user(username=username, number=number, gender=gender, dep_id=d, company_id=c)
        user_e.save()
        print(compsny_id)
        return redirect('show')


