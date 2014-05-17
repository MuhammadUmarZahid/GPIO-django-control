# Create your views here.
from django.http import HttpResponse
# Create your views here.
from django.template import RequestContext, loader
from led.models import Led
from django.shortcuts import render
import RPi.GPIO as GPIO
from django.utils import timezone
 
def index(request):
    latest_poll_list = Led.objects.order_by('-change')[:5]
    template = loader.get_template('led/index.html')
    context = RequestContext(request, {
                             'latest_poll_list': latest_poll_list,
                             })
    return HttpResponse(template.render(context))

def detail(request, led_id):
    try:
	GPIO.setmode(GPIO.BOARD)       
	led = Led.objects.get(pk=led_id)
	
	if led.stat==0:
		GPIO.setup(led.pin,GPIO.OUT)
		GPIO.output(led.pin,False)
		led.stat=1
		led.save()
		led.change=timezone.now()
		led.save()
			
    except Led.DoesNotExist:
        raise Http404
    return render(request, 'led/detail.html', {'led': led})

def detailoff(request, led_id):
    try:
        GPIO.setmode(GPIO.BOARD)
        led = Led.objects.get(pk=led_id)

        if led.stat==1:
                GPIO.setup(led.pin,GPIO.OUT)
                GPIO.output(led.pin,True)
                led.stat=0
                led.save()
                led.change=timezone.now()
                led.save()

    except Led.DoesNotExist:
        raise Http404
    return render(request, 'led/detail.html', {'led': led})
