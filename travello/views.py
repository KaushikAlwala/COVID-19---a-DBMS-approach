from django.shortcuts import render
from .models import Destination
from .models import Daily_cases
from .models import people
from .models import people3
from .models import victims
from .models import Travel_history
import psycopg2

# Create your views here.


def index(request):
    return render(request, 'index.html')

def homepage(request):
    return render(request, 'index.html')

def doneby(request):
    return render(request, 'doneby.html')

def link_1(request):
    return render(request, 'link_1.html')

def link_2(request):
    return render(request, 'link_2.html')

def link_3(request):
    return render(request, 'link_3.html')

def link_4(request):
    return render(request, 'link_4.html')

def link_5(request):
    return render(request, 'link_5.html')

def link_6(request):
    return render(request, 'link_6.html')

def link_7(request):
    return render(request, 'link_7.html')

def link_8(request):
    return render(request, 'link_8.html')

def link_9(request):
    return render(request, 'link_9.html')

def link_10(request):
    return render(request, 'link_10.html')

def link_11(request):
    return render(request, 'link_11.html')

def link_12(request):
    return render(request, 'link_12.html')

def link_13(request):
    return render(request, 'link_13.html')

def link_14(request):
    return render(request, 'link_14.html')

def link_15(request):
    return render(request, 'link_15.html')



def your_options(request):
    
    if (request.POST["option"]=="Cases_in_different_countries"):
        return render(request, 'cases.html')
    
    if (request.POST["option"]=="else"):
        return render(request, 'Graphs.html')

   

def cases_results(request):
    country_name = request.POST["s"] 
    date_entered = request.POST["date"]
    desired_country=Daily_cases()
    conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT id, date, iso_code, location, new_cases, new_deaths, total_cases, total_deaths from travello_daily_cases  where location= %s and date= %s ",(country_name , date_entered))
    name = cur.fetchall()
    desired_country.id = name[0][0]
    desired_country.date = name[0][1]
    desired_country.iso_code = name[0][2]
    desired_country.location = name[0][3]
    desired_country.new_cases = name[0][4]
    desired_country.new_deaths = name[0][5]
    desired_country.total_cases = name[0][6]
    desired_country.total_deaths = name[0][7]


    return render(request, 'cases_results.html',{'desired_country':desired_country})

def graph_options(request):
    
    if (request.POST["option"]=="Belgium"):
        gopt = "Belgium"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Brazil"):
        gopt = "Brazil"
        return render(request, 'graph_results.html',{'gopt':gopt})
    
    if (request.POST["option"]=="Canada"):
        gopt = "Canada"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Chile"):
        gopt = "Chile"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="China"):
        gopt = "China"
        return render(request, 'graph_results.html',{'gopt':gopt})
    
    if (request.POST["option"]=="France"):
        gopt = "France"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Germany"):
        gopt = "Germany"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="India"):
        gopt = "India"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Iran"):
        gopt = "Iran"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Italy"):
        gopt = "Italy"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Mexico"):
        gopt = "Mexico"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Pakistan"):
        gopt = "Pakistan"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Peru"):
        gopt = "Peru"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Qatar"):
        gopt = "Qatar"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Russia"):
        gopt = "Russia"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Saudi_Arabia"):
        gopt = "Saudi_Arabia"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Spain"):
        gopt = "Spain"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="Turkey"):
        gopt = "Turkey"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="UK"):
        gopt = "UK"
        return render(request, 'graph_results.html',{'gopt':gopt})

    if (request.POST["option"]=="USA"):
        gopt = "USA"
        return render(request, 'graph_results.html',{'gopt':gopt})


def MDU_options(request):
    
    if (request.POST["option"]=="Travel_history"):
        return render(request, 'Travel_history.html')

    if (request.POST["option"]=="PD"):
        return render(request, 'PD.html')     

    if (request.POST["option"]=="QC"):
        return render(request, 'Quarantine_centres.html')      

    if (request.POST["option"]=="VC"):
        return render(request, 'VC.html')  

    if (request.POST["option"]=="Vulnerability"):
        return render(request, 'Vulnerability.html')     

    if (request.POST["option"]=="I"):
        return render(request, 'I.html')    


def PD_results(request):
    person = request.POST["x"]
    desired_person = people3()
    conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT travello_people3.id, national_id, name, phone_number, age, address, Ischemic_heart_disease, Stroke, Bronchitis, HIV_AIDS, COPD, Diabetes_mellitus, Kidney_Disease  FROM travello_people3, travello_medical_history WHERE national_id= %s",(person,))
    name = cur.fetchall()
    desired_person.id = int(name[0][1])
    desired_person.national_id = name[0][1]
    desired_person.name = str(name[0][2])
    desired_person.phone_number = str(name[0][3])
    desired_person.age = str(name[0][4])
    desired_person.address = str(name[0][5])
    
    st = "This person is suffering from : "

    di = ["Ischemic Heart disease", "Stroke" , "Bronchitis" , "HIV-AIDS" , "COPD", "Diabetes Mellitus" , "Kidney Disease"]

    for i in [6, 7, 8, 9, 10, 11, 12]:
        if name[0][i] == "Positive":
            st = st + str(di[i-6]) + " , "


    desired_person.national_id = st



    return render(request, 'PD_results.html',{'desired_person':desired_person})

