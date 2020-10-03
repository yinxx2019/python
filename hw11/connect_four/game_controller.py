from board import Board
from disk import Disk


class GameController:

    def __init__(self, x, y):
        self.width = x
        self.height = y
        self.row_height = 100
        self.column_width = 100
        self.COL_COUNT = 2

        self.board = Board(self.width, self.height, self.row_height,
                           self.column_width)
        self.human_player_turn = True
        self.disks = []
        self.new_disk = None
        self.list_0 = []
        self.list_1 = []
        self.array = [self.list_0, self.list_1]
        self.red = color(255, 0, 0)
        self.yellow = color(255, 255, 0)
        self.s = second()
        self.delay = 2

    def update(self):
        background(180)
        self.board.draw_line()
        # show game over message
        if (len(self.disks) == 4 and second() > self.s + self.delay and
           self.disks[-1].active is False):
            self.board.message()
        for disk in self.disks:
            disk.display()
            self.board.draw_line()
            if not disk.active:
                continue
            # to check which column the disk is in
            column_number = disk.x // self.column_width
            # to check the current length of each sub-list
            # aiming to set the disk position to be that length.
            # if the length is 0, we want the disk to fall to the position
            # of index 0 of the sub-list (the bottom)
            # then the position if confirmed and won't change again.
            disk.position = len(self.array[column_number])
            if (disk.y < self.height - disk.radius -
               self.row_height * disk.position):
                disk.y += disk.rate
                disk.rate += 1
            else:
                disk.active = False
                disk.y = (self.height - disk.radius -
                          self.row_height * disk.position)
                self.array[column_number].append(disk)

    def prepare_to_drop(self):
        # to restrict to only generate a disk
        # when user click on the first row of the board
        # and adjust the disk's position to be in the middle of a column.
        mouseX_revised = ((mouseX // self.column_width) * self.column_width
                          + self.column_width / 2)
        mouseY_revised = self.row_height / 2
        self.create_new_disk(mouseX_revised, mouseY_revised, mouseY)

    def handle_dragged(self):
        mouseX_revised = ((mouseX // self.column_width) * self.column_width
                          + self.column_width / 2)
        # the below for lines deal with the exception when mouseX
        # is out of width's range. (width - 1)'s purpose is to make
        # ((width - 1) // column_width) to be zero.
        if mouseX_revised >= self.width:
            mouseX_revised = (((self.width - 1) // self.column_width)
                              * self.column_width + self.column_width / 2)
        elif mouseX_revised < 0:
            mouseX_revised = self.column_width / 2
        mouseY_revised = self.row_height / 2
        # when the mouse is dragged, create a new disk.
        if not self.new_disk:
            self.create_new_disk(mouseX_revised, mouseY_revised, mouseY)
        # if mouseY falls into the grid, remove the disk just created.
        # and reset new_all to be None.
        elif mouseY > self.row_height:
            self.disks.remove(self.new_disk)
            self.new_disk = None
        # if the list hasn't been filled in full, and new_disk,
        # and mouseY <= row_height, then display the disk
        elif (len(self.array[mouseX_revised // self.column_width])
              < self.COL_COUNT):
            self.new_disk.hide = False
            self.new_disk.x = mouseX_revised
            self.new_disk.y = mouseY_revised
        # the below else means:
        # new_disk and mouseY <= row_height and
        # len(array[mouseX_revised // column_width]) >= COL_COUNT
        # still create the disk, but just hide it from displaying.
        else:
            self.new_disk.hide = True

    def start_drop(self):
        if not self.new_disk:
            return
        self.new_disk.active = True
        self.new_disk.hide = False
        self.new_disk = None
        self.human_player_turn = not self.human_player_turn

    def create_new_disk(self, mouseX_revised, mouseY_revised, mouseY):
        if (len(self.disks) == 0 or not self.disks[-1].active) and \
                0 <= mouseY <= self.row_height and 0 <= mouseX <= self.width \
                and (len(self.array[mouseX_revised // self.column_width])
                     < self.COL_COUNT):
            color = self.red
            if not self.human_player_turn:
                color = self.yellow
            self.new_disk = Disk(mouseX_revised, mouseY_revised, color)
            self.disks.append(self.new_disk)
