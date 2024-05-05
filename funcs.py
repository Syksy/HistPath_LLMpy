import re

# LLama does not fully adhere to the JSON standard, and requires additional parsing/sanitization to be JSON-readable
def jsonSanitize(text):
    return re.sub(": 3\+3", ": \"3+3\"", re.sub(": 3\+4", ": \"3+4\"", re.sub(": 4\+3", ": \"4+3\"",
        # Some convenience subs
        re.sub(": NA", ": \"NA\"", re.sub("\)\n", "\n", re.sub("\),",",", re.sub(": \(",": ",
            # Native json.loads cannot handle //-comments at the end of lines in JSON files (?)
            re.sub("\/\/.*","", text)))))
        )))

