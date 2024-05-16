import mysql.connector as MySQLdb
from PySide6.QtWidgets import QTableWidgetItem

class managerDataBase:
    def __init__(self):
        self.connection = MySQLdb.connect(
            host="localhost",
            user="root",
            passwd="Airtemp"
        )
        self.database = "AtlasRack"

        with self.connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database};")
            cursor.execute(f"USE {self.database};")

        self.CreateTable()
        self.CreateTableMaster()
        self.CreateTableData("BackUp")

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()

    def connect(self):
        if not self.connection.is_connected():
            self.connection.connect()

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
    def CreateTable(self):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = f"CREATE TABLE IF NOT EXISTS Atlas(" \
                  "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT," \
                  "Nserie VARCHAR(40) NOT NULL," \
                  "Code VARCHAR(40) NOT NULL," \
                  "date DATETIME DEFAULT current_timestamp," \
                  "f_etiqueta VARCHAR(12) NOT NULL);"
            cursor.execute(sql)
            self.connection.commit()
    def CreateTableMaster(self):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = f"CREATE TABLE IF NOT EXISTS atlas_master(" \
                  "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT," \
                  "SerialMaster VARCHAR(40) NOT NULL," \
                  "cantidadRack VARCHAR(40) NOT NULL," \
                  "ordnt VARCHAR(40) NOT NULL," \
                  "fcreate VARCHAR(40) NOT NULL," \
                  "fproduction VARCHAR(40) NOT NULL," \
                  "status VARCHAR(20) NOT NULL);"
            cursor.execute(sql)
            self.connection.commit()
    def addMaster(self, Serial, cantidadRack, OT, fcreacion, fproduccion, status):
        self.connect()
        with self.connection.cursor() as cursor:
            insert = f"INSERT INTO atlas_master (SerialMaster, cantidadRack, ordnt, fcreate, fproduction,status) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (Serial, cantidadRack, OT, fcreacion, fproduccion, status)
            cursor.execute(insert, values)
            self.connection.commit()
    def addModule(self, nSerie, nCode, Fetiqueta):
        self.connect()
        with self.connection.cursor() as cursor:
            insert = f"INSERT INTO atlas (NSerie, Code, f_etiqueta) VALUES (%s, %s, %s)"
            values = (nSerie, nCode, Fetiqueta)
            cursor.execute(insert, values)
            self.connection.commit()
    def Check_nCode(self, nCode):
        self.connect()
        with self.connection.cursor() as cursor:
            check_query = f"SELECT COUNT(*) FROM atlas WHERE Code = %s"
            cursor.execute(check_query, (nCode,))
            count = cursor.fetchone()[0]
            return count > 0
    def InsertinTable(self, req, table, qty):
        print("insertamos datos en tabla")
        self.connect()
        if req == 1:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM atlas ORDER BY id DESC LIMIT {qty}")
                # Limpia la tabla
                table.clearContents()
                table.setRowCount(0)
                index = 0

                for row in cursor.fetchall():
                    ids, NSerie, Code, date, f_etiqueta = row
                    # Ahora organizar los datos en la tabla creada anteriormente
                    table.setRowCount(index + 1)
                    table.setItem(index, 0, QTableWidgetItem(str(ids)))
                    table.setItem(index, 1, QTableWidgetItem(str(NSerie)))
                    table.setItem(index, 2, QTableWidgetItem(str(Code)))
                    table.setItem(index, 3, QTableWidgetItem(str(date)))
                    table.setItem(index, 4, QTableWidgetItem(str(f_etiqueta)))
                    index += 1

                self.invertir_tabla(table)
        elif req == 2:
            with self.connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM atlas_master ORDER BY id DESC LIMIT {qty}")
                # Limpia la tabla
                table.clearContents()
                table.setRowCount(0)
                index = 0

                for row in cursor.fetchall():
                    ids, Serial, CantidadRack, OT, fcreacion, fproduccion, status = row
                    # Ahora organizar los datos en la tabla creada anteriormente
                    table.setRowCount(index + 1)
                    table.setItem(index, 0, QTableWidgetItem(str(ids)))
                    table.setItem(index, 1, QTableWidgetItem(str(Serial)))
                    table.setItem(index, 2, QTableWidgetItem(str(CantidadRack)))
                    table.setItem(index, 3, QTableWidgetItem(str(OT)))
                    table.setItem(index, 4, QTableWidgetItem(str(fcreacion)))
                    table.setItem(index, 5, QTableWidgetItem(str(fproduccion)))
                    table.setItem(index, 6, QTableWidgetItem(str(status)))
                    index += 1

                self.invertir_tabla(table)
    def invertir_tabla(self, tabla):
        row_count = tabla.rowCount()
        for i in range(row_count // 2):
            top_row = []
            bottom_row = []

            # Copia los datos de la fila superior
            for column in range(tabla.columnCount()):
                item = tabla.takeItem(i, column)
                if item is not None:
                    top_row.append(item)

            # Copia los datos de la fila inferior
            for column in range(tabla.columnCount()):
                item = tabla.takeItem(row_count - 1 - i, column)
                if item is not None:
                    bottom_row.append(item)

            # Intercambia los datos entre la fila superior y la fila inferior
            for column in range(tabla.columnCount()):
                if top_row:
                    tabla.setItem(row_count - 1 - i, column, top_row.pop(0))
                if bottom_row:
                    tabla.setItem(i, column, bottom_row.pop(0))
    def CreateTableData(self, table):
        self.connect()
        with self.connection.cursor() as cursor:
            sql = f"CREATE TABLE IF NOT EXISTS {table}(" \
                  "id INT UNSIGNED PRIMARY KEY," \
                  "PartNo VARCHAR(40) NOT NULL," \
                  "Supplier VARCHAR(40) NOT NULL," \
                  "OT VARCHAR(40) NOT NULL," \
                  "PzsTotales VARCHAR(40) NOT NULL," \
                  "PzsRealizadas VARCHAR(40) NOT NULL," \
                  "SerialNum VARCHAR(255) NOT NULL," \
                  "FechaCreacion VARCHAR(255) NOT NULL);"
            cursor.execute(sql)
            # Insertar un registro con ID 1 si la tabla es recién creada
            sql_insert_record = f"INSERT IGNORE INTO  {table} (id, PartNo, Supplier, OT, PzsTotales, PzsRealizadas, SerialNum, FechaCreacion)" \
                                "VALUES (1, '3QF121257E', '6001003941', '162555', '10', '0', '180210052024151305', '0')"
            cursor.execute(sql_insert_record)
            self.connection.commit()
    def updateData(self, PartNo, Supplier, OT, PzsTotales, PzsRealizadas, SerialNum, Fcreacion):
        self.connect()
        with self.connection.cursor() as cursor:
            # Definir la tabla y las columnas que deseas actualizar
            table = "backup"
            columnas = ["PartNo", "Supplier", "OT", "PzsTotales", "PzsRealizadas", "SerialNum","FechaCreacion"]

            # Nuevos valores para cada columna
            nuevos_valores = {
                "PartNo": PartNo,
                "Supplier": Supplier,
                "OT": OT,
                "PzsTotales": PzsTotales,
                "PzsRealizadas": PzsRealizadas,
                "SerialNum": SerialNum,
                "FechaCreacion": Fcreacion
            }

            # Actualizar cada columna
            for columna in columnas:
                nuevo_valor = nuevos_valores[columna]
                sql = f"UPDATE {table} SET {columna} = %s"
                cursor.execute(sql, (nuevo_valor,))

            # Confirmar la actualización
            self.connection.commit()
    def GetDataBackUp(self):
        self.connect()
        with self.connection.cursor() as cursor:
            query = f"SELECT * FROM backup WHERE id = %s"
            cursor.execute(query, (1,))
            result = cursor.fetchone()

            if result:
                # Convertir la tupla a una lista antes de devolverla
                return list(result)
            else:
                return None

    def GetDataMaster(self, serial):
        self.connect()
        with self.connection.cursor() as cursor:
            query = f"SELECT * FROM atlas_master WHERE SerialMaster = %s"
            cursor.execute(query, (serial,))
            result = cursor.fetchone()

            if result:
                # Convertir la tupla a una lista antes de devolverla
                return list(result)
            else:
                return None

    def GetSerialMaster(self, tabla):
        self.connect()
        with self.connection.cursor() as cursor:
            query = f"SELECT SerialMaster FROM {tabla}"
            # Ejecutar la consulta
            cursor.execute(query)

            # Obtener todos los resultados y almacenarlos en una lista
            resultados = [registro[0] for registro in cursor.fetchall()]
            cursor.close()
            return resultados

    def GetOTMaster(self, tabla):
        self.connect()
        with self.connection.cursor() as cursor:
            try:
                query = f"SELECT ordnt FROM {tabla}"
                # Ejecutar la consulta
                cursor.execute(query)

                # Utilizar un conjunto para almacenar valores únicos
                resultados_set = set()
                for registro in cursor.fetchall():
                    resultados_set.add(registro[0])

                # Convertir el conjunto a una lista (elimina duplicados)
                resultados = list(resultados_set)

                # Cerrar el cursor
                cursor.close()

                return resultados

            except Exception as e:
                print(f"Error al ejecutar la consulta: {e}")
                return []
