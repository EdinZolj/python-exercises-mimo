#Every element in a list has a numbered position called an index. Starting by "0".

#With both "append()" and "insert()" we can add JUST ONE ELEMENT AT A TIME.
initials = ["RM", "LP"]
initials.append("LC")
initials.insert(1, "LS")
print(initials)

#...to remove the last element of a list, we use the instruction "pop()".
todo = ["call mom", "dishes"]
todo.pop()
print(todo)