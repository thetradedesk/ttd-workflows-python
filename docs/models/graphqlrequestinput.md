# GraphQLRequestInput

Required fields for executing a GraphQL query


## Fields

| Field                                   | Type                                    | Required                                | Description                             |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `request`                               | *str*                                   | :heavy_check_mark:                      | The GraphQL query to execute.           |
| `variables`                             | Dict[str, *Any*]                        | :heavy_minus_sign:                      | Variables to substitute into the query. |