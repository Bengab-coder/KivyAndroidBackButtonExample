from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder

Window.size = (300,500) # Set the window


class TestAndroidBackButtonApp(App):
    def build(self): 
        return Builder.load_file('design.kv') #Load our kv file

    def on_start(self):
        self.screens_list = [] # This list will hold all the screens we have visited
        Window.bind(on_keyboard=self.keyboard_key_pressed)

    def keyboard_key_pressed(self,window_object,keycode,*args):
        if keycode == 27: # Here we listen for the 'esc' keyboard key which corresponds to the back button on android.
            if len(self.screens_list)>0: # We check if we have visited any new screen else we exit the app by returning False otherwise we move to the previous screen which is the last item or the item returned by pop() method which also removes the screen from the list.
                most_recent_screen = self.screens_list.pop().name
                self.root.current = most_recent_screen
                return True # this will stop the program from being closed when we press the button as opposed to its normal behaviour

            else:
                return False
            
    def screen_changed(self,screen): # This function is called from the kv file each time we visit a ew screen , see the kv file to better understand how it has been structured.
        print("Changed to ",screen.name)
        if screen not in self.screens_list:
            self.screens_list.append(screen)
            print("Visited Screens = ",self.screens_list)

TestAndroidBackButtonApp().run() # Finally we instantiate the main app and run it