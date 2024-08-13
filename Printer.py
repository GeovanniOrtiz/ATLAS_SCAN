from PySide6.QtCore import QCoreApplication
import serial
from main import *
import socket
COM = "COM12"
HOST = "192.168.100.85"#85

class PrinterState:
    def __init__(self):
        self.mState = 0
        self.mText = ""

def check_error(m_string1, m_string2):
    error = ()
    if m_string1[1] == "1":
        error = "     SIN ETIQUETA",1
    elif m_string1[2] == "1" and m_string1[1] == "0" and m_string2[2] == "0":
        error = "     PAUSADA",2
    elif m_string2[2] == "1":
        error = "     ABIERTA",3
    elif m_string2[3] == "1":
        error = "     VERIFICAR RIBBON",4
    else:
        error = "     CONECTADA",0
    return error
def ConsultStatePrint_Rs232(ui_main, printer_state):
    try:
        with serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE, xonxoff=False,  rtscts=False,  dsrdtr=False) as ser:
            # ser = serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10,stopbits=serial.STOPBITS_ONE)  # Open port
            check_command = b"~HS"
            ser.write(check_command)
            r = ser.read_until('', 82)
            string_text = r.decode('utf-8')  # Decodificar bytes a texto
            lines = string_text.splitlines()  # Dividir en líneas
            S1 = lines[0].split(",")
            S2 = lines[1].split(",")
            state = check_error(S1, S2)
            printer_state.mState = state[1]
            printer_state.mText = state[0]
            ser.close()
    except serial.SerialTimeoutException:
        print("Timeout error while communicating with the serial port")
        printer_state.mState = 5
    except serial.SerialException as e:
        print("Serial communication error:", e)
        printer_state.mState = 5
    except Exception as e:
        print("fatal error", e)
        printer_state.mState = 5
def SendTemplate_Rs232():
    try:
        #ser = serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10,stopbits=serial.STOPBITS_ONE)  # Open port
        with serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE, xonxoff=False,  rtscts=False,  dsrdtr=False) as ser:
            # ^DFR:SAMPLE.GRF^FS
            template = f"""
                    ^XA
                    ^DFE:Label_Atlas.ZPL^FS
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
                    ^FT698,1190^A0B,37,38^FH\^CI28^FD(4S)^FS^CI27
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
                    ^XZ
                    """
            ser.write(bytes(template.encode('UTF-8')))
            ser.close()
    except serial.SerialTimeoutException:
        print("Timeout error while communicating with the serial port")
    except serial.SerialException as e:
        print("Serial communication error:", e)
    except Exception as e:
        print("Other error:", e)
def SendReqPrint_Rs232(fecha,partNo,Qty,supplier,serie,OT):
    try:
        #ser = serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10,stopbits=serial.STOPBITS_ONE)  # Open port
        with serial.Serial(COM, baudrate=9600, bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE, xonxoff=False,  rtscts=False,  dsrdtr=False) as ser:
            # ^XFR:SAMPLE.GRF
            reqPrint = f"""
                   ^XA
                   ^XFE:Label_Atlas.ZPL^FS
                   ^FN1^FD{fecha}^FS	
                   ^FN2^FD>:{partNo}^FS
                   ^FN3^FD>:{Qty}^FS
                   ^FN4^FD>;{supplier}^FS
                   ^FN5^FD>;{serie}^FS
                   ^FN6^FD>;{OT}^FS
                   ^PQ1,,,Y
                   ^XZ
                   """
            ser.write(bytes(reqPrint.encode('UTF-8')))
            ser.close()
    except serial.SerialTimeoutException:
        print("Timeout error while communicating with the serial port")
    except serial.SerialException as e:
        print("Serial communication error:", e)
    except Exception as e:
        print("Other error:", e)


def ConsultStatePrint(ui_main, printer_state):
    try:
        # Establecer conexión TCP/IP
        host = HOST # Dirección IP de la impresora
        port = 4100  # Puerto estándar para impresoras Zebra

        with socket.create_connection((host, port), timeout=2) as sock:

            check_command = b"~HS"
            sock.sendall(check_command)

            r = b""
            r += sock.recv(82)  # Leer datos hasta recibir la terminación esperada
            #print(r)

            string_text = r.decode('utf-8')  # Decodificar bytes a texto
            lines = string_text.splitlines()  # Dividir en líneas
            S1 = lines[0].split(",")
            S2 = lines[1].split(",")
            state = check_error(S1, S2)
            printer_state.mState = state[1]
            printer_state.mText = state[0]
    except socket.timeout:
        print("Timeout error while communicating with the printer")
        printer_state.mState = 5
    except socket.error as e:
        print("Network communication error:", e)
        printer_state.mState = 5
    except Exception as e:
        print("fatal error", e)
        printer_state.mState = 5
def SendReqPrint(fecha, partNo, qty, supplier, serie, ot):
    try:
        # Establecer conexión TCP/IP
        host = HOST  # Dirección IP de la impresora
        port = 4100  # Puerto estándar para impresoras Zebra

        with socket.create_connection((host, port), timeout=10) as sock:
            reqPrint = f"""^XA
            ^XFE:Label_Atlas.ZPL^FS
            ^FN1^FD{fecha}^FS	
            ^FN2^FD>:{partNo}^FS
            ^FN3^FD>:{qty}^FS
            ^FN4^FD>;{supplier}^FS
            ^FN5^FD>;{serie}^FS
            ^FN6^FD>;{ot}^FS
            ^PQ1,,,Y
            ^XZ      
            """
            sock.sendall(reqPrint.encode('UTF-8'))
            print("Print request sent successfully")

    except socket.timeout:
        print("Timeout error while communicating with the printer")
    except socket.error as e:
        print("Network communication error:", e)
    except Exception as e:
        print("Other error:", e)
def SendTemplate():
    try:
        # Establecer conexión TCP/IP
        host = HOST  # Dirección IP de la impresora
        port = 4100  # Puerto estándar para impresoras Zebra

        with socket.create_connection((host, port), timeout=10) as sock:
            template = f"""^XA
                    ^DFE:Label_Atlas.ZPL^FS
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
                    ^FT698,1190^A0B,37,38^FH\^CI28^FD(4S)^FS^CI27
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
                    ^XZ            
                    """
            sock.sendall(template.encode('UTF-8'))
            print("Set Template sent succesfully")
    except serial.SerialTimeoutException:
        print("Timeout error while communicating with the serial port")
    except serial.SerialException as e:
        print("Serial communication error:", e)
    except Exception as e:
        print("Other error:", e)
def SendLabelCalibrate():
    try:
        # Establecer conexión TCP/IP
        host = HOST  # Dirección IP de la impresora
        port = 4100  # Puerto estándar para impresoras Zebra

        with socket.create_connection((host, port), timeout=2) as sock:
            Calibrate = b"~JC"
            sock.sendall(Calibrate)
            print("Calibrate sent succesfully")

    except serial.SerialTimeoutException:
        print("Timeout error while communicating with the serial port")
    except serial.SerialException as e:
        print("Serial communication error:", e)
    except Exception as e:
        print("Other error:", e)