from django.shortcuts import render
from . forms import contactForm

def home(request):
    return render(request,'./first_app/home.html')



def about(request):
        return render(request,'./first_app/about.html',)
   
 
   
   
def form(request):
    if request.method=='POST':
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request,'./first_app/form.html',{'name':name,'email':email,'select':select})
    
    else:
        return render(request,'./first_app/form.html',)




def Django_form(request):
    if request.method=='POST':
        form=contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['FILES']
          
            with open('./first_app/upload/' +file.name,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                 
        print(form.cleaned_data)  
    else:
        form=contactForm() 
        
    return render(request,'./first_app/django_form.html',{'form':form})   
    


   
       
   
