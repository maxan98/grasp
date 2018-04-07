import npyscreen
import time
class Tui(npyscreen.StandardApp):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.addForm("MAIN", MainForm, name="Choose options")

class MainForm(npyscreen.ActionForm):
    # Конструктор

    def create(self):
        y, x = self.useable_space()
        
        self.date = self.add(npyscreen.TitleDateCombo, name="Date:", max_width=x // 2,allowTodaysDate=True,allowClear=False)
        self.title = self.add(npyscreen.TitleText, name="Номер группы", value="5512",relx=50,rely = 2)
        
    # переопределенный метод, срабатывающий при нажатии на кнопку «ok»
    def on_ok(self):
        raise Exception(str(self.date.value),str(self.title.value))

        self.parentApp.setNextForm(None)
        
    # переопределенный метод, срабатывающий при нажатии на кнопку «cancel»
    def on_cancel(self):
        exit()


