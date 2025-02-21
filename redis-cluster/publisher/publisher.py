import redis
import time

# Conectar a Redis a través de HAProxy
redis_client = redis.Redis(host='haproxy', port=6389, decode_responses=True)

while True:
    redis_client.publish('notificaciones', 'Nuevo mensaje en tiempo real')
    print("Mensaje enviado...")
    time.sleep(5)