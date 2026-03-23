CREATE TABLE IF NOT EXIST ativos (
    id_ativos INTEGER PRIMARY KEY NOT NULL,
    ativo TEXT NOT NULL
);

CREATE TABLE IF NOT EXIST dados_ativos (
    id_dados_ativos INTEGER PRIMARY KEY NOT NULL,
    id_ativos INTEGER FOREIGN KEY,
    preço_ajustado INTEGER,
    retorno_diario INTEGER
)