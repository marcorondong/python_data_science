ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

# For list
ft_list[1] = "World!"
# ft_list.pop()
# ft_list.append("World!")

# For tuples
# They are immutable, so I need to overwrite it
ft_tuple = ("Hello", "Austria!")

# For set
# A set is a collection which is unordered, unchangeable*, and un-indexed
# But even that its items are unchangeable, I can remove and add new items
ft_set.remove("tutu!")
ft_set.add("Vienna!")

# For  dictionaries
ft_dict["Hello"] = "42Vienna!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)