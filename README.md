## 📝 Descripción del Proyecto

Este sistema es una aplicación web tipo **CRUD** (Create, Read, Update, Delete) diseñada para el control de clientes en un gimnasio (**Zona Fit**). El proyecto aplica una arquitectura de capas, separando la lógica de negocio de la persistencia de datos mediante el patrón **DAO (Data Access Object)**.

La aplicación permite gestionar el ciclo de vida completo de un usuario: desde el registro inicial, la visualización en tiempo real de la base de datos, hasta la actualización de membresías y eliminación de registros.

## 🛠️ Stack Tecnológico

* **Backend:** Desarrollado con **Python 3.x**, utilizando el framework **Flask** para el manejo de rutas y lógica de servidor.
* **Base de Datos:** **MySQL** para el almacenamiento relacional de la información.
* **ORM / Acceso a Datos:** Uso de **MySQL Connector** para la comunicación directa con la base de datos y **Flask-WTF** para la gestión y validación de formularios.
* **Frontend:** Plantillas dinámicas procesadas con el motor **Jinja2**, estructuradas con **HTML5** y **Boostrap**.
* **Arquitectura:** Implementación de **Patrones de Diseño (DAO)** para asegurar un código mantenible, escalable y con bajo acoplamiento.

---


## 📸 Capturas de Pantalla del Proyecto

### 🗄️ Visualización en Base de Datos
Aquí se muestra cómo se persisten los datos de los clientes en MySQL.
<img width="1776" alt="visual_data_base" src="https://github.com/user-attachments/assets/f7d5f177-844a-40fa-a0af-a14f2754923c" />

---

### 🏠 Interfaz de Inicio (Listado)
Vista principal donde se cargan todos los clientes registrados en la Zona Fit.
<img width="1702" alt="inicio" src="https://github.com/user-attachments/assets/9a1930bb-5ab3-44eb-9fee-1a607678d0de" />

---

### ✍️ Edición de Usuario
Funcionalidad para modificar los datos existentes de un cliente por su ID.
<img width="1811" alt="editando_usuario" src="https://github.com/user-attachments/assets/1645b9b8-8f9f-43ad-8428-bdee336ef0e6" />

---

### ➕ Registro de Nuevo Usuario
Formulario validado para dar de alta nuevos miembros en el sistema.
<img width="1646" alt="Agregando_usuario" src="https://github.com/user-attachments/assets/95ddca83-3a38-48f9-b90f-085c48b9ae67" />
