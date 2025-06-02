class Informe:
    def __init__(self, id, fechaRegistro, antecFamiliaresAlzheimer, diabetes, colesterol, migrainas,
                hipertension, cardiopatia, depresionDiag, accidenteCerebrovascular, trastornoSueno,
                horaSueno, calidadSueno, fumador, consumoAlcohol, actividadFisica, nivelEstres,
                dietaSaludable, presionArterialSis, presionArterialDia):
        self._id = id
        self._fechaRegistro = fechaRegistro
        self._antecFamiliaresAlzheimer = antecFamiliaresAlzheimer
        self._diabetes = diabetes
        self._colesterol = colesterol
        self._migrainas = migrainas
        self._hipertension = hipertension
        self._cardiopatia = cardiopatia
        self._depresionDiag = depresionDiag
        self._accidenteCerebrovascular = accidenteCerebrovascular
        self._trastornoSueno = trastornoSueno
        self._horaSueno = horaSueno
        self._calidadSueno = calidadSueno
        self._fumador = fumador
        self._consumoAlcohol = consumoAlcohol
        self._actividadFisica = actividadFisica
        self._nivelEstres = nivelEstres
        self._dietaSaludable = dietaSaludable
        self._presionArterialSis = presionArterialSis
        self._presionArterialDia = presionArterialDia

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def fechaRegistro(self):
        return self._fechaRegistro

    @fechaRegistro.setter
    def fechaRegistro(self, fechaRegistro):
        self._fechaRegistro = fechaRegistro

    @property
    def antecFamiliaresAlzheimer(self):
        return self._antecFamiliaresAlzheimer

    @antecFamiliaresAlzheimer.setter
    def antecFamiliaresAlzheimer(self, antecFamiliaresAlzheimer):
        self._antecFamiliaresAlzheimer = antecFamiliaresAlzheimer

    @property
    def diabetes(self):
        return self._diabetes

    @diabetes.setter
    def diabetes(self, diabetes):
        self._diabetes = diabetes

    @property
    def colesterol(self):
        return self._colesterol

    @colesterol.setter
    def colesterol(self, colesterol):
        self._colesterol = colesterol

    @property
    def migrainas(self):
        return self._migrainas

    @migrainas.setter
    def migrainas(self, migrainas):
        self._migrainas = migrainas

    @property
    def hipertension(self):
        return self._hipertension

    @hipertension.setter
    def hipertension(self, hipertension):
        self._hipertension = hipertension

    @property
    def cardiopatia(self):
        return self._cardiopatia

    @cardiopatia.setter
    def cardiopatia(self, cardiopatia):
        self._cardiopatia = cardiopatia

    @property
    def depresionDiag(self):
        return self._depresionDiag

    @depresionDiag.setter
    def depresionDiag(self, depresionDiag):
        self._depresionDiag = depresionDiag

    @property
    def accidenteCerebrovascular(self):
        return self._accidenteCerebrovascular

    @accidenteCerebrovascular.setter
    def accidenteCerebrovascular(self, accidenteCerebrovascular):
        self._accidenteCerebrovascular = accidenteCerebrovascular

    @property
    def trastornoSueno(self):
        return self._trastornoSueno

    @trastornoSueno.setter
    def trastornoSueno(self, trastornoSueno):
        self._trastornoSueno = trastornoSueno

    @property
    def horaSueno(self):
        return self._horaSueno

    @horaSueno.setter
    def horaSueno(self, horaSueno):
        self._horaSueno = horaSueno

    @property
    def calidadSueno(self):
        return self._calidadSueno

    @calidadSueno.setter
    def calidadSueno(self, calidadSueno):
        self._calidadSueno = calidadSueno

    @property
    def fumador(self):
        return self._fumador

    @fumador.setter
    def fumador(self, fumador):
        self._fumador = fumador

    @property
    def consumoAlcohol(self):
        return self._consumoAlcohol

    @consumoAlcohol.setter
    def consumoAlcohol(self, consumoAlcohol):
        self._consumoAlcohol = consumoAlcohol

    @property
    def actividadFisica(self):
        return self._actividadFisica

    @actividadFisica.setter
    def actividadFisica(self, actividadFisica):
        self._actividadFisica = actividadFisica

    @property
    def nivelEstres(self):
        return self._nivelEstres

    @nivelEstres.setter
    def nivelEstres(self, nivelEstres):
        self._nivelEstres = nivelEstres

    @property
    def dietaSaludable(self):
        return self._dietaSaludable

    @dietaSaludable.setter
    def dietaSaludable(self, dietaSaludable):
        self._dietaSaludable = dietaSaludable

    @property
    def presionArterialSis(self):
        return self._presionArterialSis

    @presionArterialSis.setter
    def presionArterialSis(self, presionArterialSis):
        self._presionArterialSis = presionArterialSis

    @property
    def presionArterialDia(self):
        return self._presionArterialDia

    @presionArterialDia.setter
    def presionArterialDia(self, presionArterialDia):
        self._presionArterialDia = presionArterialDia
