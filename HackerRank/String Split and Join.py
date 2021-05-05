def split_and_join(line):
    line=line.split()
    output="-".join(line)
    return output

output=split_and_join(input("Enter a String :"))
print(output)
