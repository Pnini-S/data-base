from db_api import *
import csv


class MyDBTable(DBTable):
    def __init__(self, name: str, field: List[DBField], key_field_name: str):
        self.name = name
        self.fields = field[:]
        self.key_field_name = key_field_name
        self.counterRecords = 0
        self.file = f'{name}.csv'
        with open(self.file, "w") as csv_file:
            csv_writer = csv.writer(csv)
            # writes the title
            csv_writer.writerow([i.name for i in self.fields])

        '''where I make files?'''

    #def search(self, key: Any) -> int:



    def count(self) -> int:
        return self.counterRecords
        # raise NotImplementedError

    def insert_record(self, values: Dict[str, Any]) -> None:
        with open(self.file, "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            # writes the row
            csv_writer.writerow(values.values())

        #raise NotImplementedError

    def delete_record(self, key: Any) -> None:
        raise NotImplementedError

    def delete_records(self, criteria: List[SelectionCriteria]) -> None:
        raise NotImplementedError

    def get_record(self, key: Any) -> Dict[str, Any]:
        raise NotImplementedError

    def update_record(self, key: Any, values: Dict[str, Any]) -> None:
        raise NotImplementedError

    def query_table(self, criteria: List[SelectionCriteria]) \
            -> List[Dict[str, Any]]:
        raise NotImplementedError

    def create_index(self, field_to_index: str) -> None:
        raise NotImplementedError


fiel1 = DBField("name", str)
fiel2 = DBField("age", int)
fiel3 = DBField("id", int)


table = MyDBTable("Person", [fiel1, fiel2, fiel3], "id")
table.insert_record({"name": "Pnini", "age": 20, "id": 315437145})
table.insert_record({"name": "Shira", "age": 20, "id": 211426754})

