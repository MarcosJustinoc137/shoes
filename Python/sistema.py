from conexao import conectar

#=====================================
        #Cadastrar cliente
#=====================================


def cadastrar_cliente():

    nome = input("Nome do cliente: ")
    telefone = input("Telefone: ")
    fabricante = input("Fabricante: ")

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
            f"Fabrica: {cliente[3]}"
        )

    cur.close()
    conn.close()


# ==========================================
# CADASTRAR COSTURA PARA UM CLIENTE
# ==========================================



def cadastrar_costura():
    cliente_id = int(input("Digite o ID do cliente: "))
    nome_costura = input("Digite o tipo de costura: ")
    valor = float(input("Digite o valor por par: "))

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO customer_seam
            (customer_id, name_seam, valor)
        VALUES
            (%s, %s, %s);
    """, (cliente_id, nome_costura, valor))

    conn.commit()

    cur.close()
    conn.close()

    print("Costura cadastrada com sucesso!")



# ==========================================
# CONSULTAR COSTURAS
# ==========================================

def consultar_costuras():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            customer_seam.id_customer_seam,
            customer.customer_name,
            customer_seam.name_seam,
            customer_seam.valor
        FROM customer_seam
        INNER JOIN customer
            ON customer.id_customer = customer_seam.customer_id
        ORDER BY customer_seam.id_customer_seam;
    """)

    costuras = cur.fetchall()

    for valor in costuras:
        print(f"ID: {valor[0]} | " 
              f"Cliente: {valor[1]} | "
              f"Costura: {valor[2]} | "
              f"Valor: R${valor[3]:.2f}"
        )

    cur.close()
    conn.close()

consultar_costuras()