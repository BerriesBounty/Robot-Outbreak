from ultimates.ult_invisible import Invisible
from ultimates.ult_rage import Rage
from ultimates.ult_shockwave import Shockwave


class UltManager:
    ultimateList = []
    ultimateList.append(Invisible(5, 100, 0))
    ultimateList.append(Rage(5, 100, 1))
    ultimateList.append(Shockwave(2, 50, 2))