import random
def randomcolor(rgb):
    color=random.choice (rgb),random.choice (rgb),random.choice (rgb),random.choice (rgb),random.choice (rgb),random.choice (rgb)
    color=str(color)
    color=color.replace(",","")
    color=color.replace(" ","")
    color=color.replace("(","")
    color=color.replace("'","")
    color=color.replace(")","")
    return color
