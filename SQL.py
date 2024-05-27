import mysql.connector as MySQLdb
from mysql.connector import Error
from PySide6.QtWidgets import QTableWidgetItem

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
        if self.connection is None or not self.connection.is_connected():
            try:
                self.connection = MySQLdb.connect(
                    host=self.db_config['host'],
                    user=self.db_config['user'],
                    passwd=self.db_config['passwd']
                )
                with self.connection.cursor() as cursor:
                    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_config['db']};")
                    cursor.execute(f"USE {self.db_config['db']};")
            except Error as e:
                print(f"Error connecting to database: {e}")
                self.connection = None
            else:
                print("Successfully connected to the database")

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None

    def reconnect_if_needed(self):
        if self.connection is None or not self.connection.is_connected():
            self.connect()

    def execute_query(self, query, values=None):
        self.reconnect_if_needed()
        if self.connection:
            try:
                with self.connection.cursor(buffered=True) as cursor:
                    cursor.execute(query, values)
                    self.connection.commit()
                    return cursor
            except Error as e:
                print(f"Error executing query: {e}")
                # Ensure there are no unread results before reconnecting
                self.connection.reset_session()
                self.connect()
                return None
        return None

    def CreateTable(self):
        self.execute_query(
            "CREATE TABLE IF NOT EXISTS Atlas ("
            "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, "
            "Nserie VARCHAR(40) NOT NULL, "
            "Code VARCHAR(40) NOT NULL, "
            "date DATETIME DEFAULT current_timestamp, "
            "f_etiqueta VARCHAR(12) NOT NULL);"
        )

    def CreateTableMaster(self):
        self.execute_query(
            "CREATE TABLE IF NOT EXISTS atlas_master ("
            "id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, "
            "SerialMaster VARCHAR(40) NOT NULL, "
            "cantidadRack VARCHAR(40) NOT NULL, "
            "ordnt VARCHAR(40) NOT NULL, "
            "fcreate VARCHAR(40) NOT NULL, "
            "fproduction VARCHAR(40) NOT NULL, "
            "status VARCHAR(20) NOT NULL);"
        )

    def addMaster(self, Serial, cantidadRack, OT, fcreacion, fproduccion, status):
        self.execute_query(
            "INSERT INTO atlas_master (SerialMaster, cantidadRack, ordnt, fcreate, fproduction, status) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (Serial, cantidadRack, OT, fcreacion, fproduccion, status)
        )

    def addModule(self, nSerie, nCode, Fetiqueta):
        self.execute_query(
            "INSERT INTO atlas (NSerie, Code, f_etiqueta) VALUES (%s, %s, %s)",
            (nSerie, nCode, Fetiqueta)
        )

    def Check_nCode(self, nCode):
        cursor = self.execute_query(
            "SELECT COUNT(*) FROM atlas WHERE Code = %s",
            (nCode,)
        )
        if cursor:
            count = cursor.fetchone()[0]
            return count > 0
        return False

    def InsertinTable(self, req, table, qty):
        print("Insertando datos en tabla")
        if req == 1:
            query = f"SELECT * FROM atlas ORDER BY id DESC LIMIT {qty}"
        elif req == 2:
            query = f"SELECT * FROM atlas_master ORDER BY id DESC LIMIT {qty}"
        else:
            print("Solicitud no válida")
            return

        cursor = self.execute_query(query)
        if cursor:
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
        self.execute_query(
            f"CREATE TABLE IF NOT EXISTS {table} ("
            "id INT UNSIGNED PRIMARY KEY, "
            "PartNo VARCHAR(40) NOT NULL, "
            "Supplier VARCHAR(40) NOT NULL, "
            "OT VARCHAR(40) NOT NULL, "
            "PzsTotales VARCHAR(40) NOT NULL, "
            "PzsRealizadas VARCHAR(40) NOT NULL, "
            "SerialNum VARCHAR(255) NOT NULL, "
            "FechaCreacion VARCHAR(255) NOT NULL);"
        )
        self.execute_query(
            f"INSERT IGNORE INTO {table} "
            "(id, PartNo, Supplier, OT, PzsTotales, PzsRealizadas, SerialNum, FechaCreacion) "
            "VALUES (1, '3QF121257E', '6001003941', '162555', '10', '0', '180210052024151305', '0')"
        )

    def updateData(self, PartNo, Supplier, OT, PzsTotales, PzsRealizadas, SerialNum, Fcreacion):
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
            self.execute_query(
                f"UPDATE {table} SET {columna} = %s",
                (nuevo_valor,)
            )

    def GetDataBackUp(self):
        cursor = self.execute_query(
            "SELECT * FROM backup WHERE id = %s",
            (1,)
        )
        if cursor:
            result = cursor.fetchone()
            if result:
                return list(result)
        return None

    def GetDataMaster(self, serial):
        cursor = self.execute_query(
            "SELECT * FROM atlas_master WHERE SerialMaster = %s",
            (serial,)
        )
        if cursor:
            result = cursor.fetchone()
            if result:
                return list(result)
        return None

    def GetSerialMaster(self, tabla):
        cursor = self.execute_query(
            f"SELECT SerialMaster FROM {tabla}"
        )
        if cursor:
            return [registro[0] for registro in cursor.fetchall()]
        return []

    def GetOTMaster(self, tabla):
        cursor = self.execute_query(
            f"SELECT ordnt FROM {tabla}"
        )
        if cursor:
            try:
                resultados_set = set(registro[0] for registro in cursor.fetchall())
                return list(resultados_set)
            except Exception as e:
                print(f"Error al ejecutar la consulta: {e}")
        return []
