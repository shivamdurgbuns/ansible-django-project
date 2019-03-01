# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'home.html', context=None)

def take_view(request):
          package = request.GET.get('pname')
          f = open( '/django_project/ekaurbaaar/files/indata', 'w+' )
          f.write( package )
          f.close()
          hostname= request.GET.get('hname')
          f = open( '/django_project/ekaurbaaar/files/hdata', 'w+' )
          f.write( hostname )
          f.close()   
          import os
          cmd = 'ansible-playbook /django_project/ekaurbaaar/files/install.yml'
          os.system(cmd)

          return HttpResponse('Package installed')
