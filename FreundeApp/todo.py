import flet as ft

meine_todos = []

def view_todo(page: ft.Page, header, back_button):
    todo_liste = ft.Column()

    def delete_task(zeile, text):
        # 1. Aus der Liste im Hintergrund löschen
        if text in meine_todos:
            meine_todos.remove(text)
        # 2. Aus der Anzeige auf dem Bildschirm löschen
        todo_liste.controls.remove(zeile)
        page.update()

    def add_todo(e):
        if todo_input.value.strip() != "":
            task_text = todo_input.value
            meine_todos.append(task_text)
            
            # Wir erstellen eine neue Zeile für das To-Do
            neue_zeile = ft.Row()
            
            # In die Zeile kommt das Häkchen und der Lösch-Knopf
            neue_zeile.controls = [
                ft.Checkbox(label=task_text, expand=True),
                ft.TextButton("Löschen", on_click=lambda _: delete_task(neue_zeile, task_text))
            ]
            
            todo_liste.controls.append(neue_zeile)
            todo_input.value = ""
            page.update()

    # Vorhandene Aufgaben beim Laden der Seite anzeigen
    for aufgabe in meine_todos:
        aktuelle_zeile = ft.Row()
        aktuelle_zeile.controls = [
            ft.Checkbox(label=aufgabe, expand=True),
            ft.TextButton("Löschen", on_click=lambda e, z=aktuelle_zeile, t=aufgabe: delete_task(z, t))
        ]
        todo_liste.controls.append(aktuelle_zeile)

    todo_input = ft.TextField(hint_text="Was steht an?", expand=True)
    add_btn = ft.ElevatedButton("Hinzufügen", on_click=add_todo)
    
    page.controls.clear()
    page.add(
        header, 
        back_button, 
        ft.Divider(),
        ft.Row([todo_input, add_btn]), 
        todo_liste
    )
    page.update()
        