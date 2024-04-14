from pers_base import * #all classes
warrior = Warrior('Eivor', 32, 200, 80)
warrior.descr()
guy = People('Killian', 35, 195, 94)
guy.descr()

import pers_base #pers_base. show what is import pers_base
warrior = pers_base.Warrior('Eivor', 32, 200, 80)
warrior.descr()
guy = pers_base.People('Killian', 35, 195, 94)
guy.descr()