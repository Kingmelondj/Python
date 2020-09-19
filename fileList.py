import sqlite3

conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileList ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fAnime TEXT \
        )")
    conn.commit()
conn.close()




conn = sqlite3.connect('fileList.db')
list1 = ['information.docx', 'Hello.txt', 'myImage.png', \
        'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']
for file in list1:
    if file.endswith('txt'):
        print(file)
        
