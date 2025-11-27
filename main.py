from src.service_locator import ServiceLocator


def main():
    service_locator = ServiceLocator()

    service_locator.presenter.run()


if __name__ == "__main__":
    main()
