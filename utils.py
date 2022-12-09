import settings as s


def height_percentage(percentage):
    return (s.HEIGHT / 100) * percentage


# print(height_percentage(25))
def width_percentage(percentage):
    return (s.WIDTH / 100) * percentage
