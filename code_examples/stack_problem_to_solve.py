#create empty stacks to work with
input_ = []
control_y = []

# enter all the user's inputs
input_.append('I am so excited for this weekend!')
input_.append('Icant wait')
control_y.append(input_.pop())
input_.append("I can't wait to go")
input_.append("to the lake!")
input_.append("I haven't been there in years.")
input_.append("I used to go there")
control_y.append(input_.pop())
control_y.append(input_.pop())
input_.append("I haven't been there in over a decade.")
control_y.clear()
input_.append('My favorite thing to do at the lake is ')
input_.append('Going')
input_.append('out on my families boat.')
input_.append('I hope the water will be good for boating.')
control_y.append(input_.pop())
control_y.append(input_.pop())
input_.append("out on my family's boat")
control_y.clear()
control_y.append(input_.pop())
control_y.append(input_.pop())
control_y.append(input_.pop())
input_.append(control_y.pop())
input_.append('going boating with my family.')
control_y.clear()

#print both stacks to see their values
print(input_)
print(control_y)
