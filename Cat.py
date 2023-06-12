class Cat:
    def __init__(self, pos_x, pos_y, clone_number):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = 44
        self.height = 47
        self.clone_number = clone_number

    def collision_check(self, mouse_pos):
        if self.pos_x <= mouse_pos[0] <= self.pos_x + self.width and mouse_pos[1] >= self.pos_y and mouse_pos[1] <= self.pos_y + self.height:
            return True
        else:
            return False

    def cat_identity_check(self, number):
        if number == self.clone_number:
            return True
        else:
            return False
