# https://habr.com/ru/articles/774254/

# https://github.com/textualize/textual/
# https://textual.textualize.io/getting_started/

from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Static


class TimeDisplay(Static):
    """Виджет для отображения прошедшего времени."""

    start_time = reactive(monotonic)
    time = reactive(0.0)
    total = reactive(0.0)

    def on_mount(self) -> None:
        """Обработчик события, вызываемый при добавлении виджета в приложение."""
        self.update_timer = self.set_interval(1 / 60, self.update_time, pause=True)

    def update_time(self) -> None:
        """Метод обновления времени до текущего времени."""
        self.time = self.total + (monotonic() - self.start_time)

    def watch_time(self, time: float) -> None:
        """Вызывается при изменении атрибута времени."""
        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        self.update(f"{hours:02,.0f}:{minutes:02.0f}:{seconds:05.2f}")

    def start(self) -> None:
        """Метод запуска (или возобновления) обновления времени."""
        self.start_time = monotonic()
        self.update_timer.resume()

    def stop(self) -> None:
        """Метод остановки обновления дисплея времени."""
        self.update_timer.pause()
        self.total += monotonic() - self.start_time
        self.time = self.total

    def reset(self) -> None:
        """Метод сброса показаний времени на ноль."""
        self.total = 0
        self.time = 0


class Stopwatch(Static):
    """Виджет с секундомером."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Обработчик события, вызываемый при нажатии кнопки."""
        button_id = event.button.id
        time_display = self.query_one(TimeDisplay)
        if button_id == "start":
            time_display.start()
            self.add_class("started")
        elif button_id == "stop":
            time_display.stop()
            self.remove_class("started")
        elif button_id == "reset":
            time_display.reset()

    def compose(self) -> ComposeResult:
        """Создание дочерних виджетов секундомера."""
        yield Button("Старт", id="start", variant="success")
        yield Button("Стоп", id="stop", variant="error")
        yield Button("Сброс", id="reset")
        yield TimeDisplay()


class StopwatchApp(App):
    """Textual приложение для управления секундомерами."""

    CSS_PATH = "stopwatch.tcss"
    BINDINGS = [("d", "toggle_dark", "Переключение светлого / темного режимов"),
                ("a", "add_stopwatch", "Добавить секундомер"),
                ("r", "remove_stopwatch", "Удалить секундомер")]

    def compose(self) -> ComposeResult:
        """Создание дочерних виджетов для приложения."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(Stopwatch(), Stopwatch(), Stopwatch(), id="timers")

    def action_add_stopwatch(self) -> None:
        """Действие для добавления таймера."""
        new_stopwatch = Stopwatch()
        self.query_one("#timers").mount(new_stopwatch)
        new_stopwatch.scroll_visible()

    def action_remove_stopwatch(self) -> None:
        """Действие для удаления таймера."""
        timers = self.query("Stopwatch")
        if timers:
            timers.last().remove()

    def action_toggle_dark(self) -> None:
        """Действие для переключения темного режима."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = StopwatchApp()
    app.run()
