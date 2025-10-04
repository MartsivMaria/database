from ..models.corridors import Corridors

class CorridorsDAO:
    def __init__(self, mysql):
        self.mysql = mysql

    def get_all_corridors(self):
        cur = self.mysql.connection.cursor()
        cur.execute("SELECT * FROM corridors")
        corridors = cur.fetchall()
        cur.close()
        return [Corridors(corridor_id=row[0], object_id=row[1], name=row[2]) for row in corridors]
    
    # Insert operation, will be blocked by MySQL trigger
    def insert_corridors(self, corridors):
        cur = self.mysql.connection.cursor()
        cur.execute("INSERT INTO corridors (corridor_id, object_id, name) VALUES (%s, %s, %s)", 
                    (corridors['corridor_id'], corridors['object_id'], corridors['name']))
        self.mysql.connection.commit()
        cur.close()

    # Update operation, will be blocked by MySQL trigger
    def update_corridors(self, corridor_id, corridors):
        cur = self.mysql.connection.cursor()
        cur.execute("UPDATE corridors SET object_id = %s, name = %s WHERE corridor_id = %s", 
                    (corridors['object_id'], corridors['name'], corridor_id))
        self.mysql.connection.commit()
        cur.close()

    # Delete operation, will be blocked by MySQL trigger
    def delete_corridors(self, corridor_id):
        cur = self.mysql.connection.cursor()
        cur.execute("DELETE FROM corridors WHERE corridor_id = %s", (corridor_id,))
        self.mysql.connection.commit()
        cur.close()

