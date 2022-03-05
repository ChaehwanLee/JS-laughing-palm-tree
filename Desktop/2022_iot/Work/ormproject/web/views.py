import logging
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

    @request_mapping("/ajax", method="get")
    def ajax(self, request):
        context = {
            'center': 'ajax.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/ajaximpl", method="get")
    def ajaximpl(self, request):
        # [{},{},{}]
        data = [];
        for i in range(1, 10):
            dic = {};
            dic['id'] = 'id'+str(i);
            dic['name'] = 'james' + str(i);
            dic['age'] = i;
            data.append(dic);
        return HttpResponse(json.dumps(data),content_type='application/json');

    @request_mapping("/iot", method="get")
    def iot(self, request):
        id = request.GET['id'];
        temp = request.GET['temp'];
        el = request.GET['el'];
        # -------------------------------------------
        el_logger = logging.getLogger('el_file');
        el_logger.debug(id + ',' + temp + ',' + el);
        # -------------------------------------------
        return render(request, 'ok.html');



    @request_mapping("/login", method="get")
    def login(self, request):
        context = {
            'center': 'login.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/loginimpl", method="post")
    def loginimpl(self, request):
        # id, pwd 를 프로그램을 확인 한다.
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        context = {};
        try:
            cust = Cust.objects.get(id=id); # 입력한 아이디가 db에 있느냐 없느냐
            if cust.pwd == pwd:
                request.session['sessionid'] = cust.id;
                request.session['sessionname'] = cust.name;
                context['center'] = 'loginok.html';
            else:
                raise Exception;
        except:
            context['center'] = 'loginfail.html';

        return render(request, 'home.html', context);

    @request_mapping("/logout", method="get")
    def logout(self, request):
        if request.session['sessionid'] != None:
            del request.session['sessionid'];
        return render(request, 'home.html');

    @request_mapping("/register", method="get")
    def register(self, request):
        context = {
            'center': 'register.html'
        };
        return render(request, 'home.html', context);

    @request_mapping("/registerimpl", method="post")
    def registerimpl(self, request):
        id = request.POST['id'];
        pwd = request.POST['pwd'];
        name = request.POST['name'];
        print(id,pwd,name);
        context = {};
        try:
            Cust.objects.get(id = id);
            context['center'] = 'registerfail.html';

        except:
            Cust(id=id, pwd=pwd, name=name).save();
            context['center'] = 'registerok.html';
            context['rname'] = name;

        return render(request, 'home.html', context);

    @request_mapping("/geo", method="get")
    def geo(self, request):
        context = {
            'center': 'geo.html'
        };
        return render(request, 'home.html', context);

# 새롭게 추가한 부분
    @request_mapping("/geoimpl", method="get")
    def geoimpl(self, request):
        data = [];
        dic1 = {};
        dic1['content'] = '더베이 101'
        dic1['lat'] = 35.156593
        dic1['lng'] = 129.152030
        dic1['target'] = 'http://www.thebay101.com/the-bay-101/enjoy/'
        data.append(dic1);

        dic2 = {};
        dic2['content'] = 'The Westin Josun Busan'
        dic2['lat'] = 35.155927
        dic2['lng'] = 129.153801
        dic2['target'] = 'https://josunhotel.com/m/hotel/westinBusan.do'
        data.append(dic2);

        dic3 = {};
        dic3['content'] = 'Dongbaek Park'
        dic3['lat'] = 35.153620
        dic3['lng'] = 129.152213
        dic3['target'] = 'https://kr.trip.com/travel-guide/attraction/busan/dongbaekseom-island-95269/'
        data.append(dic3);

        dic4 = {};
        dic4['content'] = 'Nurimaru APEC House'
        dic4['lat'] = 35.152330
        dic4['lng'] = 129.151344
        dic4['target'] = 'https://www.busan.go.kr/nurimaru'
        data.append(dic4);

        return HttpResponse(json.dumps(data), content_type='application/json');
# 여기까지

    @request_mapping("/geo2", method="get")
    def geo2(self, request):
        context = {
            'center': 'geo2.html'
        };
        return render(request, 'home.html', context);