from django.shortcuts import render # django.shorcuts 패키지에 있는 render라는 함수 사용

def showmain(request):
      return render(request, 'main/mainpage.html')

# Create your views here.
#  def 함수이름(인자):
#    함수를 호출했을때 실행될 코드