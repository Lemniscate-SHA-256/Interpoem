from interpoem.parser import parser
from interpoem.interpreter import interpret_poem

def main():
    with open('poems/example.poem', 'r') as file:
        data = file.read()
    
    parsed_poem = parser.parse(data)
    html_output = interpret_poem(parsed_poem)
    
    with open('poem.html', 'w') as file:
        file.write(html_output)
    print("Poem rendered to poem.html")

if __name__ == "__main__":
    main()
