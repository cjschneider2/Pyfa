# Used by:
# Celestials named like: Red (6 of 6)
runTime = "early"
type = ("projected", "offline")
def handler(fit, module, context):
    fit.modules.filteredItemMultiply(lambda mod: "overloadRangeBonus" in mod.itemModifiedAttributes,
                                     "overloadRangeBonus", module.getModifiedItemAttr("overloadBonusMultiplier"))
