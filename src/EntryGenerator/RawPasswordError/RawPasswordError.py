
class RawPasswordError(ValueError):

    def __init__(self, error_message: str):
        super().__init__(error_message)