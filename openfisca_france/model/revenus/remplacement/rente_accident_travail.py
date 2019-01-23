# -*- coding: utf-8 -*-

from openfisca_france.model.base import *


class rente_accident_travail(Variable):
    value_type = float
    entity = Individu
    label = u"Montant mensuel ou tremestriel de la rente d’accident du travail"
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000006073189&idArticle=LEGIARTI000006743072&dateTexte=&categorieLien=cid"
    definition_period = MONTH

    def formula(individu, period):
        rente_accident_travail_salarie = individu('rente_accident_travail_salarie', period)
        rente_accident_travail_exploitant_agricole = individu('rente_accident_travail_exploitant_agricole', period)

        return max_(rente_accident_travail_salarie, rente_accident_travail_exploitant_agricole)


class rente_accident_travail_salarie(Variable):
    value_type = float
    entity = Individu
    label = u"Montant de la rente d’accident du travail pour les victimes salaries"
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000006073189&idArticle=LEGIARTI000006743072&dateTexte=&categorieLien=cid"
    definition_period = MONTH

    def formula(individu, period):
        previous_year = period.start.period('year').offset(-1)
        salairie = individu('salaire_net', previous_year, options=[ADD]) != 0
        rente_accident_travail_rachat = individu('rente_accident_travail_rachat', period)
        taux_incapacite = individu('taux_accident_travail', period)
        rente_accident_travail_base = individu('rente_accident_travail_base', period) * salairie
        rente_accident_travail_apres_rachat = individu('rente_accident_travail_apres_rachat', period)

        montant_rente_accident_travail = where(rente_accident_travail_rachat != 0, rente_accident_travail_apres_rachat,
                                               rente_accident_travail_base)
        rente_accident_travail_verse = select([taux_incapacite < 0.1, taux_incapacite < 0.5, taux_incapacite >= 0.5],
                                  [0, montant_rente_accident_travail / 4, montant_rente_accident_travail / 12]
                                  )
        return rente_accident_travail_verse


class rente_accident_travail_exploitant_agricole(Variable):
    value_type = float
    entity = Individu
    label = u"Montant de la rente d’accident du travail pour les chefs d'exploitation ou d'entreprise agricole"
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000006071367&idArticle=LEGIARTI000006598097&dateTexte=&categorieLien=cid"
    definition_period = MONTH

    def formula(individu, period):
        previous_year = period.start.period('year').offset(-1)
        non_salarie_agricole = individu('tns_benefice_exploitant_agricole', previous_year,options=[ADD]) != 0
        rente_accident_travail_rachat = individu('rente_accident_travail_rachat', period)
        taux_incapacite = individu('taux_accident_travail', period)
        rente_accident_travail_base = individu('rente_accident_travail_base', period) * non_salarie_agricole
        rente_accident_travail_apres_rachat = individu('rente_accident_travail_apres_rachat', period)

        montant_rente_accident_travail = where(rente_accident_travail_rachat != 0, rente_accident_travail_apres_rachat,
                                               rente_accident_travail_base)
        rente_accident_travail_verse = select([taux_incapacite < 0.3, taux_incapacite >= 0.3],
                                              [0, montant_rente_accident_travail / 12]
                                              )
        return rente_accident_travail_verse


class indemnite_accident_travail(Variable):
    value_type = float
    entity = Individu
    label = u"Indimnite selon taux d'incapacite"
    reference = u"https://www.legifrance.gouv.fr/affichCode.do?idSectionTA=LEGISCTA000006172216&cidTexte=LEGITEXT000006073189"
    definition_period = MONTH

    def formula(individu, period, parameters):
        indem_at = parameters(period).accident_travail.rente.taux
        taux_incapacite = individu('taux_accident_travail', period)
        return select(
            [taux_incapacite == 0.01, taux_incapacite == 0.02, taux_incapacite == 0.03, taux_incapacite == 0.04,
             taux_incapacite == 0.05, taux_incapacite == 0.06, taux_incapacite == 0.07, taux_incapacite == 0.08,
             taux_incapacite == 0.09],
            [indem_at.indemnite_accident_travail['taux_1'], indem_at.indemnite_accident_travail['taux_2'],
             indem_at.indemnite_accident_travail['taux_3'], indem_at.indemnite_accident_travail['taux_4'],
             indem_at.indemnite_accident_travail['taux_5'], indem_at.indemnite_accident_travail['taux_6'],
             indem_at.indemnite_accident_travail['taux_7'], indem_at.indemnite_accident_travail['taux_8'],
             indem_at.indemnite_accident_travail['taux_9']],
        )


