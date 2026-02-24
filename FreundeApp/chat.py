import flet as ft

nachrichten = []

def view_chat(page: ft.Page, header, back_button, user_name):
    chat_verlauf = ft.Column(scroll="always", expand=True)
    
    for msg in nachrichten:
        chat_verlauf.controls.append(ft.Text(msg))

    def send_message(e):
        if chat_input.value.strip() != "":
            text = f"{user_name}: {chat_input.value}"
            nachrichten.append(text)
            chat_verlauf.controls.append(ft.Text(text))
            chat_input.value = ""
            page.update()

    chat_input = ft.TextField(hint_text="Nachricht...", expand=True)
    send_btn = ft.ElevatedButton("Senden", on_click=send_message)
    
    page.controls.clear()
    page.add(
        header, 
        back_button, 
        ft.Container(content=chat_verlauf, height=300, bgcolor="black12"), 
        ft.Row([chat_input, send_btn])
    )
    page.update()