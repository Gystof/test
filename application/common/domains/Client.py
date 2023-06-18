from dataclasses import dataclass
from datetime import datetime


@dataclass
class CLient:
    id: int
    email: str
    tariff: str
    created_at: datetime = datetime.now()

    @property
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'tariff': self.tariff,
            'created_at': self.created_at
        }

