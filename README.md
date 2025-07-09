# 🧠 DetectaMentIA

**DetectaMentIA** es una aplicación de escritorio interactiva desarrollada en Python, cuyo objetivo es **predecir el riesgo de padecer Alzheimer** mediante la recolección de datos clínicos y el desempeño en mini-juegos cognitivos.

Proyecto final del Bootcamp de Ciencia de Datos.

---

## 🎯 Objetivo

Desarrollar una herramienta que:

- Evalúe funciones cognitivas como memoria y atención.
- Recoja datos clínicos relevantes.
- Aplique un modelo predictivo para estimar el riesgo de Alzheimer.
- Ofrezca recomendaciones personalizadas al paciente.
- Sirva de apoyo a profesionales de la salud.

---

## 👥 Usuarios

- 🧓 **Pacientes**: Acceden a los juegos con credenciales.
- 🧑‍⚕️ **Profesionales de la salud**: Registran pacientes, revisan informes y resultados.

---

## 🧩 Mini-juegos incluidos

| Juego             | Evalúa                          | Métricas                          |
|------------------|----------------------------------|-----------------------------------|
| Stroop Test       | Atención selectiva               | Tiempo de reacción, aciertos      |
| N-back            | Memoria de trabajo               | Nivel máximo, precisión, tiempo   |
| Encuentra el Par  | Memoria visual a corto plazo     | Intentos, tiempo total, errores   |

---

## 🧱 Arquitectura del proyecto

### ✔️ Patrón **MVC (Modelo - Vista - Controlador)**

- **Vista**: `menu_*.py`, `validacion.py`
- **Controlador**: `usuarios.py`, `pacientes.py`, `informes.py`, `resultadojuegos.py`
- **Modelo**: `usuario.py`, `paciente.py`, `informe.py`, `resultadojuego.py`


---

## 🔄 Flujo de datos

1. El profesional da de alta al paciente (usuario + datos + informe).
2. El paciente accede con su cuenta y realiza los juegos.
3. Se almacenan los resultados.
4. Se ejecuta el modelo predictivo (en desarrollo).
5. El profesional accede al dashboard para evaluar riesgos y recomendaciones.

---

## 📁 Estructura de carpetas


---

## 📊 A futuro...

- [ ] Integración de modelo de Machine Learning.
- [ ] Visualización de dashboard con gráficos.
- [ ] Exportación de informes en PDF.
- [ ] Sistema de login completo con recuperación de contraseña.

---

## 🧪 Requisitos

- Python 3.8+
- SQL Server u otra base de datos compatible
- Paquetes estándar: `typing`, `abc`, `re`, etc.

---

## 🤝 Créditos

Proyecto final del bootcamp de Ciencia de Datos.  

---

## 📜 Licencia

Este proyecto es de uso académico y sin fines comerciales.

