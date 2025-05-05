from database.DB_connect import DBConnect
from model.arco import Arco
from model.artObject import ArtObject


class DAO:
    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select *
                from objects o"""
        cursor.execute(query)

        for row in cursor:
            result.append(ArtObject(**row))

        cursor.close()
        conn.close()

        return result

    @staticmethod
    def getPeso(v1, v2):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select eo.object_id, eo2.object_id, count(*) as peso
                    from exhibition_objects eo, exhibition_objects eo2  # prendo due istanze e confronto le righe
                    where eo.exhibition_id = eo2.exhibition_id 
                    and eo.object_id < eo2.object_id # mi toglie un senso degli archi e anche il caso in cui sono uguali
                    and eo.object_id = %s and eo2.object_id = %s
                    group by eo.object_id, eo2.object_id"""

        cursor.execute(query, (v1.object_id, v2.object_id))

        for row in cursor:
            result.append(row["peso"])

        cursor.close()
        conn.close()

        if len(result) == 0:
            return None

        return result

    @staticmethod
    def getAllArchi(idMap):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        result = []
        query = """select eo.object_id as o1, eo2.object_id as o2, count(*) as peso
                    from exhibition_objects eo, exhibition_objects eo2  # prendo due istanze e confronto le righe
                    where eo.exhibition_id = eo2.exhibition_id 
                    and eo.object_id < eo2.object_id # mi toglie un senso degli archi e anche il caso in cui sono uguali
                    group by eo.object_id, eo2.object_id
                    order by peso desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(Arco(idMap[row["o1"]], idMap[row["o2"]], row["peso"]))

        cursor.close()
        conn.close()

        if len(result) == 0:
            return None

        return result
