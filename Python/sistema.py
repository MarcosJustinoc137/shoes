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


# ==========================================
# REGISTRAR PEDIDO
# ==========================================

def registrar_pedido():
    costura_id = int(input("Digite o ID da costura: "))
    quantidade = int(input("Digite a quantidade de pares: "))

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO request 
        (customer_seam_id, amount)
    VALUES 
        (%s,%s);
    """,(costura_id, quantidade))

    conn.commit()

    cur.close()
    conn.close()
    print("Pedido registrado com sucesso!")


# ==========================================
# CONSULTAR PEDIDOS
# ==========================================


def consultar_pedidos():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    SELECT 
        request.id_request,
        customer.customer_name,
        customer_seam.name_seam,
        request.date_request,
        request.amount
    FROM request
    INNER JOIN customer_seam ON request.customer_seam_id = customer_seam.id_customer_seam
    INNER JOIN customer ON customer_seam.customer_id = customer.id_customer
    ORDER BY request.id_request;
""")

    pedidos = cur.fetchall()

    for valor in pedidos:
        print(
            f"ID: {valor[0]} | "
            f"Nome: {valor[1]} | " 
            f"Tipo de costura: {valor[2]} | "
            f"Data: {valor[3]} | "
            f"Pares: {valor[4]}"
        )

    cur.close()
    conn.close()


# ==========================================
# CALCULAR VALORES
# ==========================================


def calcular_valores():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            customer.customer_name,
            customer_seam.name_seam,
            customer_seam.valor,
            request.amount,
            customer_seam.valor * request.amount AS valor_total
        FROM
            request
        INNER JOIN customer_seam ON request.customer_seam_id = customer_seam.id_customer_seam
        INNER JOIN customer ON customer_seam.customer_id = customer.id_customer
        ORDER BY customer.customer_name;
    """)

    valor_final = cur.fetchall()

    for valor in valor_final:
        print(
            f"Cliente: {valor[0]} | "
            f"Tipo de Costura: {valor[1]} | "
            f"Valor por par: R$ {valor[2]:2f} | "
            f"Pares: {valor[3]} | "
            f"Total a pagar: R$ {valor[4]:2f}"
            )

    cur.close()
    conn.close()

calcular_valores()