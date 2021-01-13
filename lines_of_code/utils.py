def get_blank_lines(lines, defs):

    blank_lines = 0

    for line in lines:
        if line == '\n':
            blank_lines += 1
    
    return blank_lines

def get_comment_lines(lines, defs):

    comment_lines = 0

    for line in lines:
        if line.startswith(defs['comment']):
            comment_lines += 1

    return comment_lines 
