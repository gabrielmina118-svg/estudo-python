produtos = [
    {
        "nome": "Notebook",
        "preco": 2500,
        "importada": True,
        "estoque": 10,
        "especificacoes": {
            "processador": "Intel i7",
            "ram": "16GB",
            "armazenamento": "512GB SSD",
        },
        "avaliacoes": [
            {"usuario": "Lucas", "nota": 5, "comentario": "Muito rápido"},
            {"usuario": "Fernanda", "nota": 4, "comentario": "Ótimo custo-benefício"},
        ],
    },
    {
        "nome": "Mouse",
        "preco": 150,
        "importada": False,
        "estoque": 50,
        "especificacoes": {"dpi": "1600", "botoes": 6, "sem_fio": True},
        "avaliacoes": [
            {"usuario": "Paulo", "nota": 5, "comentario": "Muito preciso"},
            {
                "usuario": "Juliana",
                "nota": 4,
                "comentario": "Confortável para longas horas",
            },
        ],
    },
    {
        "nome": "Teclado",
        "preco": 300,
        "importada": True,
        "estoque": 20,
        "especificacoes": {"tipo": "Mecânico", "switch": "Red", "iluminacao": "RGB"},
        "avaliacoes": [],
    },
    {
        "nome": "Monitor",
        "preco": 800,
        "importada": False,
        "estoque": 15,
        "especificacoes": {
            "tamanho": "27 polegadas",
            "resolucao": "2K",
            "taxa_atualizacao": "144Hz",
        },
        "avaliacoes": [
            {"usuario": "Rafael", "nota": 5, "comentario": "Imagem perfeita"},
            {"usuario": "Patrícia", "nota": 4, "comentario": "Vale cada centavo"},
        ],
    },
    {
        "nome": "Impressora",
        "preco": 600,
        "importada": True,
        "estoque": 5,
        "especificacoes": {
            "tipo": "Laser",
            "velocidade": "30 ppm",
            "conectividade": "Wi-Fi",
        },
        "avaliacoes": [
            {"usuario": "Marcos", "nota": 4, "comentario": "Impressão rápida e nítida"},
            {"usuario": "Aline", "nota": 3, "comentario": "Toner caro para repor"},
        ],
    },
    {
        "nome": "Headset",
        "preco": 450,
        "importada": True,
        "estoque": 30,
        "especificacoes": {"conexao": "USB", "microfone": True, "som": "7.1 Surround"},
        "avaliacoes": [
            {"usuario": "João", "nota": 5, "comentario": "Excelente qualidade"},
            {"usuario": "Maria", "nota": 4, "comentario": "Muito confortável"},
        ],
    },
    {
        "nome": "Webcam",
        "preco": 350,
        "importada": False,
        "estoque": 25,
        "especificacoes": {"resolucao": "1080p", "fps": 60, "autofoco": True},
        "avaliacoes": [
            {"usuario": "Carlos", "nota": 5, "comentario": "Imagem nítida"},
            {"usuario": "Ana", "nota": 3, "comentario": "Software deixa a desejar"},
        ],
    },
]


produtos_avaliadores =[
    {
        'nomeProduto': produto.get('nome'),
        'avaliadores': [avaliador_nome['usuario'] for avaliador_nome in produto['avaliacoes']]
    }
    for produto in produtos
]
print(produtos_avaliadores)
