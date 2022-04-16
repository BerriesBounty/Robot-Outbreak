class GameCamera:
    def __init__(self, game, xOffset, yOffset):
        self.game = game
        self.xOffset = xOffset
        self.yOffset = yOffset

    def centerOnPlayer(self, player):
        self.xOffset = player.rect.x - self.game.width / 2 + player.rect.width / 2
        self.yOffset = player.rect.y - self.game.height / 2 + player.rect.height / 2
