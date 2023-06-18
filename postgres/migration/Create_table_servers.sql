CREATE TABLE IF NOT EXISTS servers (
    server_id SERIAL PRIMARY KEY,
    hardware INT NOT NULL,
    ip CHAR NOT NULL,
    os CHAR NOT NULL
);

COMMENT IN COLUMN servers.servers_id  IS 'Идентификатор сервера';
COMMENT IN COLUMN servers.hardware  IS 'ПК на котором запущен сервер';
COMMENT IN COLUMN servers.ip  IS 'IP-адрес сервера';
COMMENT IN COLUMN servers.os  IS 'Операционная система';

