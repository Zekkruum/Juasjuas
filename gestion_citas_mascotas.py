from decoradores import decorador_mio


usuarios = {}
mascotas = {}
citas = {}


class Usuario:
    def __init__(self, documento, nombre, telefono, correo):
        self.documento = documento
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class Mascota:
    def __init__(self, id_mascota, nombre, especie, edad, raza, dueño_id):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.raza = raza
        self.dueño_id = dueño_id

class FichaMedica(Mascota):
    def __init__(self, id_mascota, nombre, especie, edad, raza, dueño_id, vacunas, alergias, historial):
        super().__init__(id_mascota, nombre, especie, edad, raza, dueño_id)
        self.vacunas = vacunas
        self.alergias = alergias
        self.historial = historial

    def mostrar_ficha(self):
        print(f"\nFicha médica de {self.nombre} (ID Dueño: {self.dueño_id}):")
        print(f"- Especie: {self.especie}, Edad: {self.edad}, Raza: {self.raza}")
        print(f"- Vacunas: {self.vacunas}")
        print(f"- Alergias: {self.alergias}")
        print(f"- Historial Médico: {self.historial}")

class Cita:
    def __init__(self, id_cita, id_mascota, fecha, motivo):
        self.id_cita = id_cita
        self.id_mascota = id_mascota
        self.fecha = fecha
        self.motivo = motivo

    def mostrar(self):
        print(f"\nCita ID: {self.id_cita} | Mascota ID: {self.id_mascota}")
        print(f"- Fecha: {self.fecha}")
        print(f"- Motivo: {self.motivo}")

# Gestión de usuarios
@decorador_mio
def crear_usuario():
    documento = input("Documento: ")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo: ")
    usuarios[documento] = Usuario(documento, nombre, telefono, correo)
    print('===========================================================')
    print("Usuario creado correctamente.")

@decorador_mio
def ver_usuarios():
    for doc, usuario in usuarios.items():
        print(f"\nDocumento: {doc} - Nombre: {usuario.nombre} - Teléfono: {usuario.telefono} - Correo: {usuario.correo}")

@decorador_mio
def actualizar_usuario():
    doc = input("Documento del usuario a actualizar: ")
    if doc in usuarios:
        nombre = input("Nuevo nombre: ")
        telefono = input("Nuevo teléfono: ")
        correo = input("Nuevo correo: ")
        usuarios[doc] = Usuario(doc, nombre, telefono, correo)
        
        print('===========================================================')
        print("Usuario actualizado.")
    else:
        print("Usuario no encontrado.")

@decorador_mio
def eliminar_usuario():
    doc = input("Documento del usuario a eliminar: ")
    if doc in usuarios:
        del usuarios[doc]

        print('===========================================================')
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

# Gestión de mascotas
@decorador_mio
def registrar_mascota():
    id_mascota = input("ID de la mascota: ")
    nombre = input("Nombre: ")
    especie = input("Especie: ")
    edad = input("Edad: ")
    raza = input("Raza: ")
    dueño_id = input("Documento del dueño: ")
    if dueño_id in usuarios:
        mascotas[id_mascota] = Mascota(id_mascota, nombre, especie, edad, raza, dueño_id)
        print("Mascota registrada correctamente.")
    else:
        print("Dueño no registrado.")

@decorador_mio
def ver_mascotas():
    for id_m, mascota in mascotas.items():
        print(f"\nID Mascota: {id_m} - Nombre: {mascota.nombre} - Especie: {mascota.especie}")
        print(f"  Edad: {mascota.edad} - Raza: {mascota.raza} - Dueño: {mascota.dueño_id}")

@decorador_mio
def actualizar_mascota():
    id_m = input("ID de la mascota: ")
    if id_m in mascotas:
        nombre = input("Nuevo nombre: ")
        especie = input("Nueva especie: ")
        edad = input("Nueva edad: ")
        raza = input("Nueva raza: ")
        mascotas[id_m].nombre = nombre
        mascotas[id_m].especie = especie
        mascotas[id_m].edad = edad
        mascotas[id_m].raza = raza
        print("Datos actualizados.")
    else:
        print("Mascota no encontrada.")

