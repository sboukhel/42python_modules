# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_count_harvest_recursive.py                     :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/09/05 16:17:15 by sboukhel         #+#    #+#              #
#    Updated: 2026/09/07 21:47:30 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

Day = int(input("Days until harvest: "))
x = 1
def ft_count_harvest_recursive(Day, x):
    if x <=Day:
        print("Day ", x)
        x += 1
        return ft_count_harvest_recursive(Day, x)
    else:
        print("Harvest complete!")
