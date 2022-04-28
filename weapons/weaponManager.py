from weapons.assaultRifle import AssaultRifle
from weapons.coolSword import CoolSword
from weapons.lazerBeam import PiercingGun
from weapons.pistol import Pistol
from weapons.sword import Sword


class WeaponManager:
    weaponList = []
    def init():
        WeaponManager.weaponList.append(AssaultRifle())
        WeaponManager.weaponList.append(Pistol())
        WeaponManager.weaponList.append(Sword())
        WeaponManager.weaponList.append(CoolSword())
        WeaponManager.weaponList.append(PiercingGun())