def QC_results(request):
    centre = request.POST["s"]
    conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT centre_name, address FROM travello_quarantine_centres WHERE centre_id= %s",(centre,))
    name = cur.fetchall()
    stri = "Centre Name :" + str(name[0][0]) +" , " + "Address : " + str(name[0][1]) + ". The ID's of the victims in this centre are : "
    conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT victim_id FROM travello_victims WHERE centre_id= %s",(centre,))
    y = cur.fetchall()   
    for i in range(0,len(y)-1):
        stri = stri + " , " + str(y[i][0]) 

    return render(request, 'QC_results.html',{'stri':stri})

def VC_results(request):
    person = request.POST["s"]
    y = victims.objects.all()
    flag = 0
    for z in y:
        if z.victim_id == person:
            d=z
            flag = 1

    if(flag==1):
        stri = "This person is infected with COVID19 on " + str(d.admit_date) + " . He is currently at the Quarantine centre with ID : " + str(d.centre_id)  
    else:
        stri = "This person is not infected with COVID19"
    
    return render(request, 'QC_results.html',{'stri':stri})


def TH_results(request):
    person = request.POST["s"]
    date = request.POST["option"]
    conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("SELECT april_16 FROM travello_travel_history WHERE person_id= %s",(person,))
    name = cur.fetchall()
    if date == "april_16":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_16 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_16= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_17":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_17 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_17= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_18":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_18 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_18= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_19":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_19 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_19= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)-1):
            stri = stri + str(y[i][0]) + " , "


    if date == "april_20":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_20 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_20= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)-1):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_21":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_21 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_21= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)-1):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_22":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_22 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_22= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)-1):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_23":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_23 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_23= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + str(y[i][0]) + " , "

    if date == "april_24":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_24 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_24= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + str(y[i][0]) + " , "


    if date == "april_25":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_25 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_25= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + str(y[i][0]) + " , "


    if date == "april_26":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_26 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_26= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri  + str(y[i][0]) + " , "

    if date == "april_27":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_27 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_27= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + " , " + str(y[i][0])

    if date == "april_28":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_28 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_28= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri  + str(y[i][0])+ " , "

    if date == "april_29":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_29 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_29= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri  + str(y[i][0]) + " , "

    if date == "april_30":
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_20 FROM travello_travel_history WHERE person_id= %s",(person,))
        name = cur.fetchall()
        stri = "This perosn was at " + str(name[0][0]) + ". The ID's of other people who were in the same place on the same date are "
        place = str(name[0][0])
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT person_id FROM travello_travel_history WHERE april_30= %s",(place,))
        y=cur.fetchall()
        for i in range(2,len(y)):
            stri = stri + + str(y[i][0]) + " , "




    return render(request, 'TH_results.html',{'stri':stri})


