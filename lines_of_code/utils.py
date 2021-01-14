import re

def scan_lines(lines, defs):
    """
    Function to return number of comment and blank lines using list of lines 
    from parameter lines and using the definition provided by defs based on the file extension
    """

    blank_lines = 0
    comment_lines = 0

    i = 0

    while(i < len(lines)):

        line = lines[i].strip()

        if re.match(defs['empty_line'], line):
            blank_lines += 1

        elif line.startswith(defs['comment']):
            comment_lines += 1
        
        elif line.startswith(defs['multiline_comment_start']):
            #multiline comment start
            if line.count(defs['multiline_comment_start']) == 2:
                comment_lines += 1

            elif line.endswith(defs['multiline_comment_end']) \
                and (defs['multiline_comment_start'] != defs['multiline_comment_end']):
                comment_lines += 1

            else:
                comment_lines += 1; i += 1 
                while defs['multiline_comment_end'] not in lines[i]:  # iterating in multiline comment 
                    comment_lines += 1
                    i += 1
                
                comment_lines += 1 # multiline comment end
        else:
            pass

        i += 1

    return blank_lines, comment_lines
