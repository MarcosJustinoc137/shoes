from conexao import conectar

# ==========================================
# Cadastrar pedidos
# ==========================================

def registrar_pedido():
    costura_id = int(input("Digite o ID da costura (Digite 0 para cancelar): "))
    if costura_id == 0:
            print("Pedido cancelado")
            return
    quantidade = int(input("Digite a quantidade de pares: "))
    if quantidade == 0:
        print("Pedido cancelado")
        return

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
            f"Pares: {valor[4]}")

    cur.close()
    conn.close()