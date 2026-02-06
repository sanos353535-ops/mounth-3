from datetime import datetime

import flet as ft


def app(page: ft.Page):
    # button = ft.Button(content="Кнопка")
    plain_text = ft.Text(value="Hello world!")
    # page.theme_mode = ft.ThemeMode.LIGHT
    history = []

    def clear_history(e):
        history.clear()
        history_text.value = ""

    delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    history_text = ft.Text()

    def change_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK

    icon_button = ft.IconButton(icon=ft.Icons.SMART_BUTTON, on_click=change_theme)

    def change(e):
        txt = user_input.value.strip()
        user_input.value = ""
        history.append(txt)
        print(history)
        history_text.value = "История имён: \n" + ", \n".join(history)
        date = datetime.now().strftime("%Y-%m-%d - %H:%M:%S")

        if txt:
            plain_text.color = None
            plain_text.value = f"{date} Hello {txt}"
        else:
            plain_text.value = "Введите правильное имя!"
            plain_text.color = ft.Colors.RED

    # button.content = "Другая кнопка"
    # button.color = ft.Colors.GREEN_900
    btn = ft.TextButton("Отправить", on_click=change)

    user_input = ft.TextField(label="Enter name", on_submit=change)
    row = ft.Row([user_input, btn, history_text, icon_button],alignment=ft.MainAxisAlignment.START)
    page.add(plain_text, row, delete_button)


ft.app(app)