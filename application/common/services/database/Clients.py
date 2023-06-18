from typing import List, Dict
from datetime import datetime
from application.common.domains import Client


class Clients:
    def __init__(self, connection):
        self.__connection = connection

    @staticmethod
    def __map(record: Dict) -> Client:
        return Client(
            id=record.get('id'),
            email=record.get('email'),
            tariff=record.get('tariff'),
            created_at=datetime.fromtimestamp(record.get('created_at'))            
        )

    def all(self) -> List[Client] | List:
        cur = self.__connection.cursor()
        data = list()
        cur.execute('SELECT id, email, tariff, created_at FROM regions')
        for item in cur.fetchall():
            id, email, created_at, tariff = item
            data.append(Client(
                id=id,
                email=email,
                created_at=created_at,
                tariff=tariff
            ))
        cur.close()
        return data

    def find_by_id(self, id: int) -> Client | None:
        cur = self.__connection.cursor()
        cur.execute('SELECT id, email, tariff, created_at FROM regions WHERE id = %s', (id,))
        item = cur.fetchone()
        cur.close()
        if not item:
            return
        id, email, created_at, tariff = item
        return Client(
            id=id,
            email=email,
            tariff=tariff,
            created_at=created_at
        )

    def save(self, item: Client) -> Dict | None:
        email = item.email
        id = item.id
        errors = dict()
        cur = self.__connection.cursor()
        cur.execute('INSERT INTO client (email) VALUES (%s)', (email,))
        self.__connection.commit()
        cur.close()
        return errors
        # print(item)
        # if not id:
        #     last_id = 0
        #     if self.__data:
        #         last_id = max(self.__data.keys())
        #     id = last_id + 1
        #     check = list(filter(lambda record: record.get('email') == email, self.__data.values()))
        #     if check:
        #         errors['email'] = 'Запись с таким именем уже существует'
        # elif id not in self.__data:
        #     errors['id'] = 'Запись с данным ID не найдена'
        # else:
        #     check = list(filter(lambda record: record.get('email') == email and record.get('id') != id,
        #                         self.__data.values()))
        #     if check:
        #         errors['email'] = 'Запись с таким именем уже существует'
        #     item.tariff = datetime.now()
        # if errors:
        #     return errors
        # self.__data[id] = {
        #     'id': id,
        #     'email': email,
        #     'created_at': int(datetime.timestamp(item.created_at)),
        #     'tariff': int(datetime.timestamp(item.tariff))
        # }

    def delete(self, item: Client):
        if item.id in self.__data:
            del self.__data[item.id]
