class Informe:
    def __init__(self, id_paciente, id_informe, fecha_registro, antece_familiar, enfer_previas, depresion_diag,
                 accidente_cv, fumador, alcohol, actividad_fisica, trastorno_sueno, horas_sueno,
                 calidad_sueno, nivel_estres, dieta_saludable, presion_arterial):
        self._id_paciente = id_paciente
        self._id_informe = id_informe
        self._fecha_registro = fecha_registro
        self._antece_familiar = antece_familiar
        self._enfer_previas = enfer_previas
        self._depresion_diag = depresion_diag
        self._accidente_cv = accidente_cv
        self._fumador = fumador
        self._alcohol = alcohol
        self._actividad_fisica = actividad_fisica
        self._trastorno_sueno = trastorno_sueno
        self._horas_sueno = horas_sueno
        self._calidad_sueno = calidad_sueno
        self._nivel_estres = nivel_estres
        self._dieta_saludable = dieta_saludable
        self._presion_arterial = presion_arterial

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, id_paciente):
        self._id_paciente = id_paciente

    @property
    def id_informe(self):
        return self._id_informe

    @id_informe.setter
    def id_informe(self, id_informe):
        self._id_informe = id_informe

    @property
    def fecha_registro(self):
        return self._fecha_registro

    @fecha_registro.setter
    def fecha_registro(self, fecha_registro):
        self._fecha_registro = fecha_registro

    @property
    def antece_familiar(self):
        return self._antece_familiar

    @antece_familiar.setter
    def antece_familiar(self, antece_familiar):
        self._antece_familiar = antece_familiar

    @property
    def enfer_previas(self):
        return self._enfer_previas

    @enfer_previas.setter
    def enfer_previas(self, enfer_previas):
        self._enfer_previas = enfer_previas

    @property
    def depresion_diag(self):
        return self._depresion_diag

    @depresion_diag.setter
    def depresion_diag(self, depresion_diag):
        self._depresion_diag = depresion_diag

    @property
    def accidente_cv(self):
        return self._accidente_cv

    @accidente_cv.setter
    def accidente_cv(self, accidente_cv):
        self._accidente_cv = accidente_cv

    @property
    def fumador(self):
        return self._fumador

    @fumador.setter
    def fumador(self, fumador):
        self._fumador = fumador

    @property
    def alcohol(self):
        return self._alcohol

    @alcohol.setter
    def alcohol(self, alcohol):
        self._alcohol = alcohol

    @property
    def actividad_fisica(self):
        return self._actividad_fisica

    @actividad_fisica.setter
    def actividad_fisica(self, actividad_fisica):
        self._actividad_fisica = actividad_fisica

    @property
    def trastorno_sueno(self):
        return self._trastorno_sueno

    @trastorno_sueno.setter
    def trastorno_sueno(self, trastorno_sueno):
        self._trastorno_sueno = trastorno_sueno

    @property
    def horas_sueno(self):
        return self._horas_sueno

    @horas_sueno.setter
    def horas_sueno(self, horas_sueno):
        self._horas_sueno = horas_sueno

    @property
    def calidad_sueno(self):
        return self._calidad_sueno

    @calidad_sueno.setter
    def calidad_sueno(self, calidad_sueno):
        self._calidad_sueno = calidad_sueno

    @property
    def nivel_estres(self):
        return self._nivel_estres

    @nivel_estres.setter
    def nivel_estres(self, nivel_estres):
        self._nivel_estres = nivel_estres

    @property
    def dieta_saludable(self):
        return self._dieta_saludable

    @dieta_saludable.setter
    def dieta_saludable(self, dieta_saludable):
        self._dieta_saludable = dieta_saludable

    @property
    def presion_arterial(self):
        return self._presion_arterial

    @presion_arterial.setter
    def presion_arterial(self, presion_arterial):
        self._presion_arterial = presion_arterial
