import serial

def StoreTemplateInFlash(template_data, template_name):
    try:
        COM = 'COM12'  # Reemplaza '/dev/ttyUSB0' con el puerto serial correcto de tu impresora
        ser = serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)

        command = f"^DFF{template_name},R:{len(template_data)}," + template_data + "\n"
        ser.write(bytes(command.encode('UTF-8')))
        ser.close()

        print(f"Template '{template_name}' almacenado en la memoria flash correctamente.")

    except Exception as e:
        print("Error al almacenar el template en la memoria flash:", e)

def PrintWithStoredTemplate(fecha, partNo, Qty, supplier, serie, OT, template_name):
    try:
        COM = 'COM12'  # Reemplaza '/dev/ttyUSB0' con el puerto serial correcto de tu impresora
        ser = serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)

        print_command = f"""
        ^XA
        ^XFR:{template_name}
        ^FN1^FD{fecha}^FS	
        ^FN2^FD>{partNo}^FS
        ^FN3^FD>{Qty}^FS
        ^FN4^FD>{supplier}^FS
        ^FN5^FD>{serie}^FS
        ^FN6^FD>{OT}^FS
        ^XZ
        """
        ser.write(bytes(print_command.encode('UTF-8')))
        ser.close()

        print("Impresión realizada correctamente utilizando el template almacenado.")

    except Exception as e:
        print("Error al imprimir utilizando el template almacenado:", e)

# Ejemplo de uso para almacenar el template en la memoria flash
template_data = """
        ^XA
        ^DFR:SAMPLE.GRF^FS
        ^MMT
        ^PW815
        ^LL1215
        ^LS0
        ^FO196,8^GB0,1191,8^FS
        ^FO396,0^GB0,1191,8^FS
        ^FO595,0^GB0,1191,8^FS
        ^FO8,276^GB192,0,8^FS
        ^FO200,595^GB200,0,8^FS
        ^FO400,412^GB200,0,8^FS
        ^FO599,356^GB168,0,8^FS
        ^FT93,224^A0B,37,38^FH\^CI28^FDRAD ASSY^FS^CI27
        ^FT139,224^A0B,37,38^FH\^CI28^FDATLAS^FS^CI27
        ^FT45,1197^A0B,37,38^FH\^CI28^FDPart No^FS^CI27
        ^FT91,1197^A0B,37,38^FH\^CI28^FD(P)^FS^CI27
        ^FT253,1196^A0B,37,38^FH\^CI28^FDQuantity^FS^CI27
        ^FT299,1196^A0B,37,38^FH\^CI28^FD(Q)^FS^CI27
        ^FT453,1191^A0B,37,38^FH\^CI28^FDSupplier^FS^CI27
        ^FT499,1191^A0B,37,38^FH\^CI28^FD(V)^FS^CI27
        ^FT652,1190^A0B,37,38^FH\^CI28^FDSerial^FS^CI27
        ^FT698,1190^A0B,37,38^FH\^CI28^FD(5S)^FS^CI27
        ^FT253,580^A0B,37,38^FH\^CI28^FDNo. Lote^FS^CI27
        ^FT299,580^A0B,37,38^FH\^CI28^FD(1T)^FS^CI27
        ^FT453,396^A0B,37,38^FH\^CI28^FDOT^FS^CI27
        ^FT499,396^A0B,37,38^FH\^CI28^FD(K)^FS^CI27
        ^FT632,348^A0B,25,25^FH\^CI28^FDProduction Date:^FS^CI27
        ^FT692,346^A0B,37,38^FH\^CI28^FN1^FS^CI27    
        ^FT752,339^A0B,25,25^FH\^CI28^FDExpiry Date:^FS^CI27
        ^FT796,1162^A0B,25,25^FH\^CI28^FDAIR TEMP DE MEXICO SA DE C.V. Km. 20 Carretera Merida-Uman Tablaje Rustico No 4193 C.P. 97390 ^FS^CI27
        ^BY3,3,136^FT160,1001^BCB,,Y,N
        ^FH\^FN2^FS                                  
        ^BY3,3,136^FT363,1001^BCB,,Y,N
        ^FH\^FN3^FS                                   
        ^BY3,3,136^FT562,1001^BCB,,Y,N
        ^FH\^FN4^FS                                  
        ^BY3,3,99^FT730,1001^BCB,,Y,N
        ^FH\^FN5^FS                                   
        ^BY3,3,136^FT560,300^BCB,,Y,N
        ^FH\^FN6^FS                                   
        ^PQ1,,,Y
        ^XZ
"""
#StoreTemplateInFlash(template_data, "SAMPLE.ZPL")
# Ejemplo de uso para imprimir utilizando el template almacenado
fecha = "2024-05-14"
partNo = "12345"
Qty = "10"
supplier = "SupplierA"
serie = "ABC123"
OT = "OT-001"
template_name = "SAMPLE.ZPL"

PrintWithStoredTemplate(fecha, partNo, Qty, supplier, serie, OT, template_name)
