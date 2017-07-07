from django.shortcuts import redirect

def userlogin(func):
    def funcs(request, *args, **kwargs):
        if request.session.has_key('uid'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')
    return funcs
