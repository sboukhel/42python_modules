# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_harvest_total.py                               :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 10:20:42 by sboukhel         #+#    #+#              #
#    Updated: 2026/09/07 21:21:30 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_harvest_total():
    Day1 = int(input("Day 1 harvest: "))
    Day2 = int(input("Day 2 harvest: "))
    Day3 = int(input("Day 3 harvest: "))
    print("total harvest: " , (Day1 + Day2 + Day3))
