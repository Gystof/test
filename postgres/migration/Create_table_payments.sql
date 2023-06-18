CREATE TABLE IF NOT EXISTS payments (
    payment_id SERIAL PRIMARY KEY,
    tariff TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tariff) REFERENCES tariff(type_name)
);

COMMENT IN COLUMN payments.payment_id  IS 'Идентификатор оплаты';
COMMENT IN COLUMN payments.tariff  IS 'Выбранный тариф';
COMMENT IN COLUMN payments.created_at  IS 'Дата создания';