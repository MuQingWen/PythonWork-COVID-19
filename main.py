from china_ui import *
from country_ui import *
from main_ui import *
import sys
#render_dayly_chart('05-01-2020','05-01-2021','India')
#print(list(flat_country_data('01-01-2021','China')))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())