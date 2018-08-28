# doomsdayAOEDamp
#
# Used by:
# Module: Sensor Dampening Burst Projector
# Structure Module: Standup Sensor Dampening Burst Projector
type = "projected", "active"


def handler(fit, module, context, *args, **kwargs):
    if "projected" not in context:
        return

    fit.ship.boostItemAttr("maxTargetRange", module.getModifiedItemAttr("maxTargetRangeBonus"),
                           stackingPenalties=True, *args, **kwargs)

    fit.ship.boostItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionBonus"),
                           stackingPenalties=True, *args, **kwargs)
