from . import Webbrowser

class BerkeliumBrowser():
    def build(self):
        return Webbrowser(url='http://google.fr/', transparency=False)

if __name__ == '__main__':
    BerkeliumBrowser().run()
