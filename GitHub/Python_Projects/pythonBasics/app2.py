import pythonBasics.app as app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    print('I am confused with {}.'.format(app.print_app()))
    print('calling from this page: {}'.format(print_app2()))
