from game_controller import GameController

width = 200
height = 300
game_controller = GameController(width, height)


def setup():
    size(width, height)


def mousePressed():
    game_controller.prepare_to_drop()


def mouseDragged():
    game_controller.handle_dragged()


def mouseReleased():
    game_controller.start_drop()


def draw():
    game_controller.update()
