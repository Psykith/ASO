import redis

# Conectar a Redis a través de HAProxy
redis_client = redis.Redis(host='haproxy', port=6389, decode_responses=True)

# Suscribirse al canal "notificaciones"
pubsub = redis_client.pubsub()
pubsub.subscribe('notificaciones')

print("Esperando mensajes...")
for message in pubsub.listen():
    if message['type'] == 'message':
        print(f"Mensaje recibido: {message['data']}")