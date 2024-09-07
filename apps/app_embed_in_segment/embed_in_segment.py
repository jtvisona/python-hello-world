
lines_counter = 0

def read_lines( filename, lines ):
    lines_counter = 0
    with open( filename ) as file:
        for line in file:
            line = line.replace( "\n", "" )
            lines.append( line )
            lines_counter += 1
    print( f"Read {lines_counter} lines from '{filename}'." )
    return lines

def write_lines( filename, lines ):
    lines_counter = 0
    output_file = filename + ".out"
    with open( output_file, "w" ) as file:
        for line in lines:
            file.write( f"{line}\n" )
            lines_counter += 1
    print( f"Wrote {lines_counter} lines to '{output_file}'." )

def number_lines( lines ):
    lines2 = []
    lines2.append( "### Source" )
    lines2.append( "```" )
    for line in lines:
        lines2.append( f"{line}" )
    lines2.append( "```" )
    lines2.append( "" )
    lines2.append( "### Output" )
    lines2.append( "```" )
    lines2.append( "" )
    lines2.append( "" )
    lines2.append( "```" )
    lines2.append( "### Explanation" )
    lines2.append( "" )
    lines2.append( "### Details" )
    lines2.append( "*" )
    lines2.append( "---" )
    lines2.append( f"Embedded lines in md." )
    return lines2

def print_lines ( lines ):
    lines_counter = 0
    for each_line in lines:
        print( f"{each_line}" )
        lines_counter += 1
    print( f"Printed {lines_counter} lines to stdout." )

def main():
    file_lines = []
    filename = input( "Name of file? " )
    read_lines( filename, file_lines )
    file_lines = number_lines( file_lines )
    print_lines( file_lines )
    write_lines( filename, file_lines )

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
