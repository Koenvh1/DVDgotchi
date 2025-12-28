import os
import shutil

for food_level in range(1, 4):
    for happiness_level in range(1, 4):
        for animation in os.listdir(f"animations\\{food_level}\\{happiness_level}"):
            print(food_level, happiness_level, animation)
            shutil.copy2(f"animations\\{food_level}\\{happiness_level}\\{animation}\\out.mpg",
                         f"videos\\{animation}_f{food_level}_h{happiness_level}.mpg")