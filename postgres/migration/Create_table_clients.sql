CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    email char(100) NOT NULL,
    tariff TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tariff) REFERENCES tariff(type_name)
);

COMMENT IN COLUMN clients.client_id  IS 'Идентификатор клиента';
COMMENT IN COLUMN clients.email  IS 'Почта';
COMMENT IN COLUMN clients.tariff  IS 'Выбранный тариф';