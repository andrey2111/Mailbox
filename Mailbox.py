inputfilename = 'unix.mailbox'
openedfiles = dict() #словарь открытых файлов {email: объект файла с этим email}

inf = open(inputfilename, 'r')
openedfiles[inputfilename] = inf #открытие входного файла на чтение и добавление его в словарь

for line in inf:
    if len(line.split()) and line.split()[0] == 'From': #Если строка начинается с From
        email = line.split()[1] #email отправителя
        if email not in openedfiles:#если файл с именем email не открыт, его необходимо открыть
            ouf = open(email, 'w')
            openedfiles[email] = ouf

    openedfiles.get(email).write(line) #запись строки в соответствующий файл

for file in openedfiles.values():
    file.close() #закрытие всех открытых файлов
