# strings
msg = "This is a sample message.\n"
horizontal_rule = "--------\n"
hr = horizontal_rule # alias

"""
This is a block comment.
"""

# stdout and concat
print( hr + msg + hr )

# compare with stdout and append rather than concat
print( hr, msg, hr, end="<END>\n" )

# use the length function to measure strings
print()
print( "len(hr) = ", hr )