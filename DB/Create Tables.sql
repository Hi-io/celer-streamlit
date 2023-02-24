USE celer_db;

CREATE TABLE IF NOT EXISTS solutions (
    id INT NOT NULL AUTO_INCREMENT,
    user VARCHAR(255) NOT NULL,
    platform VARCHAR(50) NOT NULL,
    msg TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS answers (
    id INT NOT NULL AUTO_INCREMENT,
    id_solution INT NOT NULL,
    answer TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (id_solution) REFERENCES solutions(id)
);