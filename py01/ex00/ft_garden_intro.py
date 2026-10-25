# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#    ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#    By: sboukhel <sboukhel@student.1337.ma>       +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#    Created: 2026/10/25 16:31:03 by sboukhel         #+#    #+#              #
#    Updated: 2026/10/25 17:03:05 by sboukhel        ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_garden_intro(name, height, age):
    print("=== Welcome to My Garden ===")
    print("Plant: " + name)
    print("Height: " + height)
    print("Age: " + age + "\n")

    print("=== End of Program ===")

if (__name__=="__main__"):
    ft_garden_intro("Rose", "25cm", "30 Days")
