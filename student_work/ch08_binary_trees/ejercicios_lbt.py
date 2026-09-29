from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    queue = [T.root()]
    hueco_encontrado = False

    while queue:
        node = queue.pop(0)

        # Revisar hijo izquierdo
        left_child = T.left(node)
        if left_child is not None:
            if hueco_encontrado:
                return False
            queue.append(left_child)
        else:
            hueco_encontrado = True

        # Revisar hijo derecho
        right_child = T.right(node)
        if right_child is not None:
            if hueco_encontrado:
                return False
            queue.append(right_child)
        else:
            hueco_encontrado = True

    return True



def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    # 1. Obtener ancestros de p (de p hacia la raíz)
    path_p = []
    curr = p
    while curr is not None:
        path_p.append(curr)
        curr = T.parent(curr)

    # 2. Obtener ancestros de q (de q hacia la raíz)
    path_q = []
    curr = q
    while curr is not None:
        path_q.append(curr)
        curr = T.parent(curr)

    # 3. Revertir para que los caminos vayan de la raíz hacia los nodos
    r_p = path_p[::-1]
    r_q = path_q[::-1]

    # 4. Encontrar el índice donde los caminos divergen (el ancestro común más bajo)
    i = 0
    while i < len(r_p) and i < len(r_q) and r_p[i] == r_q[i]:
        i += 1

    # 'i - 1' es el índice del ancestro común más bajo (LCA)
    # r_p[i-1:] son los nodos desde el LCA hasta p. Los revertimos para ir de p al LCA.
    camino_p_lca = r_p[i-1:][::-1] 

    # r_q[i:] son los nodos debajo del LCA hasta q.
    camino_lca_q = r_q[i:]

    # 5. Combinar los caminos y formatear el string
    camino_total = camino_p_lca + camino_lca_q

    return " -> ".join(str(nodo.element()) for nodo in camino_total)



if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
