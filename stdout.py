# strings
msg = "This is a sample message.\n"
horizontal_rule = "--------\n"
hr = horizontal_rule # alias

# stdout and concat
print(hr + msg + hr)

# compare with stdout and append rather than concat
print(hr, msg, hr, end="<END>")