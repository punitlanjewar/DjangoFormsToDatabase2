from django.shortcuts import redirect, render

from App1.models import BikeData

# Create your views here.
def home_fun(request):
    return render(request, 'index.html')


def bike_fun(request):
    b1 = BikeData()
    b1.bike_company = request.POST['txtCompanyName']
    b1.bike_name = request.POST['txtBikeName']
    b1.bike_fueltype = request.POST['selFuelType']
    b1.bike_modelyear = request.POST['txtModelYear']
    b1.save()
    return render(request, 'index.html', {'Msg': 'Data Added Successfully'})


def disp_fun(request):
    data = BikeData.objects.all()  # return list of objects
    return render(request, 'bikedata.html', {'bike': data})


def update_fun(request, id):
    b1 = BikeData.objects.get(id=id)
    if request.method == 'POST':
        b1.bike_company = request.POST['txtCompanyName']
        b1.bike_name = request.POST['txtBikeName']
        b1.bike_fueltype = request.POST['selFuelType']
        b1.bike_modelyear = request.POST['txtModelYear']
        b1.save()
        return redirect('display')
    else:
        return render(request, 'updatedata.html', {'Msg': 'Update Successfully'})
    

def del_fun(request, id):
    b1 = BikeData.objects.get(id=id)
    b1.delete()
    return redirect('display')
