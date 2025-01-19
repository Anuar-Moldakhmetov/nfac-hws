import sys

def load_ascii_template(file_path: str) -> dict:
    with open(file_path, "r") as file:
        content = file.read().split("\n\n")  

    ascii_map = {}
    characters = [chr(i) for i in range(32, 127)]  

    for i, char in enumerate(characters):
        ascii_map[char] = content[i].splitlines()

    return ascii_map



def generate_ascii_text(input_text: str, ascii_map: dict) -> str:
    ascii_lines = [""] * 8  

    for char in input_text:
        if char == "\n":  
            ascii_lines = [""] * 8  
            print("\n".join(ascii_lines))  
            ascii_lines = [""] * 8
        elif char in ascii_map:  
            for i in range(8):
                ascii_lines[i] += ascii_map[char][i]
        else:  
            for i in range(8):
                ascii_lines[i] += " " * 8  

    return "\n".join(ascii_lines)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <text> <template_file>")
        return

    input_text = sys.argv[1]
    template_file = sys.argv[2]

    try:
        ascii_map = load_ascii_template(template_file)
        ascii_art = generate_ascii_text(input_text, ascii_map)
        print(ascii_art)
    except FileNotFoundError:
        print(f"Error: File '{template_file}' not found.")
    except IndexError:
        print("Error: Template file is corrupted or incomplete.")

if __name__ == "__main__":
    main()