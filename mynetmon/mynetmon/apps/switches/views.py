from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import *
from .forms import SwitchForm, CategoryForm, TitulForm
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
#from pythonping import ping
from .sentoid import *
from .bckup import *
import socket
import os
from django.core.files.base import ContentFile

'''This site functions'''

def index(request):
    #создаем функцию switches с обязательным параметром который необходимо получить request
    switchs = Switch.objects.order_by('id')     #создаем переменную switchs и обращаемся к модели Switch ко всем ее обьектам
    #которые сортируются по id

    online_count = Switch.objects.filter(status = 'connection').count()
    offline_count = Switch.objects.filter(status = 'no connection').count()
    all_count = Switch.objects.all().count()
    statusbardel = online_count / all_count
    statusbarperc = statusbardel * 100
    statusbar = int(statusbarperc)

    if request.method == 'GET':         #если данные передаются методом гет
        for swi in switchs:   #цикл начинается с ключевого слова for, за которым следует
            # произвольное имя переменной, которое будет хранить значения следующего объекта последовательности.
            #try:
                #p = ping(swi.ipaddr, verbose=False,count=1, timeout=0.120)
                #if p._responses[0].success:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.150)
                result = sock.connect_ex((swi.ipaddr, 80))
                if result == 0:
                    zapros = sysname(swi.ipaddr)
                    swi.status = 'connection'
                    swi.label_two = zapros
                    swi.save()   #сохраняем как новую запись в базу данных
                    #print(p._responses[0].success)

                else:
                    #swi.label_two = 'no connection'
                    swi.status = 'no connection'
                    swi.save()
            #except:
                #swi.status = 'no connection'
                #swi.save()


    return render(request, 'switches/index.html', {'title': 'Главная', 'switchs': switchs, 'online_count': online_count, 'offline_count': offline_count, 'all_count': all_count, 'statusbar': statusbar})


'''Поиск по имени и айпи'''
def search(request):
    search_query = request.GET.get('search', '')
    if search_query:
        switch_query = Switch.objects.filter(Q(label__icontains=search_query) | Q(ipaddr__icontains=search_query))

    else:
        switch_query = Switch.objects.all
    return render(request, 'switches/search.html', {'title': 'Список устройств', 'switchs': switch_query })

def onlybad(request):
    onlybad = request.GET.get('search', 'no connection')
    if onlybad:
        switch_query = Switch.objects.filter(Q(status__icontains=onlybad))

    else:
        switch_query = Switch.objects.all
    return render(request, 'switches/switchlist.html', {'title': 'Список устройств', 'switchs': switch_query })



#в функции switches прежде чем отобразить шаблон мы будем получать данные из модели Switch и обрабатывать скрипт sysname
def switches(request):
    #создаем функцию switches с обязательным параметром который необходимо получить request
    switchs = Switch.objects.order_by('id')     #создаем переменную switchs и обращаемся к модели Switch ко всем ее обьектам
    #которые сортируются по id
    if request.method == 'GET':         #если данные передаются методом гет
        for swi in switchs:   #цикл начинается с ключевого слова for, за которым следует
            # произвольное имя переменной, которое будет хранить значения следующего объекта последовательности.
            #p = ping(swi.ipaddr, verbose=False,count=1, timeout=0.120)
            #if p._responses[0].success:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.120)
            result = sock.connect_ex((swi.ipaddr, 80))
            if result == 0:
                zapros = sysname(swi.ipaddr)
                swi.status = 'connection'
                swi.label_two = zapros
                swi.save()   #сохраняем как новую запись в базу данных
                #print(p._responses[0].success)

            else:
                #swi.label_two = 'no connection'
                swi.status = 'no connection'
                swi.save()
    return render(request, 'switches/switchlist.html', {'title': 'Список устройств', 'switchs': switchs })






def pingget(request):
    switchs = Switch.objects.order_by('id')
    if request.method == 'GET':
        output_data = []# если данные передаются методом гет
        for switch in switchs:  # цикл начинается с ключевого слова for, за которым следует
            # произвольное имя переменной, которое будет хранить значения следующего объекта последовательности.
            #p = ping(switch.ipaddr, verbose=False, count=1, timeout=0.120)
            #if p._responses[0].success:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.180)
            result = sock.connect_ex((switch.ipaddr, 80))
            if result == 0:
                output_data.append({'id': switch.id, 'pingget': 'True'})
            else:
                output_data.append({'id': switch.id, 'pingget': 'False'})

    return JsonResponse(output_data, safe=False)







'''добавление свича'''

def createsw(request):
    error = ''
    ferror = ''
    if request.method == 'POST':
        form = SwitchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('switchlist')
        else:
            error = 'Форма заполнена не верно!'
            ferror = form.errors

    form = SwitchForm()
    sendform = {
        'form': form,
        'error': error,
        'ferror': ferror,

    }



    return render(request, 'switches/createsw.html', sendform)

def createcat(request):
    error = ''
    ferror = ''
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            error = 'Форма заполнена не верно!'
            ferror = form.errors

    form = CategoryForm()
    sendform = {
        'form': form,
        'error': error,
        'ferror': ferror,

    }



    return render(request, 'switches/createcat.html', sendform)

