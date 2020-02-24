#!/usr/bin/env python2
hello_str = "Hello World"

hello_int = 21

hello_bool = True

hello_tuple = (21, 32)

hello_list = ["Hello,","this","is","a","list"]

hello_list = list()
hello_list.append("Hello,")
hello_list.append("this")
hello_list.append("is")
hello_list.append("a")
hello_list.append("list")

hello_dict = {"first_name":"Dave",
            "last_name":"Snyder",
            "eye_colour":"blue"}

print(hello_list)
hello_list[4]+="!"

hello_list[4] = hello_list[4] + "!"
print(hello_list[4])

print(str(hello_tuple[0]))

print(hello_dict["first_name"]+" "+hello_dict["last_name"]+" has "+
    hello_dict["eye_colour"]+" eyes.")

print("{0}{1}has{2}eyes.".format(hello_dict["first_name"],hello_dict["last_name"],
    hello_dict["eye_colour"]))
