import string
import easygui
empty = True
while empty is True:
    sentence = easygui.enterbox("Enter sentence (without punctuation)")
    if not sentence:
        easygui.msgbox("You didn't enter anything...")
    elif any(punctuation in sentence for punctuation in string.punctuation):
        easygui.msgbox("Punctuation found!")
    else:
        empty = False
sentence = sentence.lower()
sentencelist = sentence.split()
search = easygui.enterbox("Word to find")
search = search.lower()
position = [i for i, found in enumerate(sentencelist) if found == search]
positions = 'and'.join(str(i) for i in position)
if len(position) >1: plural = "s "
else:
    plural = " "
if not position:
    easygui.msgbox("The word" + search + "wasn't found.")
else:
    easygui.msgbox("The word, " + search + ", was found at position" + plural + positions + ".")
input()
