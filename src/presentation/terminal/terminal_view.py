from src.presentation.view_interfaz import ViewInterfaz


class Terminal(ViewInterfaz):
    def show(self, message: str) -> None:
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)

    def run(self, presenter) -> None:
        presenter.show_welcome()

        while True:
            presenter.show_menu()

            choice = presenter.get_menu_choice()
            self.show("")

            if choice == "1":
                presenter.add_user()
            elif choice == "2":
                presenter.list_users()
            elif choice == "3":
                presenter.show_goodbye()
                break
            else:
                presenter.show_invalid_option()
