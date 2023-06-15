
class Application:

    name: str

    def __init__(self, *, name: str) -> None:
        self.set_name(name=name)
        self.name: str = self.get_name()

    def set_name(self, *, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        self.name

    def __repr__(self) -> str:
        return self.name
