#12. б) Дан текстовий файл f. Отримати файл g, утворений з файлу f заміною всіх його
#прописних (великих) букв такими ж рядковими (малими) літерами.

#Відкриваємо спочатку файли для письма (введення даних).
f=open('text1.txt', 'w')
f.write(input('Введіть слово/речення: '))
f.close()
g=open('text2.txt', 'w')

#Ще раз відкриємо, але вже для читання написаного:
with open('text1.txt', 'r') as f: 
    lines=f.readlines()
    for i in lines:
        i=i.lower() #Перетворимо усі ВЕЛИКІ літери на малі.
        g.write(i) #Запишемо їх у файл g.

#Відкриємо файл g для прочитання.
g=open('text2.txt', 'r')
fd=g.read()
print('Елементи файлу g: ', fd) #Виведемо на екран.
