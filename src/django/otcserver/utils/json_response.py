
from rest_framework.response import Response
from rest_framework.serializers import Serializer


from utils.http_code import *

class JsonResponse(Response):
    """
    An HttpResponse that allows its data to be rendered into
    arbitrary media types.
    """

    def __init__(self, data=None, code=None, msg=None,
                 status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None):
        """
        Alters the init arguments slightly.
        For example, drop 'template_name', and instead use 'data'.
        Setting 'renderer' and 'media_type' will typically be deferred,
        For example being set automatically by the `APIView`.
        """
        if not code:
            code = get_default_http_code()

        if code:
            args = get_http_code(code)
            code = args[0]

            if not msg:
                msg = args[1]

            # 自定义status
            if not status:

                if int(HTTP_CODE_CUSTOM_START) < code < int(HTTPCODE_CUSTOM_END):
                    status = int(code / int(HTTP_CODE_CUSTOM_START) * 100)
                elif code < int(HTTP_CODE_STD_MAX_LIMIT):
                    status = args[0]

        super(Response, self).__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.data = {"code": code, "message": msg, "data": data}
        self.template_name = template_name
        self.exception = exception
        self.content_type = content_type
        if headers:
            for name, value in (headers):
                print(headers,name,value)
                self[name] = value