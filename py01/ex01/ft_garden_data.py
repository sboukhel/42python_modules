# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/10/25 17:09:45 by sboukhel         #+#    #+#              #
#    Updated: 2026/10/25 18:07:00 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

print("=== Garden Plant Registry ===")
class plant:
    def info_plant(name, height, age):
        print(f"{name}: {height}cm, {age} Days old")

plant.info_plant("Rose", 25, 30)
plant.info_plant("Sunflower", 80, 45)
plant.info_plant("Cactus", 15, 120)
