

def get_client_id(request):
    """Функция для взятия ip пользователя"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


#ip = get_client_id(self.request)
    #if Ip.objects.filter(ip=ip).exists():
    #    post.views.add(Ip.objects.get(ip=ip))
    #else:
    #    Ip.objects.create(ip=ip)
    #    post.views.add(Ip.objects.get(ip=ip))
    #return post