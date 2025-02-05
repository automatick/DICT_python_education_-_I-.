from markdown_formatter import *

# Функція для виводу довідки

def print_help():
    print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
    print("Special commands: !help !done")

# Основна функція програми

def main():
    markdown = ""
    formatter_map = {
        "plain": plain,
        "bold": bold,
        "italic": italic,
        "inline-code": inline_code,
        "header": header,
        "link": link,
        "new-line": new_line,
        "ordered-list": list_formatter,
        "unordered-list": list_formatter
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
