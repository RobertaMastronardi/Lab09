from database.DB_connect import DBConnect
from model.aeroporto import Aeroporto


class DAO():
    @staticmethod
    def get_all_airports():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select * from airports a """
            cursor.execute(query)

            for row in cursor:
                result.append(Aeroporto(**row))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_edges(dist_min, idMapA):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select a.ID as a1 , a2.ID as a2 , SUM(t.distanzatot)/SUM(t.numvoli) as peso
                        from airports a , airports a2 , (select f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID , SUM(f.DISTANCE ) as distanzaTot, COUNT(*) as numVoli
                        from flights f 
                        group by f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID) t
                        where (a.ID=t.ORIGIN_AIRPORT_ID and a2.ID =t.DESTINATION_AIRPORT_ID or a.ID=t.DESTINATION_AIRPORT_ID and a2.ID=t.ORIGIN_AIRPORT_ID ) 
                        and a.ID <a2.ID 
                        group by a.ID , a2.ID 
                        having peso>%s"""
            cursor.execute(query, (dist_min,))

            for row in cursor:
                result.append((idMapA[row["a1"]], idMapA[row["a2"]], row["peso"]))
            cursor.close()
            cnx.close()
        return result

