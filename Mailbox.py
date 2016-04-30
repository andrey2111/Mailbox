inputfilename = 'unix.mailbox'
openedfiles = dict() #словарь открытых файлов {email: объект файла с этим email}

inf = open(inputfilename, 'r')
openedfiles.update({inputfilename: inf}) #открытие входного файла на чтение и добавление его в словарь

for line in inf:
    if len(line.split()) and line.split()[0] == 'From': #Если строка начинается с From
        email = line.split()[1] #email отправителя
        if openedfiles.get(email) is None: #если файл с именем email не открыт, его необходимо открыть
            ouf = open(email, 'w')
            openedfiles.update({email: ouf})

    openedfiles.get(email).write(line) #запись строки в соответствующий файл

for file in openedfiles.values():
    file.close() #закрытие всех открытых файлов
