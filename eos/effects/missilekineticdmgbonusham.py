# Used by:
# Implants named like: Zainou Heavy AM (6 of 6)
type = "passive"
def handler(fit, container, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Heavy Assault Missiles"),
                                    "kineticDamage", container.getModifiedItemAttr("damageMultiplierBonus"))
