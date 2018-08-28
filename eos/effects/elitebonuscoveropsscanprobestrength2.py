# eliteBonusCoverOpsScanProbeStrength2
#
# Used by:
# Ships from group: Covert Ops (8 of 8)
type = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Scanner Probe",
                                    "baseSensorStrength", ship.getModifiedItemAttr("eliteBonusCovertOps2"),
                                    skill="Covert Ops")
