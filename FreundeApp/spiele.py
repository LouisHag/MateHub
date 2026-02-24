import flet as ft

def view_spiele(page: ft.Page, header, back_button):
    score = ft.Text("0", size=40, weight="bold")

    def count_up(e):
        score.value = str(int(score.value) + 1)
        page.update()

    page.controls.clear()
    page.add(
        header,
        back_button,
        ft.Divider(),
        ft.Column([
            ft.Text("Klick-Duell 🎮", size=25),
            ft.Text("Wie schnell kannst du klicken?"),
            score,
            ft.ElevatedButton("KLICK MICH!", on_click=count_up, height=50, width=200)
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
    page.update()