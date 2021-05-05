def mutate_string(string, position, character):
    lst=list(string)
    lst[position]=character
    output="".join(lst)
    return output

output=mutate_string(input("Enter a String:"),int(input("Enter position of the string to be replaced:"))
                     ,input("Enter the character to be updated at position"))
print(output)
