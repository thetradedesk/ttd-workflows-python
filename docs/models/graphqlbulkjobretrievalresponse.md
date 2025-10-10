# GraphQLBulkJobRetrievalResponse

This is the top level class returned to a user when they retrieve a bulk job


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `job`                                                          | [Optional[models.GraphQlBulkJob]](../models/graphqlbulkjob.md) | :heavy_minus_sign:                                             | The response model that mirrors the GQL bulkjob.               |
| `errors`                                                       | *OptionalNullable[str]*                                        | :heavy_minus_sign:                                             | N/A                                                            |