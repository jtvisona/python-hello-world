FILENAME = "target.txt"

def write_lines( lines ):
    with open( FILENAME, "w" ) as file:
        for line in lines:
            file.write( f"{line}\n" )

def read_lines():
    lines = []
    with open( FILENAME ) as file:
        for line in file:
            line = line.replace( "\n", "" )
            lines.append( line )
    return lines

def list_lines( lines ):
    for c, lines in enumerate( lines, start=1 ):
        print( f"{c}.{line}" )
    print()
  
def add_line( lines ):
    line = input("line: ")
    lines.append( line )
    write_lines( lines )
    print( f"{line} was added.\n" )

def delete_line( lines ):
    index = int( input( "Number: " ) )
    if index < 1 or index > len( lines ):
        print( "Invalid line number.\n" )
    else:
        line = lines.pop( index - 1 )
        write_lines( lines )
        print( f"'{line}' deleted.\n" )
        
def display_menu():
    print("The line List program")
    print()
    print("COMMAND MENU")
    print("list - List all lines")
    print("add -  Add a line")
    print("del -  Delete a line")
    print("exit - Exit program")
    print()
    
def main():
    display_menu()
    lines = read_lines()
    while True:
        command = input( "Command: " )
        if command.lower() == "list":
            list_lines(lines)
        elif command.lower() == "add":
            add_line(lines)
        elif command.lower() == "del":
            delete_line(lines)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.")

if __name__ == "__main__":
    main()
