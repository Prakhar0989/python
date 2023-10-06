# from django.http import HttpResponseForbidden

# class IPAccessMiddleware:
#     allowed_ips = ['192.168.1.80', '192.168.1.9' , '192.168.1.92']  # Add your allowed local IP addresses

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         client_ip = request.META.get('REMOTE_ADDR')
        
#         # Check if the client's IP is in the allowed list
#         if client_ip not in self.allowed_ips:
#             return HttpResponseForbidden("Access denied: Your IP is not allowed.")

#         return self.get_response(request)
