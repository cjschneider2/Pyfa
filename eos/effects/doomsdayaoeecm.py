# doomsdayAOEECM
#
# Used by:
# Module: ECM Jammer Burst Projector
# Structure Module: Standup ECM Jammer Burst Projector
from eos.modifiedAttributeDict import ModifiedAttributeDict

type = "projected", "active"


def handler(fit, module, context, **kwargs):
    if "projected" in context:
        # jam formula: 1 - (1- (jammer str/ship str))^(# of jam mods with same str))
        strModifier = 1 - module.getModifiedItemAttr("scan{0}StrengthBonus".format(fit.scanType)) / fit.scanStrength

        if 'effect' in kwargs:
            strModifier *= ModifiedAttributeDict.getResistance(fit, kwargs['effect'])

        fit.ecmProjectedStr *= strModifier
