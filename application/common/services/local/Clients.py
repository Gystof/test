from typing import List, Dict
from datetime import datetime
from application.common.domains import Client


class Clients:
    def __init__(self):
        self.__data = {
            1: {
                'id': 1,
                'email': 'example@mail.ru',
                'tariff': 'middle',
                'created_at': 1679700554       
            },
            2: {
                'id': 2,
                'email': 'example@mail.ru',
                'tariff': 'middle',
                'created_at': 1679700554
            }
        }

    @staticmethod
    def __map(record: Dict) -> Client:
        return Client(
            id=record.get('id'),
            email=record.get('email'),
            tariff=record.get('tariff')),
            created_at=datetime.fromtimestamp(record.get('created_at'))
        )


    def all(self) -> List[Client] | List:
        data = list()
        for item in self.__data.values():
            data.append(self.__map(item))
        return data

    def find_by_id(self, id: int) -> Client | None:
        item = self.__data.get(id)
        if not item:
            return
        return self.__map(item)

    def save(self, item: Client) -> Dict | None:
        email = item.email
        id = item.id
        tariff = item.tariff
        errors = dict()
        print(item)
        if not id:
            last_id = 0
            if self.__data:
                last_id = max(self.__data.keys())
            id = last_id + 1
            check = list(filter(lambda record: record.get('email') == email, self.__data.values()))
            if check:
                errors['email'] = 'Запись с таким именем уже существует'
        elif id not in self.__data:
            errors['id'] = 'Запись с данным ID не найдена'
        else:
            check = list(filter(lambda record: record.get('email') == email and record.get('id') != id,
                                self.__data.values()))
            if check:
                errors['email'] = 'Запись с таким именем уже существует'
        if errors:
            return errors
        self.__data[id] = {
            'id': id,
            'email': email,
            'tariff': tariff,
            'created_at': int(datetime.timestamp(item.created_at))    
        }

    def delete(self, item: Client):
        if item.id in self.__data:
            del self.__data[item.id]
