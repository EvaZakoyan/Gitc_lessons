
# Convert the number entered by the user to bytes or kilobytes, choised by user

a = float(input("input any number"))
cbs = input('Choise you want to convert to "b to kb" or "kb to b"')

if cbs == "b to kb":
    print(f" {a} bytes =  {a / 1024} kilobytes")
if cbs == "kb to b":
    print(f" {a} kilobytes = {a * 1024} bytes ")