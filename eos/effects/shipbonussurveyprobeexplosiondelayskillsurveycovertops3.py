# shipBonusSurveyProbeExplosionDelaySkillSurveyCovertOps3
#
# Used by:
# Ships from group: Covert Ops (5 of 8)
type = "passive"


def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.group.name == "Survey Probe",
                                    "explosionDelay", ship.getModifiedItemAttr("eliteBonusCovertOps3"),
                                    skill="Covert Ops")
