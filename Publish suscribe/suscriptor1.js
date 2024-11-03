const mqtt = require('mqtt')
const client = mqtt.connect('mqtt://localhost')

client.on('connect', () => {
    client.subscribe('topic/test')
    console.log('El suscriptor está conectado al topic.');
})

client.on('message', (topic, message) => {
    console.log(`Mensaje recibido en ${topic}: ${message.toString()}`)
})
