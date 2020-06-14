import sys
import mainwindowhorizontallayout
#出现红线的原因是程序没有把改文件当作库，右键点击horizontal文件夹，点击make directory as，再点击source root即可

from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #创建的该对象代表整个应用程序，需要传入参数
    mainwindow = QMainWindow()
    #创建一个主窗口对象
    ui = mainwindowhorizontallayout.Ui_MainWindow()
    #创建该类的实例
    ui.setupUi(mainwindow)
    #调用类中的setupUi方法，创建窗口中所有的组件
    mainwindow.show()
    #显示窗口
    sys.exit(app.exec_())
    #执行，主循环，让窗口一直存在