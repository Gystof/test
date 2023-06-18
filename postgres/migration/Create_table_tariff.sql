CREATE TABLE IF NOT EXISTS tariff (
    tariff_id SERIAL PRIMARY KEY,
    price INT NOT NULL,
    type_name TEXT NOT NULL,
    server INT NOT NULL,
    FOREIGN KEY (server) REFERENCES servers(servers_id)
);

COMMENT IN COLUMN tariff.tariff_id  IS 'Идентификатор тарифа';
COMMENT IN COLUMN tariff.price  IS 'Цена тарифа';
COMMENT IN COLUMN tariff.type_name  IS 'Название тарифа';
COMMENT IN COLUMN tariff.server IS 'Используемый сервер';