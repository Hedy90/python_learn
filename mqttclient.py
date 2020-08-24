# encoding: utf-8
import paho.mqtt.client as mqtt
import json
import time
import struct
# Client对象构造
MQTTHOST = "EQQ95JJDEA.iotcloud.tencentdevices.com"
MQTTPORT = 1883
mqttClient = mqtt.Client("EQQ95JJDEAjinanpoc")
mqttClient.username_pw_set("EQQ95JJDEAjinanpoc;12010126;YZKIZ;1621055945", "ee916b35de849545b0e28e554d18b17ab37a2bc35c2fab50fcf6740c6edc3288;hmacsha256")


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()

# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)

# 消息处理函数
def on_message_come(client, userdata, msg):

    print(msg.topic + " " + ":" + str(msg.payload))


# subscribe 消息
def on_subscribe():
    # 订阅监听自定义Topic
    mqttClient.subscribe("EQQ95JJDEA/jinanpoc/control", 1)
    mqttClient.on_message = on_message_come # 消息到来处理函数


def main():
    on_mqtt_connect()
    # 自定义Topic消息上行
    on_publish("EQQ95JJDEA/jinanpoc/event", "hello world！", 1)
    # 系统属性Topic消息上行
    # on_publish("/sys/********/pythondevice2/thing/event/property/post", "{\"method\":\"thing.service.property.set\",\"id\":\"1745506903\",\"params\":{\"Status\":1},\"version\":\"1.0.0\"}", 1)
    on_subscribe()
    while True:
        pass

if __name__ == '__main__':
    main()