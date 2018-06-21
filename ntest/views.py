from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from ntest.models import case_eg,Environment
from cwgj.cwgj_request import cwgj
from cwgj.encrypt import AESECB
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def base(request):
    return render(request,'base.html')

def extendsbase(request):
    return render(request,'base/extendsbase.html')




def index(request):
    return render(request,'base/index.html')


def case(request):
    if request.method == 'POST':
        case_name = request.POST.get('case_name','')
        token = request.POST.get('token','')
        header = request.POST.get('header','')
        url = request.POST.get('url','')
        content = request.POST.get('content','')
        case1 = case_eg(case_name=case_name,url=url,header_parameter=header,content_parameter=content,tk_parameter=token)
        case1.save()
        render(request,'case/test.html')
    case_list = case_eg.objects.all()
    return render(request,'case/test.html',{'case_list':case_list})



# def finddata(request):
#     if request.method == 'get':
#         get_type = request.GET.get('type','')
#         if get_type == 'query_carpark':
#             case_id = request.GET.get('case_id','')
#             a = case_eg.objects.get(case_id=case_id)

@csrf_exempt
def case_run(request):
    if request.method == 'POST':
        case_id = request.POST.get('case_id','')
        a = case_eg.objects.get(case_id=case_id)
        url = a.url
        header = eval(a.header_parameter)
        content = eval(a.content_parameter)
        tk = a.tk_parameter
        rq = cwgj.ownercar(url,header=header,content=content)
        # rq_decode = rq.decode()
        # print(type(rq_decode))
        # return HttpResponse(rq_decode)
        json_content = AESECB.decrpyt(rq,tk=tk)
        return HttpResponse(json_content)
    else:
        return HttpResponse('get方法不提供返回值')


#@csrf_exempt
def html_encrypt(request):
    return render(request,'encrypt/encrypt.html')




@csrf_exempt
def content_encrypt(request):
    if request.method == 'POST':
        CH_key = request.POST.get('CH_key', '')
        content = request.POST.get('content', '')
        tk = request.POST.get('tk', '')
        # print(CH_key,content,tk)
        if CH_key == 'encrypt_key':
            encrypt_content = AESECB.encrpyt(content, tk)
            return HttpResponse(encrypt_content)
        elif CH_key == 'decrypt_key':
            decrypt_content = AESECB.decrpyt(content, tk)
            return HttpResponse(decrypt_content)
        else:
            return HttpResponse('过程出错')
    else:
        return HttpResponse('get方法不提供返回值')



def environment(request):
    if request.method=='POST':
        env_name = request.POST.get('environment_name','')
        env_url = request.POST.get('environment_url','')
        case_env = Environment(url=env_url,env_name=env_name)
        case_env.save()
        return render(request,'case/environment.html')
    # env_list = Environment.objects.all()
    return render(request,'case/environment_add.html')
