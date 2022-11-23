import kivy
from kivy.app import App
from kivy.uix.video import Video
from kivy.core.window import Window 

Window.size = (380,610)
class myapp(App):
    def build(self):
        self.title = 'video player'
        video = Video(source='vid.mp4')
        video.state = 'play'
        video.options = {'eos':'loop'}
        video.allow_stretch =True
        return video

if __name__ =='__main__':
    myapp().run()