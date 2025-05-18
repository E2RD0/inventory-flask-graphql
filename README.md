# API de Inventario con Flask + GraphQL

Backend de inventario construido con Flask y GraphQL.  
Permite consultar, agregar, eliminar y actualizar una lista de productos en memoria.


[Respuestas a preguntas](respuestas.md)

---

## Requisitos

- Python 3.8 o superior  
- pip (gestor de paquetes de Python)

---

## Instalación y Ejecución

```bash
pip install -r requirements.txt
python app.py
```

Una vez ejecutado, la API estará disponible en:

- **GraphQL IDE (GraphiQL):** [http://localhost:5000/graphql](http://localhost:5000/graphql)  
- **Acceso API REST:** se puede enviar peticiones HTTP tipo `POST` al endpoint `/graphql` usando JSON

---

## Cómo usar la API

### Ejemplo de consulta (query):

```graphql
query {
  allProducts {
    id
    name
    price
    stock
    available
  }
}
```

### Actualizar el stock de un producto

#### Ejemplo de mutación:

```graphql
mutation {
  updateStock(productId: 2, quantity: 3) {
    product {
      id
      stock
      available
    }
  }
}
```

## Lógica del Backend

- El backend trabaja con una lista en memoria (`product_data.py`).
- Cada producto tiene:
  - `id` (int)
  - `name` (str)
  - `price` (float)
  - `stock` (int)
  - `available` (bool)
- Al actualizar el stock:
  - Si el stock llega a 0, `available` se pone en `false`.
  - Si el stock sube desde 0, `available` vuelve a `true`.
  - No se permite que el stock sea negativo.