class Settings :
    def __init__(self):
        self.screen_width=500
        self.screen_height=500
        self.fps=60
        self.dt_max=3/self.fps #lưu số khung hình mỗi giây
        self.player_speed=2