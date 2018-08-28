# shipBonusNeutCapNeedRoleBonus2
#
# Used by:
# Ship: Damavik
# Ship: Hydra
# Ship: Leshak
# Ship: Tiamat
# Ship: Vedmak
type = "passive"


def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Energy Neutralizer", "capacitorNeed",
                                  src.getModifiedItemAttr("shipBonusRole2"))
