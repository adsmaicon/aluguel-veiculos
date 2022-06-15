CREATE SCHEMA aluguel;

CREATE TABLE veiculo (
	id int auto_increment not null,
    placa char(7),
    km FLOAT,
    carga FLOAT,
    bagageiro int,
    portas int,
    tipo ENUM('automovel', 'caminhao') default 'automovel',
    primary key (id)
);