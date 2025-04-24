from datetime import datetime


class Note:  # Note definition
    def __init__(self, subject, substance, priority, tags=None):
        self.subject = subject
        self.substance = substance
        self.priority = priority
        self.tags = tags if tags else []
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def filename(self):  # Return filename
        return f"{self.subject}.txt"

    def content(self):  # Sets the content of the note
        tags_str = ", ".join(self.tags) if self.tags else "None"
        return (
            f"Subject: {self.subject}\n"
            f"Priority: {self.priority}\n"
            f"Tags: {tags_str}\n"
            f"Timestamp: {self.timestamp}\n"
            f"---\n"
            f"{self.substance}\n"
        )
