to_21 = [i for i in range(1, 22)]
print to_21

odds = to_21[::2]
print odds

middle_third = to_21[len(to_21)/3:len(to_21)-(len(to_21)/3)]
print middle_third

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message

print ~88