@decorador_mio
def eliminar_mascota():
    id_m = input("ID de la mascota a eliminar: ")
    if id_m in mascotas:
        del mascotas[id_m]
        print("Mascota eliminada.")
    else:
        print("Mascota no encontrada.")

@decorador_mio
def contar_mascotas_por_dueño():
    doc = input("Ingrese el documento del dueño: ")
    mascotas_del_dueño = [m for m in mascotas.values() if m.dueño_id == doc]

    if doc not in usuarios:
        print("No existe un usuario con ese documento.")
        return

    if mascotas_del_dueño:
        print(f"\nEl usuario '{usuarios[doc].nombre}' tiene {len(mascotas_del_dueño)} mascota(s):")
        for idx, mascota in enumerate(mascotas_del_dueño, start=1):
            print(f"  {idx}. Nombre: {mascota.nombre} | Especie: {mascota.especie} | Edad: {mascota.edad}")
    else:
        print(f"El usuario '{usuarios[doc].nombre}' no tiene mascotas registradas.")

# Gestión de citas
@decorador_mio
def agendar_cita():
    id_cita = input("ID de la cita: ")
    id_mascota = input("ID de la mascota: ")
    if id_mascota in mascotas:
        fecha = input("Fecha de la cita: ")
        motivo = input("Motivo: ")
        citas[id_cita] = Cita(id_cita, id_mascota, fecha, motivo)
        print("Cita agendada.")
    else:
        print("Mascota no registrada.")

@decorador_mio
def reagendar_cita():
    id_cita = input("ID de la cita: ")
    if id_cita in citas:
        fecha = input("Nueva fecha: ")
        motivo = input("Nuevo motivo: ")
        citas[id_cita].fecha = fecha
        citas[id_cita].motivo = motivo
        print("Cita actualizada.")
    else:
        print("Cita no encontrada.")

@decorador_mio
def cancelar_cita():
    id_cita = input("ID de la cita a cancelar: ")
    if id_cita in citas:
        del citas[id_cita]
        print("Cita cancelada.")
    else:
        print("Cita no encontrada.")

@decorador_mio
def ver_citas():
    for c in citas.values():
        c.mostrar()
    else:
        print("No hay citas agendadas.")

# Menús
@decorador_mio
def mostrar_menu_principal():
    print("""
|==================== MENÚ PRINCIPAL ==================|
1. Gestión de Usuarios
2. Gestión de Mascotas
3. Gestión de Citas Médicas
4. Salir
""")

@decorador_mio
def menu_usuarios():
    print("""
-- Gestión de Usuarios --
1. Crear Usuario
2. Ver Usuarios
3. Actualizar Usuario
4. Eliminar Usuario
5. Volver
""")

@decorador_mio
def menu_mascotas():
    print("""
-- Gestión de Mascotas --
1. Registrar Mascota
2. Ver Mascotas
3. Actualizar Mascota
4. Eliminar Mascota
5. Contar Mascotas por Dueño
6. Volver
""")

@decorador_mio
def menu_citas():
    print("""
-- Gestión de Citas Médicas --
1. Agendar Cita
2. Reagendar Cita
3. Cancelar Cita
4. Ver Citas
5. Volver
""")

@decorador_mio
def ejecutar_menu():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            while True:
                menu_usuarios()
                o = input("Seleccione una opción: ")
                if o == "1": crear_usuario()
                elif o == "2": ver_usuarios()
                elif o == "3": actualizar_usuario()
                elif o == "4": eliminar_usuario()
                elif o == "5": break
        elif opcion == "2":
            while True:
                menu_mascotas()
                o = input("Seleccione una opción: ")
                if o == "1": registrar_mascota()
                elif o == "2": ver_mascotas()
                elif o == "3": actualizar_mascota()
                elif o == "4": eliminar_mascota()
                elif o == "5": contar_mascotas_por_dueño()
                elif o == "6": break
        elif opcion == "3":
            while True:
                menu_citas()
                o = input("Seleccione una opción: ")
                if o == "1": agendar_cita()
                elif o == "2": reagendar_cita()
                elif o == "3": cancelar_cita()
                elif o == "4": ver_citas()
                elif o == "5": break
        elif opcion == "4":
            print("Saliendo...")
            break
                


ejecutar_menu()