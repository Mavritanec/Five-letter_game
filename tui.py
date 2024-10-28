from textual.app import App, ComposeResult
from textual.widgets import Button, Footer, Header, Log, Static

WORDS = []


class ListWords(Log):
    """
    Виджет для отображения допустимых слов.
    При запуске приложения, загружает полный словарь
     допустимых пяти-буквенных слов в виде списка.
    Потом, с каждым ходом в игре, обновляет список.
    """

    def on_mount(self) -> None:
        """Обработчик события, вызываемый при добавлении виджета в приложение."""

        with open('dictionary_preparation/final dictionary.txt', 'r', encoding='utf-8') as file:
            for word in file:
                WORDS.append(word)
                self.write_line(word)


class GameBoard(Static):
    """
    Виджет для отображения игрового поля.
    """

    # def compose(self) -> ComposeResult:
    #     """Создание дочерних виджетов для игрового поля."""



class WordGuessingApp(App):
    """
    Графическое приложение, работающее в консольном режиме.
    Помогает в игре "5-букв" от Т-банка.
    """

    CSS_PATH = "tui.tcss"

    BINDINGS = [("ctrl+d", "toggle_dark", "Переключение темной/светлой тем"),
                ("q", "app.quit", "Выход")]

    TITLE = "5-Букв. Игра от Т-Банка"

    def compose(self) -> ComposeResult:
        """Создание дочерних виджетов для приложения."""
        yield Header()
        yield Footer()
        yield ListWords(id="list_of_words")
        yield GameBoard(id="game_board")

    # def action_toggle_dark(self) -> None:
    #     """Действие для переключения темного режима."""
    #     self.dark = not self.dark


if __name__ == '__main__':
    WordGuessingApp().run()
