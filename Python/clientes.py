from conexao import conectar

#=====================================
        #Cadastrar cliente
#=====================================


def cadastrar_cliente():

    nome = input("Nome do cliente  (Digite 0 para cancelar): ")
    telefone = input("Telefone: ")
    fabricante = input("Fabricante: ")

    if "0" in (nome, telefone, fabricante):
        print("Cadastro cancelado.")
        return
    
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO customer
        (customer_name, customer_number, maker)
        VALUES (%s, %s, %s)
    """, (nome, telefone, fabricante))

    conn.commit()

    cur.close()
    conn.close()

    print("Cliente cadastrado com sucesso!")


#==========================================
#Consultar Clientes
#==========================================


def consultar_clientes():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            id_customer,
            customer_name,
            customer_number,
            maker
        FROM customer
        ORDER BY id_customer;
    """)

    clientes = cur.fetchall()

    for cliente in clientes:
        print(
            f"ID: {cliente[0]} | "
            f"Nome: {cliente[1]} | "
            f"Telefone: {cliente[2]} | "
            f"Fabrica: {cliente[3]}")

    cur.close()
    conn.close()

