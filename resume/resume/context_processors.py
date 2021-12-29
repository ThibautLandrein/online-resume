# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:46:05 2021

@author: Thibaut
"""

from django.contrib.auth.models import User


def project_context(request):

    context = {"me": User.objects.first(),}

    return context
