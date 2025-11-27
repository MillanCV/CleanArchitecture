from src.service_locator import ServiceLocator


class Application:
    def __init__(self):
        self.service_locator = ServiceLocator()

    def run(self):
        view = self.service_locator.view
        presenter = self.service_locator.presenter
        view.run(presenter)


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
