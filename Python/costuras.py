
from conexao import conectar

def cadastrar_costura():
    cliente_id = int(input("Digite o ID do cliente (Digite 0 para cancelar): "))
    if cliente_id == 0:
        print("Cadastro cancelado")
        return
    
    nome_costura = input("Digite o tipo de costura: ")
    if nome_costura == "0":
            print("Cadastro cancelado")
            return
    valor = float(input("Digite o valor por par: "))
    if cliente_id == 0:
            print("Cadastro cancelado")
            return

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
              f"Valor: R${valor[3]:.2f}")

    cur.close()
    conn.close()