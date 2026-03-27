CREATE TABLE IF NOT EXISTS ativos (
    id INTEGER PRIMARY KEY NOT NULL,
    ativo TEXT NOT NULL,
    created_at DATA
);

CREATE TABLE IF NOT EXISTS dados_ativos (
    id_dados_ativos INTEGER PRIMARY KEY NOT NULL,
    id_ativos INTEGER,
    data_negociacao DATE,
    preco_ajustado INTEGER,
    retorno_diario INTEGER,
    created_at DATA,
    FOREIGN KEY (id_ativos) REFERENCES ativos(id)
);