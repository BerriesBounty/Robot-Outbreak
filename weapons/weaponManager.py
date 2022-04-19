from weapons.assaultRifle import AssaultRifle
from weapons.pistol import Pistol
from weapons.sword import Sword


class WeaponManager:
    weaponList = []
    def init(self):
        WeaponManager.weaponList.append(AssaultRifle())
        WeaponManager.weaponList.append(Pistol())
        WeaponManager.weaponList.append(Sword())