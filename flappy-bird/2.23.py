def add_not_to_str(string):
    if string[0:4] =="not ":
        return string
    else:
        return "not " + string
# to get rid of extra spaces at beginning and end of string is string.strip()

str = input("what is your word/phrase?")
str = str.strip()
new_phrase = add_not_to_str(str)
print(new_phrase)