'''DetailView page'''



def swdetail(request,pk):
    try:
        swdetail = Switch.objects.get(pk=pk)
        switchs = Switch.objects.filter(pk=pk)
        if request.method == 'GET':
            for swi in switchs:
                #p = ping(swi.ipaddr, verbose=False, count=1, timeout=1.420)
                #if p._responses[0].success:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.150)
                result = sock.connect_ex((swi.ipaddr, 80))
                if result == 0:
                    swi.status = 'connection'
                    serial = sysdetail(swi.ipaddr, '1.3.6.1.2.1.47.1.1.1.1.11.1')
                    swi.serial = serial
                    mask = sysdetail(swi.ipaddr, '1.3.6.1.4.1.25506.8.35.18.1.2.0')
                    swi.mask = mask
                    fullmodel = sysdetail(swi.ipaddr, '1.3.6.1.2.1.47.1.1.1.1.13.1')
                    swi.fullmodel = fullmodel
                    binfile = sysdetail(swi.ipaddr, '1.3.6.1.4.1.25506.2.3.1.4.2.1.2.524290')
                    swi.binfile = binfile
                    contact = sysdetail(swi.ipaddr, '1.3.6.1.2.1.1.4.0')
                    swi.contact = contact
                    reliz = sysdetail(swi.ipaddr, '1.3.6.1.2.1.47.1.1.1.1.10.1')
                    swi.reliz = reliz
                    location = sysdetail(swi.ipaddr, '1.3.6.1.2.1.1.6.0')
                    swi.location = location
                    #bckp = telnet(swi.ipaddr)
                    #rep = bckp.replace("  ---- More ----[16D                [16D", "")
                    #swi.cfg = rep
                    interfaces = telnetinterfaces(swi.ipaddr)
                    intrep = interfaces.replace("  ---- More ----[16D                [16D", "")
                    swi.interfaces = intrep
                    logs = logging(swi.ipaddr)
                    logrep = logs.replace("  ---- More ----[16D                [16D", "")
                    swi.logs = logrep
                    swi.save()  # сохраняем как новую запись в базу данных

                else:
                    swi.status = 'no connection'
                    swi.save()

    except Switch.DoesNotExist:
        raise Http404("Switch does not exist")
    return render(request, 'switches/swdetail.html', {'swdetail': swdetail})

def deleteswitch(request, id):
    try:
        switch = Switch.objects.get(id=id)
        switch.delete()
        return HttpResponseRedirect("/switchlist")
    except Switch.DoesNotExist:
        return HttpResponseNotFound("<h2>Switch not found</h2>")

def deletecat(request, id):
    try:
        category = Category.objects.get(id=id)
        category.delete()
        return HttpResponseRedirect("/category")
    except Switch.DoesNotExist:
        return HttpResponseNotFound("<h2>Category not found</h2>")

def deletetit(request, id):
    try:
        titul = Titul.objects.get(id=id)
        titul.delete()
        return HttpResponseRedirect("/tituls")
    except Switch.DoesNotExist:
        return HttpResponseNotFound("<h2>Titul not found</h2>")



def editsw(request, id):
    switch = Switch.objects.get(id=id)
    error = ''
    ferror = ''
    if request.method == "POST":
        form = SwitchForm(request.POST, instance=switch)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/switchlist')
    else:
        form = SwitchForm(instance=switch)
        error = 'Форма заполнена не верно!'
        ferror = form.errors


    return render(request, "switches/editsw.html", {'form': form})

def editcat(request, id):
    category = Category.objects.get(id=id)
    error = ''
    ferror = ''
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/category')
    else:
        form = CategoryForm(instance=category)
        error = 'Форма заполнена не верно!'
        ferror = form.errors


    return render(request, "switches/editcat.html", {'form': form})


def edittit(request, id):
    titul = Titul.objects.get(id=id)
    error = ''
    ferror = ''
    if request.method == "POST":
        form = TitulForm(request.POST, instance=titul)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/tituls')
    else:
        form = TitulForm(instance=titul)
        error = 'Форма заполнена не верно!'
        ferror = form.errors


    return render(request, "switches/edittit.html", {'form': form})


def getconfig(request):
    ip = request.GET.get('ip')
    pk = request.GET.get('pk')
    swi = Switch.objects.get(pk=pk)

    # print(swi)

    bckp = telnet(ip)
    rep = bckp.replace("  ---- More ----[16D                [16D", "")

    swi.cfg = rep
    swi.save()

    output_data = ({'rep': rep})

    return JsonResponse(output_data, safe=False)





def autodata(request):

    return render(request, 'switches/swdetail.html', {'swdetail': swdetail})

