import flet as ft
import google.generativeai as genai

# DEIN KEY (Bitte hier nochmal prüfen!)
API_KEY = "AIzaSyCOHiujaYm1xQyz90rdela01XQlxYHSeX8"

genai.configure(api_key=API_KEY)

# Wir versuchen das aktuellste Modell
MODEL_NAME = 'models/gemini-2.5-flash' 

def view_bot(page: ft.Page, header, back_button):
    chat_verlauf = ft.Column(scroll="always", expand=True)

    def get_ai_response(prompt):
        try:
            model = genai.GenerativeModel(MODEL_NAME)
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            # Wenn es nicht geht, listet der Bot hier zur Hilfe alle Modelle auf, die DU nutzen darfst
            error_msg = str(e)
            if "404" in error_msg:
                try:
                    available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
                    return f"Modell-Fehler! Google sagt, dieses Modell gibt es nicht. Versuche eines von diesen: {', '.join(available_models)}"
                except:
                    return "Konnte Modell-Liste nicht laden. Prüfe deinen API-Key!"
            return f"Fehler: {error_msg}"

    def send_message(e):
        if input_feld.value.strip() != "":
            user_text = input_feld.value
            chat_verlauf.controls.append(
                ft.Row([ft.Container(content=ft.Text(user_text, color="white"), bgcolor="blue700", padding=10, border_radius=10)], alignment="end")
            )
            
            # Platzhalter für die Bot-Antwort
            bot_container = ft.Container(content=ft.Text("KI schreibt..."), bgcolor="grey800", padding=10, border_radius=10)
            chat_verlauf.controls.append(ft.Row([bot_container], alignment="start"))
            page.update()

            # Antwort holen
            antwort = get_ai_response(user_text)
            bot_container.content = ft.Text(antwort, selectable=True)
            input_feld.value = ""
            page.update()

    input_feld = ft.TextField(hint_text="Frag mich was...", expand=True, on_submit=send_message)
    btn_send = ft.Button("KI Fragen", on_click=send_message)

    page.controls.clear()
    page.add(
        header,
        back_button,
        ft.Divider(),
        ft.Container(content=chat_verlauf, height=400, bgcolor="black26", border_radius=15, padding=15),
        ft.Row([input_feld, btn_send])
    )
    page.update()