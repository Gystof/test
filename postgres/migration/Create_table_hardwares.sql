CREATE TABLE IF NOT EXISTS hardwares (
    hardware_id SERIAL PRIMARY KEY,
    cpu CHAR NOT NULL,
    capacity_ram INT NOT NULL,
    capacity_disk INT NOT NULL,
    os CHAR NOT NULL,
    status TEXT
);

COMMENT IN COLUMN servers.servers_id  IS 'Идентификатор сервера';
COMMENT IN COLUMN servers.cpu  IS 'процессор сервера';
COMMENT IN COLUMN servers.capacity_ram  IS 'Количество оперативной памяти';
COMMENT IN COLUMN servers.capacity_disk  IS 'Вместимость диска';
COMMENT IN COLUMN servers.os  IS 'Операционная система';
COMMENT IN COLUMN servers.status  IS 'статус сервера';
