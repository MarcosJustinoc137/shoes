from conexao import conectar


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
            f"Total a pagar: R$ {valor[4]:2f}")

    cur.close()
    conn.close()


# ==========================================
# CALCULAR VALOR MENSAL/ANUAL
# ==========================================

def relatorio_mensal():

    mes = int(input("Digite o mês (1-12): "))
    ano = int(input("Digite o ano: "))

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            customer.customer_name,
            SUM(request.amount) AS total_pares,
            SUM(customer_seam.valor * request.amount) AS toral_a_pagar
        FROM request
        INNER JOIN customer_seam ON request.customer_seam_id = customer_seam.id_customer_seam
        INNER JOIN customer ON customer_seam.customer_id = customer.id_customer
        WHERE
            EXTRACT(MONTH FROM request.date_request) = %s
            AND EXTRACT(YEAR FROM request.date_request) = %s
        GROUP BY customer.customer_name
        ORDER BY customer.customer_name;""", (mes, ano))



    relatorio = cur.fetchall()

    print(f"\n===== RELATÓRIO {mes:02d}/{ano} =====\n")

    for valor in relatorio:
        print(
            f"Cliente: {valor[0]} | "
            f"Pares: {valor[1]} | "
            f"Total a pagar: R$ {valor[2]:.2f}")

    cur.close()
    conn.close()
