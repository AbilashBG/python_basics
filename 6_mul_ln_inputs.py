
para=[]
print("Enter a para : ")


# while True is used for infinity loop
while True:
    line=input()
    # below if condition checks input not empty
    if line:
        para.append(line)

    # below else condition stops the loop
    else:
        break

    print(para)

    # output

# Enter a para :
# hello
# ['hello']
# this is test string
# ['hello', 'this is test string']
# which is for testing purpose
# ['hello', 'this is test string', 'which is for testing purpose']

# below code prints every inputs in each line
    output="\n".join(para)
    print(output)

# output

# hello Ram.
# This is correct code
# I am not sure on this
# please explain this correctly
