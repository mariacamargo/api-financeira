# API Financeira

API REST desenvolvida em **Python + Flask** para extração de dados de **ações** e **moedas** em tempo real.

## Funcionalidades

- Consultar cotação de ações (via Yahoo Finance)
- Consultar cotação de moedas (via AwesomeAPI)
- Retornar dados atualizados em formato JSON

## Estrutura do Projeto
```
api-financeira/
│
├── app.py                # API principal
├── services/
│   ├── yahoo_service.py  # Funções para buscar dados no Yahoo Finance
│   └── currency_service.py  # Funções para moedas (API externa)
│
├── requirements.txt
└── README.md
```

## Instalação e Execução

```bash
# Criar ambiente virtual (opcional)
python -m venv venv
venv\Scripts\activate   # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar o servidor
python app.py
```

## Endpoints

### Status da API
`GET /`  
Retorna mensagem de status.

### Cotação de Ação
`GET /api/stock/<ticker>`  
Exemplo: `/api/stock/PETR4.SA`

### Cotação de Moeda
`GET /api/currency/<pair>`  
Exemplo: `/api/currency/USD-BRL`

## Tecnologias Utilizadas
- Python 3.10+
- Flask
- yfinance
- requests

## Exemplos de Retorno

### Ações
```json
{
  "ticker": "PETR4.SA",
  "price": 37.24,
  "open": 36.90,
  "high": 37.45,
  "low": 36.70,
  "volume": 25896300
}
```

### Moedas
```json
{
  "pair": "USD-BRL",
  "name": "Dólar/Real",
  "bid": "5.10",
  "ask": "5.11",
  "variation": "-0.15",
  "updated_at": "2025-10-16 12:00:00"
}
```


Feito por Maria Neiva
