class HTTPTooManyRequestException(Exception): pass


class HTTPServerDown(Exception): pass


class ErrorInvalidAuthetication(Exception): pass


class ErrorInvalidParameter(Exception): pass


class ErrorInvalidRepresentation(Exception): pass


class ErrorAPINotFound(Exception): pass


class ErrorUnauthorized(Exception): pass


class ErrorInternalServerError(Exception): pass


class ErrorTooManyRequests(Exception): pass


class ErrorExpiredAuthentication(Exception): pass


class ErrorInvalidContentType(Exception): pass


class ErrorMissingParameter(Exception): pass


error_code_map = {'invalid_parameter': (ErrorInvalidParameter, '파라미터는 제공되었지만, 해당 값이 올바르지 않습니다.'),
                  'invalid_authentication': (ErrorInvalidAuthetication, '제공된 인증 토큰이 유효하지 않습니다.'),
                  'invalid_representation': (ErrorInvalidRepresentation, '유효하지 않은 포맷의 Body 데이터입니다.'),
                  'api_not_found': (ErrorAPINotFound, '요청이 API가 요구하는 URL 혹은 HTTP 메서드와 다릅니다.'),
                  'unauthorized': (ErrorUnauthorized, '인증 토큰이 제공되지 않았습니다.'),
                  'internal_server_error': (ErrorInternalServerError, '정의되지 않은 서버 오류가 발생하였습니다.'),
                  'too_many_requests': (ErrorTooManyRequests, 'API 사용 한도를 초과하였습니다.'),
                  'expired_authentication': (ErrorTooManyRequests, '제공된 인증 토큰이 만료되었습니다.'),
                  'invalid_content_type': (ErrorInvalidContentType, '요청이 API가 요구하는 Content Type과 다릅니다.'),
                  'missing_parameter': (ErrorMissingParameter, '필요한 파라미터 값이 제공되지 않았습니다.'),
                  }
