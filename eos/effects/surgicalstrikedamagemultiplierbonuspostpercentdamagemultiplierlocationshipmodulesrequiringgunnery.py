# surgicalStrikeDamageMultiplierBonusPostPercentDamageMultiplierLocationShipModulesRequiringGunnery
#
# Used by:
# Implants named like: Agency 'Pyrolancea' DB Dose (4 of 4)
# Implants named like: Eifyr and Co. 'Gunslinger' Surgical Strike SS (6 of 6)
# Implant: Standard Cerebral Accelerator
type = "passive"


def handler(fit, implant, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Gunnery"),
                                  "damageMultiplier", implant.getModifiedItemAttr("damageMultiplierBonus"))
