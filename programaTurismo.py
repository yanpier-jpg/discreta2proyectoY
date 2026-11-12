while True:
    print("\n========= MENÚ PRINCIPAL =========")
    print("1. Procesar")
    print("2. Salir")
    
    while True:
        try:
            op = int(input("Ingrese la opción del menú principal:\t\t"))
            break
        except ValueError:
            print("ERROR.... Por favor ingrese un número.")

        if op == 2:
            print("Saliendo del programa...")
            break

        match op:
            case 1: # Procesar 
                # Ingreso del tipo de cambio
                tipo_cambio = float(input("Ingrese el tipo de cambio del día:\t\t"))
                
                print("\n====== BIENVENIDO A SU DESTINO TURISTICO ======")
                print("1. Punta Cana")
                print("2. San Andrés")
                print("3. Cancún")
                print("4. Salir")
                
                while True:
                    Opciones_de_paquete = int(input("Desea adquirir uno de estos destinos:\t\t"))
                    if (Opciones_de_paquete < 1 or Opciones_de_paquete > 4):
                        print("ERROR.... Opción no encontrada. Vuelva a seleccionar")
                    else:
                        break
                
                if (Opciones_de_paquete == 4):
                    print("Regresando al menú principal...")
                    continue
                    
                while True:
                    Cantidad_de_personas = int(input("La cantidad de personas que adquiriran este paquete:\t\t"))
                    if (Cantidad_de_personas < 1):
                        print("ERROR.... Cantidad errónea. Vuelva a digitalizar")
                    else:
                        break
                        
                # Evaluamos el paquete seleccionado, no la cantidad de personas
                match Opciones_de_paquete:
                    case 1: # Punta Cana 
                        Precio_Por_Personas = 780 * Cantidad_de_personas
                        if Cantidad_de_personas <= 4:
                            Total_En_Dolar = Precio_Por_Personas
                        else:
                            Total_En_Dolar = Precio_Por_Personas - (Precio_Por_Personas * 0.035)

                    case 2: # San Andrés
                        Precio_Por_Personas = 1350 * Cantidad_de_personas
                        if Cantidad_de_personas <= 4:
                            Total_En_Dolar = Precio_Por_Personas
                        else:
                            Total_En_Dolar = Precio_Por_Personas - (Precio_Por_Personas * 0.04)

                    case 3: # Cancún
                        Precio_Por_Personas = 2550 * Cantidad_de_personas
                        if Cantidad_de_personas <= 4:
                            Total_En_Dolar = Precio_Por_Personas
                        else:
                            Total_En_Dolar = Precio_Por_Personas - (Precio_Por_Personas * 0.045)

                Total_EN_Soles = Total_En_Dolar * tipo_cambio

                print("\n======= OPERACIÓN CON EXITO =======")
                print("Compra en dólares:\t$", Total_En_Dolar)
                print("Compra en soles:\tS/", Total_EN_Soles)          