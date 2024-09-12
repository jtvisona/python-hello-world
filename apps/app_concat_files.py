
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
    output_file = filename + ".num"
    with open( output_file, "w" ) as file:
        for line in lines:
            file.write( f"{line}\n" )
            lines_counter += 1
    print( f"Wrote {lines_counter} lines to '{output_file}'." )

def number_lines( lines ):
    lines_counter = 0
    line_number = 1
    lines2 = []
    for line in lines:
        lines2.append( f"{line_number}\t{line}" )
        line_number += 1
        lines_counter += 1
    print( f"Numbered {lines_counter} lines." )
    return lines2

def print_lines ( lines ):
    lines_counter = 0
    for each_line in lines:
        print( f"{each_line}" )
        lines_counter += 1
    print( f"Printed {lines_counter} lines to stdout." )

def concat_files():
    lines1 = []
    lines2 = []
    filename1 = input( "Name of first file? " )
    filename2 = input( "Name of second file? " )
    read_lines( filename1, lines1 )
    read_lines( filename2, lines2 )
    write_lines( filename, lines1.append( lines2 ) )

def main():
    concat_files()

# if this module is called first, call the main function
if __name__ == "__main__":
    main()
