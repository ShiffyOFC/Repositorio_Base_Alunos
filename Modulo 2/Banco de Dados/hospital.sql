CREATE TABLE IF NOT EXISTS medico (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            VARCHAR(190),
    crm             VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS paciente (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    nome            VARCHAR(190),
    cpf             VARCHAR(12)
);

CREATE TABLE IF NOT EXISTS consulta (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    idMedico        INTEGER,
    idPaciente      INTEGER,
    dataConsulta    DATE,
    FOREIGN KEY (idMedico) REFERENCES medico(id),
    FOREIGN KEY (idPaciente) REFERENCES paciente(id)
);

INSERT INTO medico (nome, crm) VALUES 
('Clara', '1234.5678.910'),
('Analy', '1098.7654.321');

INSERT INTO paciente (nome, cpf) VALUES
('Gustavo', 'XXX.XXX.XXX-XX'),
('João', 'XXX.XXX.XXX-XX'),
('Anthony', 'XXX.XXX.XXX-XX'),
('Marcos', 'XXX.XXX.XXX-XX');

INSERT INTO consulta(idMedico, idPaciente, dataConsulta) VALUES
(1, 4, date('now')),
(2, 2, date('now')),
(2, 3, date('now'));