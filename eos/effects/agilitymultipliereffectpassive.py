# Used by:
# Modules named like: Engine Housing (8 of 8)
type = "passive"
def handler(fit, module, context):
    fit.ship.boostItemAttr("agility", module.getModifiedItemAttr("agilityMultiplier"), stackingPenalties = True)
