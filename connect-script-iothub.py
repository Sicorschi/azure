from paho.mqtt import client as mqtt
from azure.iot.device import IoTHubDeviceClient, MethodResponse, X509
import ssl
import certifi

root_cert_file = "rootca/certs/rootca.pem"
cert_file = "rootca/certs/sensor1.pem"
key_file = "rootca/sensor1.key"
device_id = "sensor1"
iot_hub_name = "sngular-iot-hub"
messages_to_send = 12
count_messages = 0

print(certifi.where())


def on_connect(client, userdata, flags, rc):
    print("=======" + str(device_id) + "========" + "SUCCESSFULLY CONNECTED======with result code: " + str(rc))

def on_disconnect(client, userdata, rc):
    print("======" + str(device_id) + "========" + "IS DISCONNECTED========with result code: " + str(rc))

def on_publish(client, userdata, mid):
    print("======" + str(device_id) +  "======" + "SENDING DATA=======" + str(mid))

client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# Set the username but not the password on your client
client.username_pw_set(username=iot_hub_name+".azure-devices.net/" +
                       device_id + "/?api-version=2021-04-12", password=None)

# Set the certificate and key paths on your client
client.tls_set(ca_certs=certifi.where(), certfile=cert_file, keyfile=key_file,
              cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None, keyfile_password="sngular")

# Connect as before
client.connect(iot_hub_name+".azure-devices.net", port=8883)

while count_messages < messages_to_send:
  count_messages += 1
  client.publish("devices/" + device_id + "/messages/events/", '{"status": 200, "msg": Hello from sensor1 device}', qos=1)
client.loop_forever()

