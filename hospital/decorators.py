from django.shortcuts import redirect


def hospital_view(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return redirect('admin_page')
            if request.user.is_user():
                return redirect('user')
            else:
                return view_func(request,*args,**kwargs)
    return wrapper_func