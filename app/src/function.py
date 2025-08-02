import get_publisher

PUBLISHER_MAP = {
    "arn:...TabelaDePedidos...": "sns",
    "arn:...TabelaDeUsuarios...": "sqs",
    "arn:...TabelaDePagamentos...": "sns",
}


def handler(event):
  for record in event["Records"]:
    arn = record["eventSourceARN"]
    pub_type = PUBLISHER_MAP.get(arn)

    if not pub_type:
        print(f"ARN sem tipo de publisher mapeado: {arn}")
        continue

    publisher = get_publisher(pub_type)

    new_image = record["dynamodb"].get("NewImage", {})
    if new_image:
        data = {k: list(v.values())[0] for k, v in new_image.items()}
        publisher.send(data)

