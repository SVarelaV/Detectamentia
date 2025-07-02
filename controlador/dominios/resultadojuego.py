class ResultadoJuego:
    def __init__(self, id_resultado, nombreJuego, fecha, tiempoReaccion, aciertos, errores, numeroIntentos, tiempoTotal):
        self._id_resultado = id_resultado
        self._nombreJuego = nombreJuego
        self._fecha = fecha
        self._tiempoReaccion = tiempoReaccion
        self._aciertos = aciertos
        self._errores = errores
        self._numeroIntentos = numeroIntentos
        self._tiempoTotal = tiempoTotal

    @property
    def id_resultado(self):
        return self._id_resultado

    @id_resultado.setter
    def id_resultado(self, id_resultado):
        self._id_resultado = id_resultado

    @property
    def nombreJuego(self):
        return self._nombreJuego
    
    @nombreJuego.setter
    def nombreJuego(self, nombreJuego):
        self._nombreJuego = nombreJuego

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def tiempoReaccion(self):
        return self._tiempoReaccion

    @tiempoReaccion.setter
    def tiempoReaccion(self, tiempoReaccion):
        self._tiempoReaccion = tiempoReaccion

    @property
    def aciertos(self):
        return self._aciertos

    @aciertos.setter
    def aciertos(self, aciertos):
        self._aciertos = aciertos

    @property
    def errores(self):
        return self._errores

    @errores.setter
    def errores(self, errores):
        self._errores = errores

    @property
    def numeroIntentos(self):
        return self._numeroIntentos

    @numeroIntentos.setter
    def numeroIntentos(self, numeroIntentos):
        self._numeroIntentos = numeroIntentos

    @property
    def tiempoTotal(self):
        return self._tiempoTotal

    @tiempoTotal.setter
    def tiempoTotal(self, tiempoTotal):
        self._tiempoTotal = tiempoTotal
