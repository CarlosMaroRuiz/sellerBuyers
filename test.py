from sqlalchemy import create_engine, inspect

# Conexión a la base de datos
DATABASE_URL = "mysql+pymysql://root:12345678@85.31.235.46:3306/mydb"
engine = create_engine(DATABASE_URL)


def inspect_table_structure(table_name):

    inspector = inspect(engine)
    columns = inspector.get_columns(table_name)
    print(f"Estructura de la tabla '{table_name}':")
    for column in columns:
        print(f"- {column['name']} ({column['type']})")

    # Inspeccionar claves primarias
    primary_keys = inspector.get_pk_constraint(table_name)
    print("\nClaves primarias:")
    print(primary_keys.get('constrained_columns', []))

    # Inspeccionar claves foráneas
    foreign_keys = inspector.get_foreign_keys(table_name)
    print("\nClaves foráneas:")
    for fk in foreign_keys:
        print(f"- {fk['constrained_columns']} -> {fk['referred_table']}({fk['referred_columns']})")
    print("\n" + "-" * 50)


def list_tables():
    """
    Lista todas las tablas en la base de datos y llama a inspect_table_structure para cada una.
    """
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Tablas en la base de datos:", tables)
    for table in tables:
        inspect_table_structure(table)


if __name__ == "__main__":
    list_tables()