def pingdetail(request):
    switchs = Switch.objects.order_by('id')
    if request.method == 'GET':
        output_data = []# если данные передаются методом гет
        for switch in switchs:  # цикл начинается с ключевого слова for, за которым следует
            # произвольное имя переменной, которое будет хранить значения следующего объекта последовательности.
            #p = ping(switch.ipaddr, verbose=False, count=1, timeout=0.120)
            #if p._responses[0].success:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.150)
            result = sock.connect_ex((switch.ipaddr, 80))
            if result == 0:

                output_data.append({'id': switch.id, 'pingdetail': 'True'})
            else:
                output_data.append({'id': switch.id, 'pingdetail': 'False'})

    return JsonResponse(output_data, safe=False)

def backupjs(request):
    switchs = Switch.objects.order_by('id')
    if request.method == 'GET':
        output_data = []  # если данные передаются методом гет
        for swi in switchs:  # цикл начинается с ключевого слова for, за которым следует
            # произвольное имя переменной, которое будет хранить значения следующего объекта последовательности.
            #p = ping(swi.ipaddr, verbose=False, count=1, timeout=0.120)
            #if p._responses[0].success:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.120)
            result = sock.connect_ex((swi.ipaddr, 80))
            if result == 0:
                bckp = telnet(swi.ipaddr)
                rep = bckp.replace("  ---- More ----[16D                [16D", "")
                swi.cfg = rep

                #with open(os.path.join('D:\django\mynetmon\lackup')) as f:
                 #f = open(swi.label+'.cfg', 'w')
                 #f.write('\n')
                 #f.write(swi.cfg)
                 #f.close()

                interfaces = telnetinterfaces(swi.ipaddr)
                intrep = interfaces.replace("  ---- More ----[16D                [16D", "")
                swi.interfaces = intrep
                logs = logging(swi.ipaddr)
                logrep = logs.replace("  ---- More ----[16D                [16D", "")
                swi.logs = logrep
                swi.save()  # сохраняем как новую запись в базу данных

            else:
                swi.save()

    return JsonResponse(output_data, safe=False)


def tituls(request):
    tituls = Titul.objects.order_by('zavod')
    return render(request, 'switches/tituls.html', {'title': 'Титула', 'tituls': tituls})

def titdetail(request,pk):
    try:
        titdetail = Switch.objects.get(pk=pk)

    except Titul.DoesNotExist:
        raise Http404("Titul does not exist")

    titul = Titul.objects.get(pk = pk)
    switches = Switch.objects.filter(tit__id = pk)

    #swdetail=get_object_or_404(Switch, pk=pk)
    return render(request, 'switches/tituls_detail.html', {'titul': titul, 'switches': switches})

def createtit(request):
    error = ''
    ferror = ''
    if request.method == 'POST':
        form = TitulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tituls')
        else:
            error = 'Форма заполнена не верно!'
            ferror = form.errors

    form = TitulForm()
    sendform = {
        'form': form,
        'error': error,
        'ferror': ferror,

    }



    return render(request, 'switches/createtit.html', sendform)



def category(request):


    category = Category.objects.order_by('id')
    return render(request, 'switches/category.html', {'title': 'Категории', 'category': category})

def catdetail(request,pk):
    try:
        catdetail = Switch.objects.get(pk=pk)

    except Category.DoesNotExist:
        raise Http404("Category does not exist")

    category = Category.objects.get(pk = pk)
    switches = Switch.objects.filter(category__id = pk)

    #swdetail=get_object_or_404(Switch, pk=pk)
    return render(request, 'switches/category_detail.html', {'category': category, 'switches': switches})


def backup(request):
    backup = Backup.objects.order_by('id')
    switchs = Switch.objects.order_by('id')

    if request.method == 'GET':
        for swi in switchs:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.120)
            result = sock.connect_ex((swi.ipaddr, 80))
            if result == 0:
                swi.status = 'connection'
                swi.save()

            else:
                swi.status = 'no connection'
                swi.save()



    return render(request, 'switches/backup.html', {'title': 'Бекап', 'backup': backup, 'switchs': switchs})


'''BACKUP'''


def create_backup(self, pk):
    switch = Switch.objects.get(id=pk)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.120)
    result = sock.connect_ex((switch.ipaddr, 80))

    if result == 0:
        bckp = telnet(switch.ipaddr)
        rep = bckp.replace("  ---- More ----[16D                [16D", "")

        name = switch.label+'.cfg'

        backup = Backup.objects.create(backname=name)
        backup.bfile.save(name, ContentFile(rep))

        switch.backkey = backup
        switch.save()

    return HttpResponseRedirect('/backup')


def delete_backup(self, pk):
    backup = Backup.objects.get(id=pk)
    backup.bfile.delete(save=False)
    backup.delete()
    return HttpResponseRedirect('/backup')


def update_backup(self, pk):
    switch = Switch.objects.get(id=pk)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.120)
    result = sock.connect_ex((switch.ipaddr, 80))

    if result == 0:
        bckp = telnet(switch.ipaddr)
        rep = bckp.replace("  ---- More ----[16D                [16D", "")

        name = switch.label+'.cfg'

        backup = Backup.objects.get(id=switch.backkey.id)
        backup.bfile.delete(save=False)
        backup.bfile.save(name, ContentFile(rep))


    return HttpResponseRedirect('/backup')









'''This monitoring scripts functions'''

def hostname(request):
    return
