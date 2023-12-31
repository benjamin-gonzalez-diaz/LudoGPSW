normal_cells = {
    (1,6): "right", #red
    (2,6): "right",
    (3,6): "right",
    (4,6): "right",
    (5,6): "up-right",
    (6,5): "up",
    (6,4): "up",
    (6,3): "up",
    (6,2): "up",
    (6,1): "up",
    (6,0): "right",
    (7,0): "right",
    (8,0): "down",
    (8,1): "down",
    (8,2): "down",
    (8,3): "down",
    (8,4): "down",
    (8,5): "down-right",
    (9,6): "right",
    (10,6): "right",
    (11,6): "right",
    (12,6): "right",
    (13,6): "right",
    (14,6): "down",
    (14,7): "down",
    (14,8): "left",
    (13,8): "left",
    (12,8): "left",
    (11,8): "left",
    (10,8): "left",
    (9,8): "down-left",
    (8,9): "down",
    (8,10): "down",
    (8,11): "down",
    (8,12): "down",
    (8,13): "down",
    (8,14): "left",
    (7,14): "left",
    (6,14): "up",
    (6,13): "up",
    (6,12): "up",
    (6,11): "up",
    (6,10): "up",
    (6,9): "up-left",
    (5,8): "left",
    (4,8): "left",
    (3,8): "left",
    (2,8): "left",
    (1,8): "left",
    (0,8): "up",
    (0,7): "up",
    (0,6): "right",
    (1,6): "right",   
}

special_cells = {
    "red": {
        (0,7): "right",
        (1,7): "right",
        (2,7): "right",
        (3,7): "right",
        (4,7): "right",
        (5,7): "right",
    },
    "green": {
        (7,0): "down", #green
        (7,1): "down",
        (7,2): "down",
        (7,3): "down",
        (7,4): "down",
        (7,5): "down",
    },
    "yellow": {
        (14,7): "left",
        (13,7): "left",
        (12,7): "left",
        (11,7): "left",
        (10,7): "left",
        (9,7): "left",
    },
    "blue": {
        (7,14): "up",
        (7,13): "up",
        (7,12): "up",
        (7,11): "up",
        (7,10): "up",
        (7,9): "up",
    }
}

start_cells = {
    "red": (1,6),
    "green": (8,1),
    "yellow": (13,8),
    "blue": (6,13)
}

end_cells = {
    "red": (6,7),
    "green": (7,6),
    "yellow": (8,7),
    "blue": (7,8)
}