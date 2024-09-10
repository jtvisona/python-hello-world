# Demonstrate basic string functionality
temp_string = "   This is a string: TESTING.   "
temp_int = "41234"
temp_lower = "apples"
temp_upper = "ZEBRA"
temp_alphanumeric = "abc123"
temp_allwhitespace = "\t \t"

print( f"'{temp_string}'" )            # As is
print( f"'{temp_string.upper()}'" )    # All to uppercase
print( f"'{temp_string.lower()}'" )    # All to lowercase
print ( f"'{temp_string.lstrip()}'" )    # Remove preceding whitespace
print ( f"'{temp_string.rstrip()}'" )   # Remove trailing whitespace
print( f"'{temp_string.strip()}'" )    # Remove preceding and trailing whitespace

if( temp_int.isdigit ):    # only characters 0-9
    print( f"'{temp_int}' is a digit" )
if( temp_int.isdecimal ):  # digits plus some other Unicode values
    print( f"'{temp_int}' is decimal" )
if( temp_lower.isalpha ):  # alphabetic characters
    print( f"'{temp_lower}' is alphabetic" )
if( temp_alphanumeric.isalnum ): # alphanumeric characters
    print( f"'{temp_alphanumeric}' is alphanumeric" )
if( temp_lower.islower ):    # lowercase characters
    print( f"'{temp_lower}' is lowercase" )
if( temp_upper.isupper ):    # uppercase characters
    print( f"'{temp_upper}' is uppercase" )
if( temp_allwhitespace.isspace ):      # whitespace only
    print( f"'{temp_allwhitespace}' is all whitespace" )
if( temp_allwhitespace.isascii ):      # ASCII charactersss
    print( f"'{temp_alphanumeric}{temp_allwhitespace}{temp_upper}' is all ASCII characters" )