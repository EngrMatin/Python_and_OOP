import re
lst = ["text", "be", "there"]
text = "This is an example [word]. Normally there would [word] something important here but [word] isn't."

text = re.sub(r"\[word\]", lambda _, i=iter(lst): next(i), text)
print(text)

list = ['text', 'be', 'there']
text = "This is an example [word]. Normally there would [word] something important here but [word] isn't."
output = re.sub(r'\[word\]', list.pop(), text)
print(output)

words = ['text', 'be', 'there']
text = "This is an example [word]. Normally there would [word] something important here but [word] isn't."

print(''.join(w for p in zip(text.split('[word]'), (*words, '')) for w in p))

s = 'in may 1999, nothing really happened, same as in june 1999'
month_set = {'may', 'june', 'july'}
final_string = ' '.join("month" if i in month_set else i for i in s.split())
print(final_string)

# l = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
# s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

# b = list(s.split())
# for i in range(len(l)-1):
#     for x in b:
#         if x==l[i]:
#             s = s.replace(x, l[i+1])
# print(s)


