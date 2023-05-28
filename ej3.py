Diurno = 12000
Nocturno = 12000
domingod = Diurno + 2000
domingon = Nocturno + 3000

empleados = {
    "empleado1": ["nocturno", "nocturno", "nocturno", "diurno", "diurno"],
    "empleado2": ["nocturno", "nocturno", "nocturno", "domingo diurno"],
    "empleado3": ["diurno", "diurno", "diurno", "nocturno", "domingo nocturno"]
}

for empleado, turnos in empleados.items():
    pago_diario = 0
    total_semanal = 0
    
    for turno in turnos:
        if turno == "diurno":
            if "domingo" in turnos:
                pago_diario = Diurno + domingod
            else:
                pago_diario = Diurno
        elif turno == "nocturno":
            if "domingo" in turnos:
                pago_diario = Nocturno + domingon
            else:
                pago_diario = Nocturno
        
        total_semanal += pago_diario
    
    empleados[empleado] = {"pago_diario": pago_diario, "total_semanal": total_semanal}

for empleado, info_empleado in empleados.items():
    print(f"Empleado: {empleado}")
    print(f"Pago diario: {info_empleado['pago_diario']} CLP")
    print(f"Total semanal: {info_empleado['total_semanal']} CLP")
    print()
