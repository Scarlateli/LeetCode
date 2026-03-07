class LRUCache {

    // --- 1. O tijolinho: cada nó guarda chave, valor, e ponteiros ---
    private class Node {
        int key, val;
        Node prev, next;
        Node(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    private int capacity;
    private HashMap<Integer, Node> map;  // chave -> nó (acesso direto)
    private Node head, tail;              // sentinelas (nós falsos)

    // --- 2. Construtor: monta a estrutura vazia ---
    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.map = new HashMap<>();

        // Cria os sentinelas e liga um no outro
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.prev = head;
        // Agora a lista é: head <-> tail (vazia)
    }

    // --- 3. get: busca o valor e move pra frente ---
    public int get(int key) {
        if (!map.containsKey(key)) return -1;  // não existe? -1

        Node node = map.get(key);   // HashMap me leva direto ao nó
        remove(node);               // arranca de onde tá
        insertAfterHead(node);      // coloca como mais recente
        return node.val;
    }

    // --- 4. put: insere/atualiza e faz eviction se necessário ---
    public void put(int key, int value) {
        // Se já existe, remove o antigo primeiro
        if (map.containsKey(key)) {
            remove(map.get(key));
            map.remove(key);
        }

        // Cria nó novo, registra no map, coloca na frente
        Node node = new Node(key, value);
        map.put(key, node);
        insertAfterHead(node);

        // Estourou a capacidade? Remove o LRU (o de trás)
        if (map.size() > capacity) {
            Node lru = tail.prev;    // quem tá logo antes do tail
            remove(lru);
            map.remove(lru.key);     // remove do map também!
        }
    }

    // --- 5. Operações auxiliares na linked list (O(1)) ---

    // Desconecta o nó da lista (pula ele)
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    // Encaixa o nó logo depois do head (posição "mais recente")
    private void insertAfterHead(Node node) {
        node.next = head.next;
        node.prev = head;
        head.next.prev = node;
        head.next = node;
    }
}
