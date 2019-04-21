from abc import ABCMeta, abstractmethod
import dash

class DashPage(metaclass=ABCMeta):

    @abstractmethod
    def layout(self):
        pass

    @abstractmethod
    def callbacks(self):
        pass

    @classmethod
    def as_app(cls, *args, **kwargs):

        page = cls()

        app = dash.Dash(*args, **kwargs)

        app.layout = page.layout()

        for callback in page.callbacks():
            app.callback(*callback.get_args())(callback)

        return app

