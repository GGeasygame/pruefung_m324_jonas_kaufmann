import markdown
import os

def convert_markdown_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Die Datei {input_file} existiert nicht.")
        return

    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()

        html_content = markdown.markdown(markdown_content)

        with open(output_file, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)

        print(f"Die Datei {output_file} wurde erfolgreich erstellt.")

    except Exception as e:
        print(f"Fehler bei der Konvertierung: {e}")

if __name__ == "__main__":
    input_markdown_file = "task-3.md"
    output_html_file = "task-3.html"

    convert_markdown_to_html(input_markdown_file, output_html_file)
