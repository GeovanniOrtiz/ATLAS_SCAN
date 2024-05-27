#import mysql.connector as MySQLdb
from PySide6.QtWidgets import QTableWidgetItem
import MySQLdb

class managerDataBase:
    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': 'Airtemp',
            'db': 'AtlasRack'
        }
        self.connection = None
        self.connect()

        self.CreateTable()
        self.CreateTableMaster()
        self.CreateTableData("BackUp")

    def connect(self):
        if self.connection is None or not self.connection.open:
            self.connection = MySQLdb.connect(
                host=self.db_config['host'],
                user=self.db_config['user'],
                passwd=self.db_config['passwd']
            )
            with self.connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['db']};")
                cursor.execute(f"USE {self.db_config['db']};")

    def disconnect(self):
        if self.connection and self.connection.open:
            self.connection.close()
            self.connection = None

    def CreateTable(self):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = ("CREATE TABLE IF NOT EXISTS Atlas ("
                   "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, "
                   "Nserie VARCHAR(40) NOT NULL, "
                   "Code VARCHAR(40) NOT NULL, "
                   "date DATETIME DEFAULT current_timestamp, "
                   "f_etiqueta VARCHAR(12) NOT NULL);")
            cursor.execute(sql)
            self.connection.commit()

    def CreateTableMaster(self):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = ("CREATE TABLE IF NOT EXISTS atlas_master ("
                   "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, "
                   "SerialMaster VARCHAR(40) NOT NULL, "
                   "cantidadRack VARCHAR(40) NOT NULL, "
                   "ordnt VARCHAR(40) NOT NULL, "
                   "fcreate VARCHAR(40) NOT NULL, "
                   "fproduction VARCHAR(40) NOT NULL, "
                   "status VARCHAR(20) NOT NULL);")
            cursor.execute(sql)
            self.connection.commit()

    def addMaster(self, Serial, cantidadRack, OT, fcreacion, fproduccion, status):
        self.connect()
        with self.connection.cursor() as cursor:
            insert = ("INSERT INTO atlas_master (SerialMaster, cantidadRack, ordnt, fcreate, fproduction, status) "
                      "VALUES (%s, %s, %s, %s, %s, %s)")
            values = (Serial, cantidadRack, OT, fcreacion, fproduccion, status)
            cursor.execute(insert, values)
            self.connection.commit()

    def addModule(self, nSerie, nCode, Fetiqueta):
        self.connect()
        with self.connection.cursor() as cursor:
            insert = ("INSERT INTO atlas (NSerie, Code, f_etiqueta) VALUES (%s, %s, %s)")
            values = (nSerie, nCode, Fetiqueta)
            cursor.execute(insert, values)
            self.connection.commit()

    def Check_nCode(self, nCode):
        self.connect()
        with self.connection.cursor() as cursor:
            check_query = "SELECT COUNT(*) FROM atlas WHERE Code = %s"
            cursor.execute(check_query, (nCode,))
            count = cursor.fetchone()[0]
            return count > 0

    def InsertinTable(self, req, table, qty):
        print("Insertando datos en tabla")
        self.connect()
        if req == 1:
            query = f"SELECT * FROM atlas ORDER BY id DESC LIMIT {qty}"
        elif req == 2:
            query = f"SELECT * FROM atlas_master ORDER BY id DESC LIMIT {qty}"
        else:
            print("Solicitud no válida")
            return

        with self.connection.cursor() as cursor:
            cursor.execute(query)
            table.clearContents()
            table.setRowCount(0)
            index = 0

            for row in cursor.fetchall():
                table.setRowCount(index + 1)
                for col, value in enumerate(row):
                    table.setItem(index, col, QTableWidgetItem(str(value)))
                index += 1

            self.invertir_tabla(table)

    def invertir_tabla(self, tabla):
        row_count = tabla.rowCount()
        for i in range(row_count // 2):
            top_row = []
            bottom_row = []

            for column in range(tabla.columnCount()):
                item = tabla.takeItem(i, column)
                if item is not None:
                    top_row.append(item)

            for column in range(tabla.columnCount()):
                item = tabla.takeItem(row_count - 1 - i, column)
                if item is not None:
                    bottom_row.append(item)

            for column in range(tabla.columnCount()):
                if top_row:
                    tabla.setItem(row_count - 1 - i, column, top_row.pop(0))
                if bottom_row:
                    tabla.setItem(i, column, bottom_row.pop(0))

    def CreateTableData(self, table):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = (f"CREATE TABLE IF NOT EXISTS {table} ("
                   "id INT UNSIGNED PRIMARY KEY, "
                   "PartNo VARCHAR(40) NOT NULL, "
                   "Supplier VARCHAR(40) NOT NULL, "
                   "OT VARCHAR(40) NOT NULL, "
                   "PzsTotales VARCHAR(40) NOT NULL, "
                   "PzsRealizadas VARCHAR(40) NOT NULL, "
                   "SerialNum VARCHAR(255) NOT NULL, "
                   "FechaCreacion VARCHAR(255) NOT NULL);")
            cursor.execute(sql)
            sql_insert_record = (f"INSERT IGNORE INTO {table} "
                                 "(id, PartNo, Supplier, OT, PzsTotales, PzsRealizadas, SerialNum, FechaCreacion) "
                                 "VALUES (1, '3QF121257E', '6001003941', '162555', '10', '0', '180210052024151305', '0')")
            cursor.execute(sql_insert_record)
            self.connection.commit()

    def updateData(self, PartNo, Supplier, OT, PzsTotales, PzsRealizadas, SerialNum, Fcreacion):
        self.connect()
        with self.connection.cursor() as cursor:
            table = "backup"
            columnas = ["PartNo", "Supplier", "OT", "PzsTotales", "PzsRealizadas", "SerialNum", "FechaCreacion"]
            nuevos_valores = {
                "PartNo": PartNo,
                "Supplier": Supplier,
                "OT": OT,
                "PzsTotales": PzsTotales,
                "PzsRealizadas": PzsRealizadas,
                "SerialNum": SerialNum,
                "FechaCreacion": Fcreacion
            }

            for columna in columnas:
                nuevo_valor = nuevos_valores[columna]
                sql = f"UPDATE {table} SET {columna} = %s"
                cursor.execute(sql, (nuevo_valor,))

            self.connection.commit()

    def GetDataBackUp(self):
        self.connect()
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM backup WHERE id = %s"
            cursor.execute(query, (1,))
            result = cursor.fetchone()

            if result:
                return list(result)
            else:
                return None

    def GetDataMaster(self, serial):
        self.connect()
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM atlas_master WHERE SerialMaster = %s"
            cursor.execute(query, (serial,))
            result = cursor.fetchone()

            if result:
                return list(result)
            else:
                return None

    def GetSerialMaster(self, tabla):
        self.connect()
        with self.connection.cursor() as cursor:
            query = f"SELECT SerialMaster FROM {tabla}"
            cursor.execute(query)
            resultados = [registro[0] for registro in cursor.fetchall()]
            return resultados

    def GetOTMaster(self, tabla):
        self.connect()
        with self.connection.cursor() as cursor:
            try:
                query = f"SELECT ordnt FROM {tabla}"
                cursor.execute(query)
                resultados_set = set(registro[0] for registro in cursor.fetchall())
                return list(resultados_set)
            except Exception as e:
                print(f"Error al ejecutar la consulta: {e}")
                return []
