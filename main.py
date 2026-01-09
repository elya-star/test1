import flet as ft
import datetime as dt

def main(page: ft.Page):
    text_hello = ft.Text(value="Hello World!", color=ft.Colors.GREEN_200)
    greeting_history = []
    greeting_text = ft.Text('История приветствия')

    def on_button_click(_):
        page.title = "Моё первое тестовое приложение"
        page.theme_mode = ft.ThemeMode.LIGHT


        name = name_input.value.strip()
        print(name)
        if name:
            now = dt.datetime.now()
            time_str = now.strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.color = None
            text_hello.value = f"{time_str} - Hello, {name}"
            name_input.value = ''

            greeting_history.append(name)
            print(greeting_history)
            greeting_text.value = "История приветсвий: \n" + "\n".join(greeting_history)


        else:
            text_hello.value = "Введите корректное имя" 
            text_hello.color = ft.Colors.RED_200
        page.update()

    
    eleveted_button = ft.ElevatedButton("SEND", icon=ft.Icons.SEND, on_click=on_button_click)
    def clear_history(_):
        greeting_history.clear()
        greeting_text.value = 'История приветсвия'

    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    main_object = ft.Row([name_input, eleveted_button, clear_button])

    text_row = ft.Row([text_hello], alignment=ft.MainAxisAlignment.CENTER)

    page.add(text_row, main_object, greeting_text)

ft.run(main, view=ft.AppView.WEB_BROWSER, port=8550)
    

