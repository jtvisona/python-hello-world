"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
html_converter.py
"""

def main():

    print( "HTML Converter\n" )

    filename = "Assignments\Assignment7 Deliverables\index.html"
    html = ""
    
    with open( filename, "r" ) as file:
        for line in file:
            html += line.lstrip()
    text = html \
        .replace( "<h1>", "" ) \
        .replace( "</h1>", "" ) \
        .replace( "<ul>", "" ) \
        .replace( "</ul>", "" ) \
        .replace( "<li>", "* " ) \
        .replace( "</li>", "" ) \
        .replace( "\n\n", "\n" ) \
        .strip()
    print( text )

if __name__ == "__main__":
    main()