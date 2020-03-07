# ！ python3.8.1

# os模块的用法
import os

os.getcwd()
os.chdir('c:\\Users')
os.getcwd()
os.makedirs('d:\\users\\python\\python.py\\python.docx\\1.txt')  # 只能创建文件夹，“1.txt"也是以文件夹的形式出现
os.path.abspath('..')
os.path.relpath('d:\\SNIS-730.HD.mp4', 'd:\\迅雷下载')
os.path.isabs('.\\KSSS.py')
os.path.basename('d:\\迅雷下载\\SNIS-730.HD.mp4')
os.path.split('d:\\迅雷下载\\SNIS-730.mp4')
os.path.getsize('d:\\迅雷下载\\SNIS-730.mp4')
os.listdir('d:\\迅雷下载')
os.path.exists('d:\\迅雷下载')
os.path.isdir('d:\\迅雷下载')
os.path.isfile('d:\\迅雷下载\\ABP-583-C.mp4')
# 读取内容
av = open('d:\\迅雷下载\\ABP-583-C.mp4')
avcontent = av.read()
# 写入内容
baconFile = open('c:\\Users\\MI\\bacon.txt', 'w')
baconFile.write('i want to eat bacon!')
baconFile.close()
# 用SHELVE模块保存变量
import shelve
shelfFile = shelve.open('c:\\Users\\MI\\mydata')
cats = ['Zophia', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
# 读取shelve创建的数据内容
shelfFile = shelve.open('c:\\Users\\MI\\mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()
# 就像字典一样，shelf的值有keys()和values()方法，返回的shelf中键和值的类似列表值
shelfFile = shelve.open('c:\\Users\\MI\\mydata')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()
# 用pprint.pformat()函数来保存变量
import pprint
cats = [{'name':'Zophia','desc':'chubby'},{'name':'Pooka','desc':'fluffy'}]
pprint.pformat(cats)
fileobj = open('c:\\Users\\MI\\myCats.py','w')
fileobj.write('cats = ' + pprint.pformat(cats) + '\n')
fileobj.close()
import myCats
myCats.cats
myCats.cats[0]
myCats.cats[0]['name']

#pprint.pformat:格式化一个数据结构而不把它直接写至一个流（例如用于日志记录），可以使用pformat()来构造一个字符串表示。
import logging
from pprint import pformat

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-8s %(message)s',
                    )
logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())

#DEBUG  Logging pformatted data
#DEBUG  [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
#DEBUG   (2,
#DEBUG   {'e': 'E',
#DEBUG    'f': 'F',
#DEBUG    'g': 'G',
#DEBUG    'h': 'H',
#DEBUG    'i': 'I',
#DEBUG    'j': 'J',
#DEBUG    'k': 'K',
#DEBUG    'l': 'L'})]

#项目1
import random
#The quiz data.Keys are states and values are their capitals.
capitals = {
               'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona':'Phoenix', 'Arkansas': 'Little ROCK',
               ' California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware':'Dover',
               'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii':'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
               'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':'Topeka', 'Kentucky': 'Frankfort',
               'Louisiana':'Baton Rouge', 'Maine':' Augusta','Maryland':'Annapolis', 'Massachusetts':'Boston',
               'Michigan':'Lansing','Minnesota':'Saint Paul','Mississippi': 'Jackson','Missouri':'Jefferson City',
               'Montana': 'Helena','Nebraska':'Lincoln','Nevada':'Carson city','New Hampshire':'Concord',
               'New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany', 'North Carolina':'Raleigh',
               'North Dakota':'Bismarck','Ohio':'Columbus','klahoma':'Oklahoma City','oregon': 'Salem',
               'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence','South Carolina':'Columbia','South Dakota':'Pierre',
               'Tennessee':'Nashville','Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':'Montpelier','Virginia':'Richmond',
              'Washington':'Olympia','West Virginia':'Charleston','Wisconsin':'Madison','Wyoming': 'Cheyenne'}
# Generate 35 quiz files.
for quizNum in range(35):
    # creat quiz and keys docx
    quizFile = open('c:\\Users\\MI\\capiticalsquiz%s.txt' % (quizNum + 1),'w')
    answerkeyFile = open('c:\\Users\\MI\\capiticalsquiz_answers%s.txt' % (quizNum + 1),'w')

    # write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states, making a question for each
    for questionNum in range(50):

        #Get right and wrong answers
        correctAnswers = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswers]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file
        quizFile.write('%s What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i],answerOptions[i]))
        quizFile.write('\n')

        #Write the answer key to a file.
        answerkeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswers)]))
    quizFile.close()
    answerkeyFile.close()

# 项目2：多重剪贴板
import shelve,pyperclip,sys
mcbShelve = shelve.open('mcb')

#Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelve[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    #list keywords amd load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelve.keys())))
    elif sys.argv[1] in mcbShelve:
        pyperclip.copy(mcbShelve[sys.argv[1]])

mcbShelve.close()