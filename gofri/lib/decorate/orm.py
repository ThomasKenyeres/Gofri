class GofriEntity:
    def __init__(self, static=True):
        self.static = static

    def __call__(self, cls):
        if self.static:
            pass
        else:
            pass