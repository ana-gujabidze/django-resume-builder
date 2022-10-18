import logging
import sys
import traceback

from django.http import JsonResponse


def error_500(request, *args, **kwargs):
    data = {
        "error": {
            "code": "internal_error",
            "message": "Internal server error.",
        }
    }

    response = JsonResponse(data)
    response.status_code = 500

    # log exception info
    type_, value, traceback_ = sys.exc_info()
    logging.error(f"Original error detail and callback: {type_}\n{value}\n{''.join(traceback.format_tb(traceback_))}")
    return response


def error_404(request, exception):
    data = {
        "error": {
            "code": "not_found",
            "message": "Page does not exist.",
        }
    }

    response = JsonResponse(data)
    response.status_code = 404

    return response
