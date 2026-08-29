from conexao import conectar

        #Cadastrar cliente
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

cadastrar_cliente()


