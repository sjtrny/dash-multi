from abc import ABC, abstractmethod


class Route:
    """
    Struct to represent a route
    """

    def __init__(self, app_cls, name, url_base_pathname):
        self.app_cls = app_cls
        self.name = name
        self.url_base_pathname = url_base_pathname


class MultiPageApp(ABC):
    def __init__(self, name, server, url_base_pathname):
        # Name gets ignored, as we delegate naming to sub-apps

        routes = self.get_routes()

        for route in routes:

            route.app_cls(
                name=route.name,
                server=server,
                url_base_pathname=url_base_pathname + route.url_base_pathname,
            )

    @abstractmethod
    def get_routes(self):
        pass
