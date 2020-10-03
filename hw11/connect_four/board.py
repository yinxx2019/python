class Board:

    def __init__(self, width, height, row_height, column_width):
        self.width = width
        self.height = height
        self.line_width = 15
        self.row_height = row_height
        self.column_width = column_width

    def draw_line(self):
        # to draw horizontal lines
        for row_count in range(0, self.height // self.row_height):
            stroke(0, 0, 255)
            strokeWeight(self.line_width)
            line(0, self.height - self.row_height * row_count,
                 self.width, self.height - self.row_height * row_count)
        # to draw vertical lines
        for column_count in range(0, self.width // self.column_width + 1):
            stroke(0, 0, 255)
            strokeWeight(self.line_width)
            line(self.column_width * column_count, self.row_height,
                 self.column_width * column_count, self.height)

    def message(self):
        fill(0)
        textSize(20)
        text("GAME OVER", 43, 50)
