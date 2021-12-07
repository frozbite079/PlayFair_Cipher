from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

def build():
    app = QApplication(sys.argv)
    win = QWidget()
    
    img = "playf.png"
    img1 = "vector.jpg"
    try:
        def play():
            def find_position(key_matrix,letter):
                x=y=0
                for i in range(5):
                    for j in range(5):
                        if key_matrix[i][j]==letter:
                            x=i
                            y=j

                return x,y
            matrix=[]
            plaintext=edit.text()
            plaintext=plaintext.upper();
            #print(plaintext.upper())

            keyword=edit1.text()
            keyword=keyword.upper()
            #plaintext='GOODMORNINGALL'
            #keyword='MONARCHY';
            alpha='abcdefghijklmnopqrstuvwxyz'
            alpha=alpha.upper()
            #creating martix
            for e in keyword.upper():
                if e not in matrix:
                    matrix.append(e)

            print('KeyWord',matrix)

            for e in alpha:
                if e not in matrix:
                    if e=='J':
                        x='hello'
                    else:
                        matrix.append(e)
                

            keyword_matrix=[]
            for e in range(5):
                keyword_matrix.append('')
                
            keyword_matrix[0]=matrix[0:5]
            keyword_matrix[1]=matrix[5:10]
            keyword_matrix[2]=matrix[10:15]
            keyword_matrix[3]=matrix[15:20]
            keyword_matrix[4]=matrix[20:25]

            
            print('KeyWord Matrix 5*5(KEY)',keyword_matrix)
            mat = "KeyWord Matrix 5*5(KEY):\n"
            fun.appendPlainText(str(str(mat)))
            fun.appendPlainText(str(keyword_matrix)+"\n")     

            message=[]
            for  plain in plaintext:
                message.append(plain)
            for unused in message:
                if unused== '':
                    message.remove('')
            #even length
            print('message(PLAINTEXT)',message)
            mat1 = "message(PLAINTEXT):\n"
            fun.appendPlainText(str(str(mat1)))
            fun.appendPlainText(str(message)+"\n")
            i=0
            l=int(len(message)/2)

            for both in range(l):
                if message[i]== message[i+1]:
                    message.insert(i+1,'X')
                i=i+2
            #odd length
            if len(message)%2==1:
                message.append("X")
            i=0
            new_message=[]
            l=int(len(message)/2)+1
            #l=int(len(message))/2+1)

            for x in range(1,l):
                new_message.append(message[i:i+2])
                i=i+2    
            print(new_message)
            q=0;
            cipher_matrix=[]
            for e in new_message:
                p1,q1=find_position(keyword_matrix,e[0])
                p2,q2=find_position(keyword_matrix,e[1])
                
                if p1==p2:
                        if q1==4:
                                q1=-1
                        if q2==4:
                                q2=-1
                        cipher_matrix.append(keyword_matrix[p1][q1+1])
                        cipher_matrix.append(keyword_matrix[p1][q2+1])
                elif q1==q2:
                        if p1==4:
                                p1=-1;
                        if p2==4:
                                p2=-1;
                        cipher_matrix.append(keyword_matrix[p1+1][q1])
                        cipher_matrix.append(keyword_matrix[p2+1][q2])
                else:
                    cipher_matrix.append(keyword_matrix[p1][q2])
                    cipher_matrix.append(keyword_matrix[p2][q1])
            print(str(cipher_matrix))
            str1=''.join(cipher_matrix)
            i=0
            new_cipher_matrix=[]
            for x in range(int(len(cipher_matrix)/2)):
                    new_cipher_matrix.append(cipher_matrix[i:i+2])
                    i=i+2
            print(new_cipher_matrix)
            omessage=[]
            for e in new_cipher_matrix:
                    p1,q1=find_position(keyword_matrix,e[0])
                    p2,q2=find_position(keyword_matrix,e[1])
                    if p1==p2:
                        if q1==4:
                            q1=-1
                        if q2==4:
                            q2=-1
                        omessage.append(keyword_matrix[p1][q1-1])
                        omessage.append(keyword_matrix[p1][q2-1])		
                    elif q1==q2:
                        if p1==4:
                            p1=-1;
                        if p2==4:
                            p2=-1;
                        omessage.append(keyword_matrix[p1-1][q1])
                        omessage.append(keyword_matrix[p2-1][q2])
                    else:
                        omessage.append(keyword_matrix[p1][q2])
                        omessage.append(keyword_matrix[p2][q1])

            for unused in range(len(omessage)):
                    if "X" in omessage:
                            omessage.remove("X")
            print("oringal Message")
            fun.appendPlainText(str("oringal Message:\n"))
            fun.appendPlainText(str(omessage))
            print(omessage)
    except Exception as e:
        dio = QMessageBox()
        dio.setText(str(e))
        dio.setWindowIcon(QIcon(img))
        dio.show()    
     
    lab = QLabel(win)
    lab.setPixmap(QPixmap(img1))    

    title = QLabel(win)
    title.setText("PlayFair")
    title.setFont(QFont("Century Gothic",50))
    title.move(380,10)
    title.setStyleSheet("border:2px solid white;border-radius:20px;color:white")
    
    
    label = QLabel(win)
    label.setText("PlainText")
    label.setStyleSheet("color:white;font-weight:bold")
    label.setFont(QFont("arial",20))
    label.move(50,150)
    
    
    fun  =QPlainTextEdit(win)
    fun.setFont(QFont("arial",15))
    fun.setReadOnly(True)
    fun.setFixedHeight(300)
    fun.setStyleSheet("border:2px solid grey;border-radius:20px")
    fun.setFixedWidth(500)
    fun.move(450,150)
    
    edit = QLineEdit(win)
    edit.setPlaceholderText("Enter PlainText")
    edit.setFont(QFont("arial",20))
    edit.move(180,150)
    edit.setStyleSheet("border:2px solid grey;border-radius:20px")
    
    label1 = QLabel(win)
    label1.setStyleSheet("color:white;font-weight:bold")
    label1.setText("Key")
    label1.setFont(QFont("arial",20))
    label1.move(50,250)
    
    edit1 = QLineEdit(win)
    edit1.setPlaceholderText("Enter Key")
    edit1.setFont(QFont("arial",20))
    edit1.move(180,250)
    edit1.setStyleSheet("border:2px solid grey;border-radius:20px;")
    
    bu1 = QPushButton(win)
    bu1.setFont(QFont("arial",20))
    bu1.setText("Submit")
    bu1.setStyleSheet("QPushButton::hover"
                      "{"
                         "background-color:#8ce2b6" 
                      "}")
    bu1.setFixedHeight(50)
    bu1.setFixedWidth(200)
    bu1.move(50,420)
    bu1.clicked.connect(play)
    
    win.setFixedHeight(500)
    win.setFixedWidth(1000)
    win.setWindowTitle("PlayFire")
    win.setWindowIcon(QIcon(img))
    
    win.setWindowOpacity(0.89)
    win.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    build()    
    