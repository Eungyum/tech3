# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# 로그인 뷰
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # 로그인 후 대시보드로 리다이렉트
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# 로그아웃 뷰
def logout_view(request):
    logout(request)
    return redirect('login')  # 로그아웃 후 로그인 페이지로 리다이렉트

@login_required
def dashboard(request):
    """
    로그인한 사용자의 역할에 따라 다른 대시보드 페이지를 렌더링
    """
    if request.user.role == 'manager':
        return render(request, 'manager/dashboard.html', {"user": request.user})  # 관리자 대시보드
    elif request.user.role == 'client':
        return render(request, 'client/dashboard.html', {"user": request.user})  # 클라이언트 대시보드
    else:
        return redirect('login')  # 역할이 없으면 로그인 페이지로 리다이렉트