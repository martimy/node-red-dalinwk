module.exports = function(RED) {
    function RuuviAdapterNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            // expects the msg.payload to be as JSON-formatted string 
            var jmsg = JSON.parse(msg.payload);
            var msg1 = {payload: jmsg.temperature};
            var msg2 = {payload: jmsg.humidity};
            var msg3 = {payload: jmsg.pressure};
            var msg4 = {payload: jmsg.acceleration};
            var msg5 = {payload: jmsg.battery};
            
            node.send([msg1, msg2, msg3, msg4, msg5]);
        });
    }
    RED.nodes.registerType("ruuvi-adapter",RuuviAdapterNode);
}
