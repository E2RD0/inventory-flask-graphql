# Respuestas

## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

Una de las principales ventajas de GraphQL es que permite al frontend pedir **solo los datos que necesita**. En una API REST tradicional, a veces terminas recibiendo demasiada información o te ves obligado a hacer varias peticiones para conseguir todo lo que necesitas. Con GraphQL, usamos **una sola petición al endpoint `/graphql`**, y ahí podemos consultar o modificar los productos fácilmente.

Esto también encaja muy bien con un frontend reactivo como Vue, porque se pueden estructurar mejor las peticiones para mantener sincronizado el estado de los datos sin tener que implementar lógica extra.

---

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

En Flask con Graphene (la librería que usamos), los **tipos** se definen como clases que heredan de `graphene.ObjectType`. Básicamente, describen cómo está estructurado un tipo de dato, como por ejemplo un `Product`, con sus campos como `id`, `name`, `stock`, etc.

Por otro lado, los **resolvers** son funciones que se encargan de devolver los datos para cada consulta o mutación. Se pueden definir como métodos con el prefijo `resolve_`, o directamente dentro de las clases que representan queries y mutations. También se pueden usar como métodos `mutate()` dentro de clases que extienden de `graphene.Mutation`.

---

## ¿Por qué es importante que el backend también actualice `disponible`?

Porque si esa lógica solo está en el frontend, se rompe la integridad de los datos. Por ejemplo, si alguien actualiza el stock desde otra app o desde Postman, y no actualiza `disponible`, el sistema podría mostrar datos incorrectos.

Tener esa lógica en el backend garantiza que **todas las fuentes de datos sigan las mismas reglas**. Así nos aseguramos de que si el stock de un producto baja a cero, su disponibilidad cambie automáticamente a `false`, sin depender de que el frontend lo haga.

---

## ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

La lógica está integrada directamente en la mutación que actualiza el stock. Cada vez que se hace un cambio, el backend:

- Se asegura de que el stock no pueda quedar negativo (si baja de cero, se ajusta a cero).
- Actualiza automáticamente el campo `available` (`disponible`) en función del nuevo stock.

De esta forma, **no importa desde dónde se llame la API**, siempre se actualiza correctamente.