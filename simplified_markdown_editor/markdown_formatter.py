def plain(text):
    return text

def bold(text):
    return f"**{text}**"

def italic(text):
    return f"*{text}*"

def inline_code(text):
    return f"`{text}`"

def header(text):
    while True:
        try:
            level = int(input("Level: > "))
            if 1 <= level <= 6:
                return f"{'#' * level} {text}"
            print("The level should be within the range of 1 to 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def link():
    label = input("Label: > ")
    url = input("URL: > ")
    return f"[{label}]({url})"

def new_line():
    return "\n"

def list_formatter(formatter):
    while True:
        try:
            rows = int(input("Number of rows: > "))
            if rows <= 0:
                print("The number of rows should be greater than zero.")
                continue
            items = [input(f"Row #{i + 1}: > ") for i in range(rows)]
            prefix = "- " if formatter == "unordered-list" else ""
            return "\n".join([f"{prefix}{i + 1}. {item}" if formatter == "ordered-list" else f"* {item}" for i, item in enumerate(items)]) + "\n"
        except ValueError:
            print("Invalid input. Please enter a number.")
