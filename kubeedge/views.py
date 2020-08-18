from django.shortcuts import render

# Create your views here.
def recognition(request):
    now = '已傳送圖片'
    #return render(request, "hello3.html", locals())
    return render(request, 'kubeedge/home.html', locals())
def user(request):
    return render(request, 'kubeedge/control.html', locals())