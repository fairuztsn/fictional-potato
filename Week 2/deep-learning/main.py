class MyError(BaseException):
    def __init__(self, args):
        super.__init__(args)

raise MyError("Test")