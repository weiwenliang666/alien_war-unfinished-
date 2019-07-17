class GameStats():
    """跟踪记录游戏的统计信息"""

    def  __init__(self,ai_sett):
        """初始化统计信息"""
        self.ai_sett = ai_sett
        self.reset_stats()
        #游戏刚启动时处于活动状态
        self.game_active = False
        #任何情况下不应重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化游戏"""
        self.ships_left = self.ai_sett.ship_limit
        self.score = 0
