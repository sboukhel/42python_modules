# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_water_reminder.py                              :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 12:32:17 by sboukhel         #+#    #+#              #
#    Updated: 2026/09/07 21:31:14 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    Day = int(input("Days since last watering: "))
    if Day > 2:
        print("water the plants!")
    else:
        print("plante are fine")
