# -*- coding: utf-8 -*-

from .cache import tax_benefit_system
from openfisca_core.simulations import Simulation

situation = {
    "individus": {
        "demandeur": {
            "echelon_bourse": {
                "2018-12": -1,
                "2018-11": -1,
                "2018-10": -1,
                "2018-09": -1
            },
            "enfant_a_charge": {
                "2018": False
            },
            "enfant_place": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "tns_autres_revenus_type_activite": {
                "2018-12": "bic",
                "2018-11": "bic",
                "2018-10": "bic",
                "2018-09": "bic"
            },
            "tns_micro_entreprise_type_activite": {
                "2018-12": "bic",
                "2018-11": "bic",
                "2018-10": "bic",
                "2018-09": "bic"
            },
            "tns_auto_entrepreneur_type_activite": {
                "2018-12": "bic",
                "2018-11": "bic",
                "2018-10": "bic",
                "2018-09": "bic"
            },
            "date_naissance": {
                "2018-12": "1952-01-05",
                "2018-11": "1952-01-05",
                "2018-10": "1952-01-05",
                "2018-09": "1952-01-05"
            },
            "statut_marital": {
                "2018-12": "celibataire",
                "2018-11": "celibataire",
                "2018-10": "celibataire",
                "2018-09": "celibataire"
            },
            "gir": {
                "2018-12": "gir_6",
                "2018-11": "gir_6",
                "2018-10": "gir_6",
                "2018-09": "gir_6"
            },
            "age": {
                "2018-12": 66,
                "2018-11": 66,
                "2018-10": 66,
                "2018-09": 66
            },
            "age_en_mois": {
                "2018-12": 803,
                "2018-11": 803,
                "2018-10": 803,
                "2018-09": 803
            },
            "date_arret_de_travail": {
                "2018-12": "2018-12-07",
                "2018-11": "2018-12-07",
                "2018-10": "2018-12-07",
                "2018-09": "2018-12-07"
            },
            "handicap": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "taux_incapacite": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "inapte_travail": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "salaire_de_base": {
                "2017-12": 76923.07692307692,
                "2018-01": 76923.07692307692,
                "2018-02": 76923.07692307692,
                "2018-03": 76923.07692307692,
                "2018-04": 76923.07692307692,
                "2018-05": 76923.07692307692,
                "2018-06": 76923.07692307692,
                "2018-07": 76923.07692307692,
                "2018-08": 76923.07692307692,
                "2018-09": 76923.07692307692,
                "2018-10": 76923.07692307692,
                "2018-11": 76923.07692307692,
                "2018-12": 76923.07692307692,
                "2016-01": 76923.07692307691,
                "2016-02": 76923.07692307691,
                "2016-03": 76923.07692307691,
                "2016-04": 76923.07692307691,
                "2016-05": 76923.07692307691,
                "2016-06": 76923.07692307691,
                "2016-07": 76923.07692307691,
                "2016-08": 76923.07692307691,
                "2016-09": 76923.07692307691,
                "2016-10": 76923.07692307691,
                "2016-11": 76923.07692307691,
                "2016-12": 76923.07692307691
            },
            "salaire_imposable": {
                "2017-12": 62191.730769230766,
                "2018-01": 62191.730769230766,
                "2018-02": 62191.730769230766,
                "2018-03": 62191.730769230766,
                "2018-04": 62191.730769230766,
                "2018-05": 62191.730769230766,
                "2018-06": 62191.730769230766,
                "2018-07": 62191.730769230766,
                "2018-08": 62191.730769230766,
                "2018-09": 62191.730769230766,
                "2018-10": 62191.730769230766,
                "2018-11": 62191.730769230766,
                "2018-12": 62191.730769230766,
                "2016-01": 62191.73076923076,
                "2016-02": 62191.73076923076,
                "2016-03": 62191.73076923076,
                "2016-04": 62191.73076923076,
                "2016-05": 62191.73076923076,
                "2016-06": 62191.73076923076,
                "2016-07": 62191.73076923076,
                "2016-08": 62191.73076923076,
                "2016-09": 62191.73076923076,
                "2016-10": 62191.73076923076,
                "2016-11": 62191.73076923076,
                "2016-12": 62191.73076923076
            },
            "salaire_net": {
                "2017-12": 60000,
                "2018-01": 60000,
                "2018-02": 60000,
                "2018-03": 60000,
                "2018-04": 60000,
                "2018-05": 60000,
                "2018-06": 60000,
                "2018-07": 60000,
                "2018-08": 60000,
                "2018-09": 60000,
                "2018-10": 60000,
                "2018-11": 60000,
                "2018-12": 60000,
                "2016-01": 60000,
                "2016-02": 60000,
                "2016-03": 60000,
                "2016-04": 60000,
                "2016-05": 60000,
                "2016-06": 60000,
                "2016-07": 60000,
                "2016-08": 60000,
                "2016-09": 60000,
                "2016-10": 60000,
                "2016-11": 60000,
                "2016-12": 60000
            }
        }
    },
    "familles": {
        "_": {
            "proprietaire_proche_famille": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "parents": [
                "demandeur"
            ],
            "enfants": [],
            "bourse_lycee": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "bourse_college": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "ppa": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "aide_logement": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "rsa": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "paje_base": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "asf": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "cf": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "af": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "acs": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
            "aspa": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            },
        }
    },
    "foyers_fiscaux": {
        "_": {
            "declarants": [
                "demandeur"
            ],
            "personnes_a_charge": []
        }
    },
    "menages": {
        "_": {
            "loyer": {
                "2018-12": 400,
                "2018-11": 400,
                "2018-10": 400,
                "2018-09": 400
            },
            "coloc": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "logement_chambre": {
                "2018-12": False,
                "2018-11": False,
                "2018-10": False,
                "2018-09": False
            },
            "depcom": {
                "2018-12": "35238",
                "2018-11": "35238",
                "2018-10": "35238",
                "2018-09": "35238"
            },
            "statut_occupation_logement": {
                "2018-12": "locataire_vide",
                "2018-11": "locataire_vide",
                "2018-10": "locataire_vide",
                "2018-09": "locataire_vide"
            },
            "personne_de_reference": [
                "demandeur"
            ],
            "enfants": [],
            "cheque_energie": {
                "2018-11": 0,
                "2018-10": 0,
                "2018-09": 0,
                "2018-08": 0,
                "2018-07": 0,
                "2018-06": 0,
                "2018-05": 0,
                "2018-04": 0,
                "2018-03": 0,
                "2018-02": 0,
                "2018-01": 0,
                "2017-12": 0
            }
        }
    }
}

def test_cycle():
    simulation_actuelle = Simulation(
        tax_benefit_system=tax_benefit_system,
        simulation_json=situation,
        trace=True)

    result = simulation_actuelle.calculate('logement_social_eligible', '2018-12')
    rfr = simulation_actuelle.calculate('rfr', '2016')
    print(result)
    print(rfr)
    assert (result == 1).all()