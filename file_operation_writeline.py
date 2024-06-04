# f = open('myfile', 'w')
# lines = ['line1\n', 'line2\n', 'line3\n']
# f.writelines(lines)
# f.close()

'''you can do this instead '''

f = open('myfile', 'w')
lines = ['line1', 'line2', 'line3']
for line in lines:
    f.write(line + '\n')
f.close()
