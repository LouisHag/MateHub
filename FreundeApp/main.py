import flet as ft
import todo, chat, spiele, bot

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    
    def get_header(titel):
        return ft.Text(titel, size=30, weight="bold")

    def show_dashboard(e=None):
        page.controls.clear()
        
        btn_width = 400
        btn_height = 70
        font_size = 22

        page.add(
            get_header("Meine Übersicht"),
            ft.Divider(height=20, color="transparent"), 
            
            ft.Column([
                # To-Do Button
                ft.ElevatedButton(
                    content=ft.Text("To-Do Liste", size=font_size, weight="w500"),
                    width=btn_width,
                    height=btn_height,
                    on_click=lambda _: todo.view_todo(
                        page, 
                        get_header("To-Do"), 
                        ft.ElevatedButton("Zurück", on_click=show_dashboard)
                    )
                ),
                
                # Chat Button
                ft.ElevatedButton(
                    content=ft.Text("Kollegen-Chat", size=font_size, weight="w500"),
                    width=btn_width,
                    height=btn_height,
                    on_click=lambda _: chat.view_chat(
                        page, 
                        get_header("Chat"), 
                        ft.ElevatedButton("Zurück", on_click=show_dashboard), 
                        "Louis"
                    )
                ),
                
                # Spiele Button
                ft.ElevatedButton(
                    content=ft.Text("Spiele-Ecke", size=font_size, weight="w500"),
                    width=btn_width,
                    height=btn_height,
                    on_click=lambda _: spiele.view_spiele(
                        page, 
                        get_header("Spiele"), 
                        ft.ElevatedButton("Zurück", on_click=show_dashboard)
                    )
                ),

                # In der Column deiner main.py:
                ft.ElevatedButton(
                    content=ft.Text("🤖 Chat-Bot", size=22),
                    width=400,
                    height=70,
                    on_click=lambda _: bot.view_bot(page, get_header("Bot"), ft.ElevatedButton("Zurück", on_click=show_dashboard))
                )
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20 # Das macht den Abstand ZWISCHEN den Buttons größer
            )
        )
        page.update()

    show_dashboard()

if __name__ == "__main__":
    ft.app(target=main)   
