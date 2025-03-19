# GraphQLQueryInput

Required fields for executing a GraphQL query


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `query`                                                      | *str*                                                        | :heavy_check_mark:                                           | The GraphQL query to execute.                                |
| `variables`                                                  | [OptionalNullable[models.Variables]](../models/variables.md) | :heavy_minus_sign:                                           | Variables to substitute into the query.                      |