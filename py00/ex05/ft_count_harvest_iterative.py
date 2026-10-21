# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_iterative.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 13:44:41 by sboukhel         #+#    #+#              #
#    Updated: 2026/09/07 21:37:46 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    Day = int(input("Days untilharvest: "))
    x = 1
    while x in range(Day + 1):
        print("Day", x)
        x += 1
    print("harvest time!")
