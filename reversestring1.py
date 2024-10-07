str = "i.like.this.program.very.much"

str_split = str.split(".")

str_split.reverse()

print(str_split)

result = ''


for element in str_split:
    result += element + '.'

print(result)

result_new = result.rstrip(".")

print(result_new)