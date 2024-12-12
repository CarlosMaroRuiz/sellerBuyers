class CustomAppException(Exception):
    def __init__(self, code_error: int, msg: str, status_code: int = 400):
        self.code_error = code_error
        self.msg = msg
        self.status_code = status_code
