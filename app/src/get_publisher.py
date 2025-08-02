from handler.sns import SnsPublisher
from handler.sqs import SqsPublisher

_instance_cache = {}

_publisher_types = {
    "sns": SnsPublisher,
    "sqs": SqsPublisher,
}

def get_publisher(publisher_type: str):
  if publisher_type not in _instance_cache:

    if publisher_type not in _publisher_types:
      raise ValueError(f"Tipo de publisher não suportado: '{publisher_type}'. " f"Tipos suportados: {', '.join(_publisher_types.keys())}")
    
    publisher_class = _publisher_types[publisher_type]
    print(f"Criando instância de {publisher_class.__name__}")
    _instance_cache[publisher_type] = publisher_class()

  return _instance_cache[publisher_type]