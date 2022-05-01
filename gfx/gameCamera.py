class GameCamera:
    def __init__(self, game, xOffset, yOffset):
        self.game = game
        self.xOffset = xOffset
        self.yOffset = yOffset

    def centerOnPlayer(self, player):
        # x is + if on the right of center
        # y is + if on the bottom of center
        self.xOffset = player.rect.x + player.rect.width / 2 - self.game.width / 2
        self.yOffset = player.rect.y + player.rect.height / 2 - self.game.height / 2
