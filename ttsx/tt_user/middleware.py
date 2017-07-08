class Urlmiddleware:
    def process_request(self, request):
        print(request.path)
        if request.path not in['/user/register/','/user/register_handle/','/user/login/','/user/login_handle/','/user/register_yz/','/user/logout/']:
            request.session['url_path'] = request.get_full_path()
