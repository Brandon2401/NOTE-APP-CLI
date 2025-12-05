from lib.db.models import session, Note
from datetime import datetime

def create_note():
    title = input("\nEnter note title: ")
    body = input("Enter note body: ")
    tags = input("Enter tags (comma separated): ")

    note = Note(
        title=title,
        body=body,
        tags=tags,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )

    session.add(note)
    session.commit()
    print("\n✔ Note created successfully!\n")


def list_notes():
    notes = session.query(Note).all()

    if not notes:
        print("\nNo notes found.\n")
        return

    print("\n===== ALL NOTES =====")
    for note in notes:
        print(f"""
ID: {note.id}
Title: {note.title}
Tags: {note.tags}
Created: {note.created_at}
Updated: {note.updated_at}
-----------------------------------
{note.body}
""")


def search_notes():
    keyword = input("\nEnter keyword to search: ")

    notes = session.query(Note).filter(
        Note.title.like(f"%{keyword}%") |
        Note.body.like(f"%{keyword}%") |
        Note.tags.like(f"%{keyword}%")
    ).all()

    if not notes:
        print("\nNo matching notes found.\n")
        return

    print("\n===== SEARCH RESULTS =====")
    for note in notes:
        print(f"""
ID: {note.id}
Title: {note.title}
Tags: {note.tags}
-----------------------------------
{note.body}
""")


def edit_note():
    try:
        note_id = int(input("\nEnter note ID to edit: "))
    except:
        print("Invalid ID.")
        return

    note = session.query(Note).get(note_id)
    if not note:
        print("\nNote not found.")
        return

    print("\nLeave blank to keep existing value.")

    new_title = input(f"New title [{note.title}]: ") or note.title
    new_body = input(f"New body [{note.body}]: ") or note.body
    new_tags = input(f"New tags [{note.tags}]: ") or note.tags

    note.title = new_title
    note.body = new_body
    note.tags = new_tags
    note.updated_at = datetime.now()

    session.commit()
    print("\n✔ Note updated successfully!\n")


def delete_note():
    try:
        note_id = int(input("\nEnter note ID to delete: "))
    except:
        print("Invalid ID.")
        return

    note = session.query(Note).get(note_id)
    if not note:
        print("\nNote not found.\n")
        return

    session.delete(note)
    session.commit()
    print("\n✔ Note deleted successfully!\n")
