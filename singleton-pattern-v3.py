class Singleton:
    _instances = {}

    def __init__(self, class_):
        self._class = class_
        #self._instances = {} <- why is this here ???????

    def __call__(self, *args, **kwargs):
        if self._class not in self._instances:
            self._instances[self._class] = self._class(*args, **kwargs)
        return self._instances[self._class]

@Singleton
class FirstClass:
    def __init__(self, m):
        self.val = m

a = FirstClass(1)
b = FirstClass(23)

print(a == b)# True