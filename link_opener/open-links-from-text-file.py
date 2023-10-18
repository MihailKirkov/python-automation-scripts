import webbrowser

file_name = 'jobs_to_apply.txt'

with open(file_name, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            #print(f'Link : {line}', end='')
            webbrowser.open(line)