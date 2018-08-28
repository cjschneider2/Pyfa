# warpScrambleBlockMWDWithNPCEffect
#
# Used by:
# Modules named like: Warp Scrambler (27 of 27)
from eos.saveddata.module import State

runTime = "early"
type = "projected", "active"


def handler(fit, module, context):
    if "projected" not in context:
        return

    fit.ship.increaseItemAttr("warpScrambleStatus", module.getModifiedItemAttr("warpScrambleStrength"))

    # this is such a dirty hack
    for mod in fit.modules:
        if not mod.isEmpty and mod.state > State.ONLINE and (
                mod.item.requiresSkill("Micro Jump Drive Operation") or
                mod.item.requiresSkill("High Speed Maneuvering")
        ):
            mod.state = State.ONLINE
        if not mod.isEmpty and mod.item.requiresSkill("Micro Jump Drive Operation") and mod.state > State.ONLINE:
            mod.state = State.ONLINE
