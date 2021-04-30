from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def personal_data(request):
    data = {
        "full_name":"anjan kumar",
        "Qualification": "Btech",
        "Skills":["python","jango","html"]
    }
    return render(request,"apps/file.html",{"my_data": data})


def forms(request):
    if request.method == "POST":
        # import pdb;
        # pdb.set_trace()
        data1 = {
            "From mail ": request.POST["from_mail"],
            "To mail" : request.POST["to_mail"],
            "Email Subject" : request.POST["email_subject"],
            "Email Body" : request.POST["email_body"]
        }
        return HttpResponse(f"SUCCESS: {data1}")
    else:
        return render(request,"apps/forms.html")