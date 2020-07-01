from rest_framework.views import exception_handler as super_exception_handler
from utils.json_response import JsonResponse
def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = super_exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:

        response['custom_exception_handler'] = 'custom_exception_handler'
    status_code = str(response.status_code)

    return JsonResponse(None,code=status_code,msg=response.data['detail'],exception=True,content_type=response.content_type)
