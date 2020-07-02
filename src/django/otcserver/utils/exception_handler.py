from rest_framework.views import exception_handler as super_exception_handler

from utils import JsonResponse

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = super_exception_handler(exc, context)

    # default code
    status_code = '500'
    if response is  None:
        return JsonResponse(context,status_code)

    # Now add the HTTP status code to the response.
    if response.status_code:
        status_code = str(response.status_code)

    return JsonResponse(context,status_code,response.data['detail'],
                        exception=True,content_type=response.content_type)
