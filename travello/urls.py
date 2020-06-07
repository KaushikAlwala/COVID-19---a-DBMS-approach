from django.urls import path

from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('homepage',views.homepage, name='homepage'),
    path('doneby',views.doneby, name='doneby'),
    path('link_1',views.link_1, name='link_1'),
    path('link_2',views.link_2, name='link_2'),
    path('link_3',views.link_3, name='link_3'),
    path('link_4',views.link_4, name='link_4'),
    path('link_5',views.link_5, name='link_5'),
    path('link_6',views.link_6, name='link_6'),
    path('link_7',views.link_7, name='link_7'),
    path('link_8',views.link_8, name='link_8'),
    path('link_9',views.link_9, name='link_9'),
    path('link_10',views.link_10, name='link_10'),
    path('link_11',views.link_11, name='link_11'),
    path('link_12',views.link_12, name='link_12'),
    path('link_13',views.link_13, name='link_13'),
    path('link_14',views.link_14, name='link_14'),
    path('link_15',views.link_15, name='link_15'),
    path('your_options', views.your_options, name="your_options"),
    path('MDU_options', views.MDU_options, name="MDU_options"),
    path('graph_options', views.graph_options, name="graph_options"),
    path('PD_results', views.PD_results, name="PD_results"),
    path('TH_results', views.TH_results, name="TH_results"),
    path('QC_results', views.QC_results, name="QC_results"),
    path('VC_results', views.VC_results, name="VC_results"),
    path('V_results', views.V_results, name="V_results"),
    path('I_results', views.I_results, name="I_results"),
    path('cases_results', views.cases_results, name="cases_results")
]