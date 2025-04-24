import os
from note import Note


class NoteApp:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def _get_priority_dir(self, priority):
        path = os.path.join(self.base_dir, str(priority))
        os.makedirs(path, exist_ok=True)
        return path

    def add_note(self, subject, substance, priority, tags=None):
        note = Note(subject, substance, priority, tags)
        path = self._get_priority_dir(priority)
        filepath = os.path.join(path, note.filename())
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(note.content())
        print(f"Note saved: {filepath}")

    def list_notes(self):
        print("Listing all notes by priority:")
        for priority_folder in sorted(os.listdir(self.base_dir)):
            folder_path = os.path.join(self.base_dir, priority_folder)
            if os.path.isdir(folder_path):
                print(f"\nPriority {priority_folder}:")
                for file in os.listdir(folder_path):
                    print(f"  - {file.replace('.txt', '')}")

    def delete_note(self, subject):
        deleted = False
        for priority_folder in os.listdir(self.base_dir):
            path = os.path.join(self.base_dir, priority_folder, f"{subject}.txt")
            if os.path.exists(path):
                os.remove(path)
                print(f"Deleted: {path}")
                deleted = True
        if not deleted:
            print("Note not found.")
