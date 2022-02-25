from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping

from web.models import Cust


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');

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
            if cust.pwd == pwd: # 비밀번호가 같으면
                request.session['sessionid'] = id; #정상
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