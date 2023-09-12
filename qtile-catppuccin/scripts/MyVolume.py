from libqtile import widget

class MyVolume(widget.Volume):
    def _configure(self, qtile, bar):
        widget.Volume._configure(self, qtile, bar)
        self.volume = self.get_volume()
        if self.volume <= 0:
            self.text = '婢 '
        elif self.volume <= 33:
            self.text = ' '
        elif self.volume < 66:
            self.text = '墳 '
        else:
            self.text = ' '
 
    def _update_drawer(self, wob=False):
        if self.volume <= 0:
            self.text = '婢 '
        elif self.volume <= 33:
            self.text = ' '
        elif self.volume < 66:
            self.text = '墳 '
        else:
            self.text = ' '
        self.draw()
 
        if wob:
            with open(self.wob, 'a') as f:
                 f.write(str(self.volume) + "\n")