def V_results(request):
    person = request.POST["s"] 
    v = victims.objects.all()
    th = Travel_history()
    flag=0
    for g in v:
        if person in g.victim_id:
            flag = 1
            return render(request, 'AaV.html',)

    if flag==0:
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT april_16, april_17, april_18, april_19, april_20, april_21, april_22, april_23, april_24, april_25, april_26, april_27, april_28, april_29, april_30    from travello_travel_history  where person_id = %s ",(person,))
        name = cur.fetchall()
        A16 = name[0][0]
        A17 = name[0][1]
        A18 = name[0][2]
        A19 = name[0][3]
        A20 = name[0][4]
        A21 = name[0][5]
        A22 = name[0][6]
        A23 = name[0][7]
        A24 = name[0][8]
        A25 = name[0][9]
        A26 = name[0][10]
        A27 = name[0][11]
        A28 = name[0][12]
        A29 = name[0][13]
        A30 = name[0][14]
        

        dates = ["april_16","april_17","april_18","april_19","april_20","april_21","april_22","april_23","april_24","april_25","april_26","april_27","april_28","april_29","april_30"]
        
        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_16 = %s",(A16,))
        y16 = cur.fetchall()
        str16 = "On this day this person was at " + str(A16) + " The now victims who had visited this place are : "
        for i in range(0,len(y16)-1):
            str16 = str16 + str(y16[i][0]) + " , "
        th.april_16 = str16

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_17 = %s",(A17,))
        y17 = cur.fetchall()
        str17 = "On this day this person was at " + str(A17) + " The now victims who had visited this place are : "
        for i in range(0,len(y17)-1):
            str17 = str17 + str(y17[i][0]) + " , "
        th.april_17 = str17

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_18 = %s",(A18,))
        y18 = cur.fetchall()
        str18 = "On this day this person was at " + str(A18) + " The now victims who had visited this place are : "
        for i in range(0,len(y18)-1):
            str18 = str18 + str(y18[i][0]) + " , "
        th.april_18 = str18

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_19 = %s",(A19,))
        y19 = cur.fetchall()
        str19 = "On this day this person was at " + str(A19) + " The now victims who had visited this place are : "
        for i in range(0,len(y19)-1):
            str19 = str19 + str(y19[i][0]) + " , "
        th.april_19 = str19

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_20 = %s",(A20,))
        y20 = cur.fetchall()
        str20 = "On this day this person was at " + str(20) + " The now victims who had visited this place are : "
        for i in range(0,len(y20)-1):
            str20 = str20 + str(y20[i][0]) + " , "
        th.april_20 = str20

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_21 = %s",(A21,))
        y21 = cur.fetchall()
        str21 = "On this day this person was at " + str(A21) + " The now victims who had visited this place are : "
        for i in range(0,len(y21)-1):
            str21 = str21 + str(y21[i][0]) + " , "
        th.april_21 = str21

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_22 = %s",(A22,))
        y22 = cur.fetchall()
        str22 = "On this day this person was at " + str(A22) + " The now victims who had visited this place are : "
        for i in range(0,len(y22)-1):
            str22 = str22 + str(y22[i][0]) + " , "
        th.april_22 = str22

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_23 = %s",(A23,))
        y23 = cur.fetchall()
        str23 = "On this day this person was at " + str(A23) + " The now victims who had visited this place are : "
        for i in range(0,len(y23)-1):
            str23 = str23 + str(y23[i][0]) + " , "
        th.april_23 = str23

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_24 = %s",(A24,))
        y24 = cur.fetchall()
        str24 = "On this day this person was at " + str(A24) + " The now victims who had visited this place are : "
        for i in range(0,len(y24)-1):
            str24 = str24 + str(y24[i][0]) + " , "
        th.april_24 = str24     

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_25 = %s",(A25,))
        y25 = cur.fetchall()
        str25 = "On this day this person was at " + str(A25) + " The now victims who had visited this place are : "
        for i in range(0,len(y25)-1):
            str25 = str25 + str(y25[i][0]) + " , "
        th.april_25 = str25    

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_26 = %s",(A26,))
        y26 = cur.fetchall()
        str26 = "On this day this person was at " + str(A26) + " The now victims who had visited this place are : "
        for i in range(0,len(y26)-1):
            str26 = str26 + str(y26[i][0]) + " , "
        th.april_26 = str26   

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_27 = %s",(A27,))
        y27 = cur.fetchall()
        str27 = "On this day this person was at " + str(A27) + " The now victims who had visited this place are : "
        for i in range(0,len(y27)-1):
            str27 = str27 + str(y27[i][0]) + " , "
        th.april_27 = str27 

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_28 = %s",(A28,))
        y28 = cur.fetchall()
        str28 = "On this day this person was at " + str(A28) + " The now victims who had visited this place are : "
        for i in range(0,len(y28)-1):
            str28 = str28 + str(y28[i][0]) + " , "
        th.april_28 = str28

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_29 = %s",(A29,))
        y29 = cur.fetchall()
        str29 = "On this day this person was at " + str(A29) + " The now victims who had visited this place are : "
        for i in range(0,len(y29)-1):
            str29 = str29 + str(y29[i][0]) + " , "
        th.april_29 = str29

        conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
        cur = conn.cursor()
        cur.execute("SELECT travello_travel_history2.person_id FROM travello_travel_history2, travello_victims WHERE travello_travel_history2.person_id = travello_victims.victim_id and travello_travel_history2.april_30 = %s",(A30,))
        y30 = cur.fetchall()
        str30 = "On this day this person was at " + str(A30) + " The now victims who had visited this place are : "
        for i in range(0,len(y30)-1):
            str30 = str30 + str(y30[i][0]) + " , "
        th.april_30 = str30

        th.person_id = str(len(y16) + len(y17) + len(y18) + len(y19) + len(y20) + len(y21) + len(y22) +len(y23) +  len(y24) + len(y25) + len(y26) + len(y27) + len(y28) + len(y29) + len(y30))

        return render(request, 'V_results.html',{'th': th})    


def I_results(request):
    victim = request.POST["v"] 
    center = request.POST["c"]
    date = request.POST["a"]
    v = victims.objects.all()
    flag =0
    for q in v:
        if q.victim_id == victim:
            flag = 1
            return render(request, 'A.html') 
    count = 0 
    for q in v:
        count = count + 1 


    x = int(count+1) 
    conn = psycopg2.connect(database = "COVID19", user = "postgres", password = "cs251", host = "127.0.0.1", port = "5432")
    cur = conn.cursor()
    cur.execute("INSERT INTO public.travello_victims(id, victim_id, centre_id, admit_date) VALUES (246, %s, %s, %s) ",(victim,center,date,))
    return(request, 'I_results.html')
