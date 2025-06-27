# GraphQlQueryJobInput

Required fields for executing a GraphQL query job


## Fields

| Field                                                                               | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `query`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | The GraphQL query to execute                                                        |
| `callback_input`                                                                    | [Optional[models.GraphQlJobCallbackInput]](../models/graphqljobcallbackinput.md)    | :heavy_minus_sign:                                                                  | Input class for providing a callback's url and any headers needed for the callback. |