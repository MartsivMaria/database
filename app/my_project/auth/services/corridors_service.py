from dao.corridors_dao import CorridorsDAO

class CorridorsService:
    def __init__(self, mysql):
        self.dao = CorridorsDAO(mysql)

    def get_corridors(self):
        return self.dao.get_all_corridors()

    def add_corridors(self, corridors):
        return self.dao.insert_corridors(corridors)

    def modify_corridors(self, corridor_id, corridors):
        return self.dao.update_corridors(corridor_id, corridors)

    def remove_corridors(self, corridor_id):
        return self.dao.delete_corridors(corridor_id)
