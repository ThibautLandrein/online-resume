# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 13:54:57 2021

@author: Thibaut
"""

from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('portfolio/', views.PortfolioView.as_view(), name="portfolio"),
    path('portfolio/<slug:slug>',
          views.PortfolioDetailView.as_view(), name="portfolio"),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog")

]
