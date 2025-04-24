import argparse
import os
from noteMethods import NoteApp

# Default save location - Desktop/MyNotesApp
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
notes_path = os.path.join(desktop, "MyNotesApp")
app = NoteApp(notes_path)


def main():
    parser = argparse.ArgumentParser(description="OOP CLI Note App")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("subject", help="Subject of the note (filename)")
    add_parser.add_argument("substance", help="The main text of the note")
    add_parser.add_argument("--priority", type=int, default=1, help="Priority level")
    add_parser.add_argument("--tags", nargs="*", help="Optional tags (space separated)", default=[])

    # List command
    subparsers.add_parser("list", help="List all notes by priority")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a note by subject")
    delete_parser.add_argument("subject", help="Subject of the note to delete")

    args = parser.parse_args()

    if args.command == "add":
        app.add_note(args.subject, args.substance, args.priority, args.tags)
    elif args.command == "list":
        app.list_notes()
    elif args.command == "delete":
        app.delete_note(args.subject)


if __name__ == "__main__":
    main()
