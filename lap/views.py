from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from .forms import AddLaptop, Service_request
from .models import Laptop,kpi,repair
from .process import html_to_pdf 
from django.template.loader import render_to_string

# Create your views here.

def test(request):
  laptops = Laptop.objects.all().values()
  template = loader.get_template('base.html')
  context = {
    'laptops': laptops,
  }

  return HttpResponse(template.render(context, request))


def add_laptop(request):
    context ={}

    if request.method == 'POST':
       
       form = AddLaptop(request.POST, request.FILES)

       if form.is_valid():
           serial = request.POST['laptop_serial']
           old_form = form.save(commit=False)
           kpi_age = calculate_kpi("Laptop_age" ,request.POST['laptop_age'])
           kpi_motherboard = calculate_kpi("Motherboard" ,request.POST['motherboard_condition'])
           kpi_display = calculate_kpi("Display" ,request.POST['display_condition'])
           kpi_processor = calculate_kpi("Processor" ,request.POST['processor_age'])
           kpi_speed = calculate_kpi("Speed" ,request.POST['speed'])
           total = kpi_age + kpi_motherboard + kpi_display + kpi_processor + kpi_speed
           
           
           old_form.total_kpi_score = total
           old_form.save()

           #kpisd = kis.sid
           qry = Laptop.objects.filter(laptop_serial= serial).values() | Laptop.objects.order_by('-id').values()
           context['kpi_value'] = calculate_kpi("Laptop_age" ,qry[0]["laptop_age"])
           #qry = Laptop.objects.filter(laptop_serial= serial).values()
           # taking last entry of posted serial
           x = qry[0]["id"]
           return redirect('/laptops/details/'+ str(x))
    
    context['form']= AddLaptop()
    #context['kpi_value'] = calculate_kpi ("Laptop_age","2")
    template = loader.get_template('add-laptop.html')
    return HttpResponse(template.render(context, request))



def service_request(request):
    context ={}

    if request.method == 'POST':
       
       form = Service_request(request.POST, request.FILES)

       if form.is_valid():
           
          form.save()
          return redirect('/')
    
    context['form']= Service_request()
    #context['kpi_value'] = calculate_kpi ("Laptop_age","2")
    template = loader.get_template('service_request.html')
    return HttpResponse(template.render(context, request))




def laptops(request):
  laptops = Laptop.objects.all().values()
  service = repair.objects.all().values()
  template = loader.get_template('all-laptops.html')
  context = {
    'laptops': laptops,
    'service':service,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  context ={}
  laptops = Laptop.objects.get(id=id)
  cd = decision_kpi(laptops.total_kpi_score)
  template = loader.get_template('details.html')
  context = {
    'laptop': laptops,
    'desision': cd
  }
  return HttpResponse(template.render(context, request))


def service_details(request, id):
  context ={}
  service = repair.objects.get(id=id)
  template = loader.get_template('service_details.html')
  context = {
    'service': service,
  }
  return HttpResponse(template.render(context, request))


#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        data = [{'id':24 , 'first_name' : 'shiaft', 'last_name':'you','department':'me'}]
        # getting the template
        open('templates/temp.html', "w").write(render_to_string('result.html', {'data': data}))
        pdf = html_to_pdf('result.html',{})
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


#...................functions 
def calculate_kpi(type_p ,match_string_p):
    qry = kpi.objects.filter(type=type_p, match_string = match_string_p).values()
    return qry[0]['kpi_score']

def decision_kpi(total_kpi):
    desision = "Replace the laptop"
    if total_kpi < 50:
        desision = "Can not replace the Laptop"
    return desision 