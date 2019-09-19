from flask import Flask
import redis

app = Flask(__name__)


@app.route('/')
def hello():
    redis_client = redis.Redis(host="redis-server" , port= 6379)
    count = 1

    if redis_client.exists("Counter") == 0:
        redis_client.set("Counter" , count)
    else:
        count = int(redis_client.get("Counter")) + 1
        redis_client.set("Counter" , count)

    return "You have visited " + str(count) + " times !"

if __name__ == '__main__':
    app.run(host = '0.0.0.0' , port = 5000 , debug= True)