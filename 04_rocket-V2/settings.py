class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.arrowkey_upx = 1080
        self.arrowkey_upy = 680
        self.arrowkey_downx = 1080
        self.arrowkey_downy = 738
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1.5        

        #Bullet settings
        self.bullet_speed = 1.3
        self.bullet_width = 6
        self.bullet_height = 6
        self.bullet_color = (199,21,133)
        self.bullets_allowed = 5