from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#from django.views.generic import TemplateView

#class cbv_html(TemplateView):
#    template_name='cbv_html.html'

from django.views.generic import TemplateView

class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs) :
        EDCO=super().get_context_data(**kwargs)
        
        EDCO['name']="manoj"
        EDCO['age']=22
        return EDCO



class cbv_topic(TemplateView):
    template_name='cbv_topic.html'

    def get_context_data(self, **kwargs) :
        EDCO=super().get_context_data(**kwargs)
        
        TFO=Topicform()
        d={'TFO':TFO}
        EDCO[TFO]='cricket'
        return EDCO
    
    def post(self,request):
        return HttpResponse('topic inserted successfully......')