class rente_accident_travail_base(Variable):
    value_type = float
    entity = Individu
    label = u"Montant anuel de la rente d’accident du travail"
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do?cidTexte=LEGITEXT000006073189&idArticle=LEGIARTI000006743072&dateTexte=&categorieLien=cid"
    definition_period = MONTH

    def formula(individu,  period, parameters):
        param_rente_at = parameters(period).accident_travail.rente.taux
        taux_incapacite = individu('taux_accident_travail', period)
        taux = param_rente_at.bareme.calc(taux_incapacite)
        taux_rente_accident_travail = select(
            [taux_incapacite < param_rente_at.taux_minimum],
            [0], default=taux
        )
        rente_accident_travail_base = individu('rente_accident_travail_salaire_utile', period) * taux_rente_accident_travail

        return rente_accident_travail_base


class demande_rachat(Variable):
    value_type = bool
    entity = Individu
    label = u"Le victime demande le rachat partiel de la rente"
    definition_period = MONTH


class rente_accident_travail_apres_rachat(Variable):
    value_type = float
    entity = Individu
    label = u"Rachat de la rente d’accident du travail"
    definition_period = MONTH

    def formula(individu, period, parameters):
        rente_at = parameters(period).accident_travail.rente.taux
        age = individu('age', period)
        rente_accident_travail_rachat = individu('rente_accident_travail_rachat', period)
        conversion_rente_capetal = rente_at.capital_representatif[age]
        rente_accident_travail_base = individu('rente_accident_travail_base', period)
        rente_apres_rachat = rente_accident_travail_base - (rente_accident_travail_rachat / conversion_rente_capetal)

        return rente_apres_rachat


class rente_accident_travail_rachat(Variable):
    value_type = float
    entity = Individu
    label = u"Rachat de la rente d’accident du travail"
    reference = u"https://www.legifrance.gouv.fr/eli/arrete/2016/12/19/AFSS1637858A/jo/texte"
    definition_period = MONTH

    def formula(individu, period, parameters):
        rente_at = parameters(period).accident_travail.rente.taux
        demande_rachat = individu('demande_rachat', period)
        age = individu('age', period)
        conversion_rente_capetal = rente_at.capital_representatif[age]
        rente_accident_travail_base = individu('rente_accident_travail_base', period)
        rachat = (rente_accident_travail_base * conversion_rente_capetal) / 4

        return rachat * demande_rachat


class pcrtp_nombre_actes_assistance(Variable):
    value_type = int
    entity = Individu
    label = u"Nombre d'actes nécessitant l'assistance d'une tierce personne"
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=6D8F7F6917ADFBDEAFE1D8A432F39229.tplgfr23s_2?idArticle=LEGIARTI000027267037&cidTexte=LEGITEXT000006073189&dateTexte=20181218"
    definition_period = MONTH


class pcrtp(Variable):
    value_type = float
    entity = Individu
    label = u"Prestation complémentaire pour recours à tierce personne (PCRTP)"
    reference = u"https://www.legifrance.gouv.fr/affichCode.do?idSectionTA=LEGISCTA000006172216&cidTexte=LEGITEXT000006073189"
    definition_period = MONTH

    def formula(individu, period, parameters):
        rente_at = parameters(period).accident_travail.rente.taux
        taux_incapacite = individu('taux_accident_travail', period)
        pcrtp_nombre_actes__assistance = individu('pcrtp_nombre_actes_assistance', period)
        montant_pcrp = rente_at.pcrtp[pcrtp_nombre_actes__assistance]

        return montant_pcrp * (taux_incapacite >= 0.8)


class rente_accident_travail_salaire_utile(Variable):
    value_type = float
    entity = Individu
    label = u"Salaire utile pour calculer la rente d’accident du travail"
    reference = u"https://www.legifrance.gouv.fr/affichCodeArticle.do;jsessionid=7392B9902E4B974EAE8783FAF2D69849.tplgfr30s_1?idArticle=LEGIARTI000006750376&cidTexte=LEGITEXT000006073189&dateTexte=20180823"
    definition_period = MONTH

    def formula(individu, period, parameters):
        previous_year = period.start.period('year').offset(-1)
        rente_at = parameters(period).accident_travail.rente

        salaire_net = individu('salaire_net', previous_year, options=[ADD])
        tns_benefice_exploitant_agricole = individu(
            'tns_benefice_exploitant_agricole', previous_year, options=[ADD])
        salaire = max_(salaire_net, tns_benefice_exploitant_agricole)
        salaire_net_base = max_(rente_at.salaire_net.salaire_minimum, salaire)

        return rente_at.salaire_net.salaire_minimum * rente_at.salaire_net.bareme.calc(
            salaire_net_base / rente_at.salaire_net.salaire_minimum)
