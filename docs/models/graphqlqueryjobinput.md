# GraphQlQueryJobInput

Fields for executing a GraphQL query job


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `query`                                                                                  | *str*                                                                                    | :heavy_check_mark:                                                                       | The GraphQL query to execute                                                             |
| `callback_input`                                                                         | [Optional[models.GraphQlBulkJobCallbackInput]](../models/graphqlbulkjobcallbackinput.md) | :heavy_minus_sign:                                                                       | Input class for providing a callback's url and any headers needed for the callback.      |
| `beta_features`                                                                          | *OptionalNullable[str]*                                                                  | :heavy_minus_sign:                                                                       | Beta features to be enabled for this GraphQL query (passed as TTD-GQL-Beta header)       |