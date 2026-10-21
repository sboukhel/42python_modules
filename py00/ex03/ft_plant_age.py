# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_plant_age.py                                   :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 11:18:47 by sboukhel         #+#    #+#              #
#    Updated: 2026/09/07 21:31:49 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    age = int(input("enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
