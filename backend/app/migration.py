import psycopg2

migrations = [
   """CREATE TABLE IF NOT EXISTS "disease_type" (id SERIAL, description VARCHAR(50) NOT NULL, PRIMARY KEY (id));""",
    """CREATE TABLE IF NOT EXISTS "country" (
    cname VARCHAR(50) NOT NULL,
    population BIGINT NOT NULL,
    PRIMARY KEY (cname)
);""",
"""CREATE TABLE IF NOT EXISTS "disease" (
    disease_code VARCHAR(50) NOT NULL,
    pathogen VARCHAR(20) NOT NULL,
    description VARCHAR(140) NOT NULL,
    id INTEGER NOT NULL ,
    PRIMARY KEY (disease_code),
    FOREIGN KEY (id) REFERENCES disease_type (id) ON UPDATE CASCADE ON DELETE CASCADE
);""",
"""CREATE TABLE IF NOT EXISTS "discover" (
    cname VARCHAR(50) NOT NULL,
    disease_code VARCHAR(50) NOT NULL,
    first_enc_date DATE NOT NULL,
    PRIMARY KEY (cname, disease_code),
    FOREIGN KEY (cname) REFERENCES country (cname) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (disease_code) REFERENCES disease (disease_code) ON UPDATE CASCADE ON DELETE CASCADE
);""",
"""CREATE TABLE IF NOT EXISTS "users" (
    email VARCHAR(60) NOT NULL,
    name VARCHAR(30) NOT NULL,
    surname VARCHAR(40) NOT NULL,
    salary INTEGER NOT NULL,
    phone VARCHAR(20) NOT NULL,
    cname VARCHAR(50) NOT NULL,
    PRIMARY KEY (email),
    FOREIGN KEY (cname) REFERENCES country (cname) ON UPDATE CASCADE ON DELETE CASCADE
);""",

"""CREATE TABLE IF NOT EXISTS "public_servant" (
    email VARCHAR(60) NOT NULL,
    department VARCHAR(50) NOT NULL,
    PRIMARY KEY (email),
    FOREIGN KEY (email) REFERENCES "users" (email) ON UPDATE CASCADE ON DELETE CASCADE
);""",
"""CREATE TABLE IF NOT EXISTS "doctor" (
    email VARCHAR(60) NOT NULL,
    degree VARCHAR(20) NOT NULL,
    PRIMARY KEY (email),
    FOREIGN KEY (email) REFERENCES "users" (email) ON UPDATE CASCADE ON DELETE CASCADE
);"""
"""CREATE TABLE IF NOT EXISTS "specialize" (
    id INTEGER NOT NULL,
    email VARCHAR(60) NOT NULL,
    PRIMARY KEY (id, email),
    FOREIGN KEY (id) REFERENCES disease_type(id),
    FOREIGN KEY (email) REFERENCES "doctor" (email) ON UPDATE CASCADE ON DELETE CASCADE
);""",

"""CREATE TABLE IF NOT EXISTS "record" (
    email VARCHAR(60) NOT NULL,
    cname VARCHAR(50) NOT NULL,
    disease_code VARCHAR(50) NOT NULL,
    total_deaths INTEGER NOT NULL,
    total_patients INTEGER NOT NULL,
    PRIMARY KEY (email, cname, disease_code),
    FOREIGN KEY (email) REFERENCES "public_servant" (email) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (cname) REFERENCES "country" (cname) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (disease_code) REFERENCES "disease" (disease_code)
);""",
]

def create_tables():
    conn = None
    try:

        # connect to the PostgreSQL server
        conn = psycopg2.connect(host="postgres", database="assignment", user="root", password="password", port="5432", sslmode="disable")
        
        # create table one by one
        for migration in migrations:
            cur = conn.cursor()
            cur.execute(migration)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error,"error")
    finally:
        if conn is not None:
            conn.close()