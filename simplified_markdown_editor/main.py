import sys

class MarkdownFormatter:
    @staticmethod
    def plain(text):
        return text

    @staticmethod
    def bold(text):
        return f"**{text}**"

    @staticmethod
    def italic(text):
        return f"*{text}*"

    @staticmethod
    def inline_code(text):
        return f"`{text}`"

    @staticmethod
    def header(text):
        while True:
            try:
                level = int(input("Level: > "))
                if 1 <= level <= 6:
                    return f"{'#' * level} {text}"
                print("The level should be within the range of 1 to 6.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def link():
        label = input("Label: > ")
        url = input("URL: > ")
        return f"[{label}]({url})"

    @staticmethod
    def new_line():
        return "\n"

    @staticmethod
    def list_formatter(formatter):
        try:
            rows = int(input("Number of rows: > "))
            if rows <= 0:
                print("The number of rows should be greater than zero.")
                return ""
            items = [input(f"Row #{i + 1}: > ") for i in range(rows)]
            prefix = "- " if formatter == "unordered-list" else ""
            return "\n".join([f"{prefix}{i + 1}. {item}" if formatter == "ordered-list" else f"* {item}" for i, item in enumerate(items)]) + "\n"
        except ValueError:
            print("Invalid input. Please enter a number.")
            return ""

# Функція для виводу довідки

def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

# Основна функція програми

def main():
    markdown = ""
    formatter_map = {
        "plain": MarkdownFormatter.plain,
        "bold": MarkdownFormatter.bold,
        "italic": MarkdownFormatter.italic,
        "inline-code": MarkdownFormatter.inline_code,
        "header": MarkdownFormatter.header,
        "link": MarkdownFormatter.link,
        "new-line": MarkdownFormatter.new_line,
        "ordered-list": MarkdownFormatter.list_formatter,
        "unordered-list": MarkdownFormatter.list_formatter
    }
    
    while True:
        command = input("Choose a formatter: > ")
        
        if command == "!help":
            print_help()
        elif command == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(markdown)
            print("Markdown saved in output.md")
            break
        elif command in formatter_map:
            if command == "new-line":
                formatted_text = formatter_map[command]()
            elif command in ["ordered-list", "unordered-list"]:
                formatted_text = formatter_map[command](command)
            elif command == "link":
                formatted_text = formatter_map[command]()
            else:
                text = input("Text: > ")
                formatted_text = formatter_map[command](text)
            markdown += formatted_text + "\n"
            print(markdown.strip())
        else:
            print("Unknown formatting type or command")

# Запуск програми

if __name__ == "__main__":
    main()
