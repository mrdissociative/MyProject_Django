from django.shortcuts import render, redirect,HttpResponse
from.models import User, Department, Complaint, Update, Admin
from.forms import fileUploadForm, PasswordChangeForm, RegForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages


#first home page
def homepage(request):
        images = Complaint.objects.all()
        return render(request,'homepage.html',{'i': images})

#user register
def userreg(request):
    if request.method == 'POST':
        member = User(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], date=request.POST['date'],lastname=request.POST['lastname'], gender=request.POST['gender'], phone=request.POST['phone'], address=request.POST['address'], email=request.POST['email'], aadharnumber=request.POST['aadharnumber'])
        member.save()
        return redirect(userlogin)
    else:
        return render(request, 'userreg.html')

#user login
def userlogin(request):
    if request.method == 'POST':
        u1 = request.POST['username']
        p1 = request.POST['password']
        try:
            d = User.objects.get(username=u1)
            if d.password == p1:
                request.session['id'] = u1
                return redirect(userhome)
            else:
                return HttpResponse('erorr')
        except Exception:
            return HttpResponse("Incorrect user name")
    return render(request, "userlogin.html")

#user home
def userhome(request):
    if 'id' in request.session:
        return render(request, "userhome.html")
    else:
        return redirect(userlogin)

#user Logout
def userlogout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request,'userlogin.html')

#change password
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(userlogin)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form': form})

#department registration
def depregister(request):
    if request.method == 'POST':
        member1 = Department(username=request.POST['username'], password=request.POST['password'], firstname=request.POST['firstname'], lastname=request.POST['lastname'],department=request.POST['department'], phone=request.POST['phone'], address=request.POST['address'],email=request.POST['email'])
        member1.save()
        return redirect(deplogin)
    else:
        return render(request,'departmentreg.html')

#department login
def deplogin(request):
    if request.method == 'POST':
        u1 = request.POST['username']
        p1 = request.POST['password']
        d1 = request.POST['department']
        try:
            d = Department.objects.get(username=u1, department=d1)
            if d.password == p1:
                request.session['id'] = u1
                return redirect(dephome)
            else:
                return HttpResponse('erorr')
        except Exception:
            return HttpResponse("Incorrect user name")
    return render(request, "departmentlogin.html")

#department logout
def deplogout(request):
    if 'id' in request.session:
        request.session.flush()
        return render(request, 'departmentlogin.html')

#department home
def dephome(request):
    if 'id' in request.session:
        return redirect(complaintdisplay)
    else:
        return redirect(deplogin)

#user displya
def userdisplay(request):
        data = User.objects.all()
        return render(request, 'userdisplay.html', {'data': data})

#complaint register
def complaintreg(request):
    if request.method == 'POST':
        form = fileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for i in User:
                a = User.objects.get(request.post[i.username])

            b = User.objects.filter(request.post['firstname', 'lastname'])
            c = form.cleaned_data['department']
            d = User.objects.get(request.post['phone'])
            e = form.cleaned_data['address']
            f = form.cleaned_data['issue']
            g = form.cleaned_data['file']
            data = Complaint(username=a, name=b, department=c, phone=d, address=e, issue=f, file=g)
            data.save()
            return render(request, "userhome.html")

        else:
            return HttpResponse("Error")
    else:
        return render(request, "complaintreg.html")

def department_complaints(request, department_id):
    department = Department.objects.get(id=department_id)
    complaints = Complaint.objects.filter(department=department)
    return render(request, 'department_complaints.html', {'department': department, 'complaints': complaints})


#complaint display
def complaintdisplay(request):
    images = Complaint.objects.all()
    return render(request, "complaintdisplay.html", {'i': images})

#complaint update page for admin
def update(request):
    if request.method == "POST":
        data = update(comment=request.POST['comment'])
        data.save()
        return redirect(updateview)
    return HttpResponse('error')

#complaint update view page for admin
def updateview(request):
    data = Update.objects.all()
    return render(request,"complaintdisplay.html",{'text': data})

#test page
def test(request):
    images = Complaint.objects.all()
    return render(request,"test.html",{'i':images})

#user complaint display page
def usercomplaint(request):
    if request.method == 'POST':
        if request.member.is_authenticated:
            data = User.objects.filter(member=request.member)
            return render(request, 'userhome.html', {'data': data})

def complaintdisp(request):
    if request.method == 'POST':
        images = Complaint.objects.all()
        return render(request, "complaintdisplay.html", {'i': images})

#user delete page
def userdelete(request):
    User.objects.filter(Member=request.member).delete()

#gmail
def gmail(request):
    return redirect()


#-------------------ADMIN---------------------------

# admin profile
def adminlogin1(request):
    if 'id' in request.session:
        if request.method == 'GET':
            u = User.objects.all()
            d = Department.objects.all()
            c = Complaint.objects.all()
            return render(request, 'admin_profile.html', {'data': u, 'data1': d, 'data2':c})
        return render(request, 'admin_profile.html')
    else:
        return redirect(adminlogin)

#admin login
def adminlogin(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']
        try:
            d = Admin.objects.get(username=uname)

            if d.password == pword:
                request.session['id'] = uname
                return redirect(adminlogin1)
            else:
                return HttpResponse("Incorrect Password")
        except Exception:
            return HttpResponse("Incorrect username")
    return render(request, 'ADMIN.html')

#admin logout
def adminlogout(request):
    if 'id' in request.session:
        request.session.flush()
        return redirect(adminlogin)


#about page
def about(request):
    return render(request, "about.html")

#support page
def support(request):
    return render(request, "support.html")

#contact page
def contact(request):
    return render(request,"contact.html")

#Terms and conditions page
def terms(request):
    return render(request,"terms.html")


# for profile view
# def user_profile(request, username):
#     # Get the User object from the database
#     try:
#         user = User.objects.get(username=username)
#     except User.DoesNotExist:
#         return HttpResponse("User not found", status=404)
#
#     # Get the User's posts from the database
#     posts = Post.objects.filter(user=user)
#
#     # Render the template with the User and Post objects
#     context = {'user': user, 'posts': posts}
#     return render(request, 'user_profile.html', context)

def search(request):
    if request.method == 'POST':
        s = request.POST['user']
        data = User.objects.filter(username=s)
        return render(request, 'usersearch.html',{'t':data})
    else:
        return render(request, 'usersearch.html')

