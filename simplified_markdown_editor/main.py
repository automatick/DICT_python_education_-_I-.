import sys

# Функція для виводу довідки

def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

# Функція для форматування тексту відповідно до вибраного форматтера

def format_text(formatter, text):
    if formatter == "plain":
        return text
    elif formatter == "bold":
        return f"**{text}**"
    elif formatter == "italic":
        return f"*{text}*"
    elif formatter == "inline-code":
        return f"`{text}`"
    elif formatter == "header":
        level = int(input("Level: > "))
        if 1 <= level <= 6:
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6.")
            return ""
    elif formatter == "link":
        label = input("Label: > ")
        url = input("URL: > ")
        return f"[{label}]({url})"
    elif formatter == "new-line":
        return "\n"
    elif formatter in ("ordered-list", "unordered-list"):
        try:
            rows = int(input("Number of rows: > "))
            if rows <= 0:
                print("The number of rows should be greater than zero.")
                return ""
            items = []
            for i in range(1, rows + 1):
                items.append(input(f"Row #{i}: > "))
            prefix = "- " if formatter == "unordered-list" else ""
            return "\n".join([f"{prefix}{i + 1}. {item}" if formatter == "ordered-list" else f"* {item}" for i, item in enumerate(items)]) + "\n"
        except ValueError:
            print("Invalid input. Please enter a number.")
            return ""
    else:
        print("Unknown formatting type or command")
        return ""

# Основна функція програми

def main():
    markdown = ""
    
    while True:
        command = input("Choose a formatter: > ")
        
        if command == "!help":
            print_help()
        elif command == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write(markdown)
            print("Markdown saved in output.md")
            break
        elif command in ["plain", "bold", "italic", "inline-code", "header", "link", "ordered-list", "unordered-list", "new-line"]:
            text = "" if command == "new-line" else input("Text: > ")
            markdown += format_text(command, text) + "\n"
            print(markdown.strip())
        else:
            print("Unknown formatting type or command")

# Запуск програми

if __name__ == "__main__":
    main()

