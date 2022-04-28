from upgrades.upgrade import AmmoPack, HealthPack, MaxHealthUp


class UpgradeManager:
    upgradeList = []
    upgradeList.append(AmmoPack())
    upgradeList.append(HealthPack())
    upgradeList.append(MaxHealthUp())
