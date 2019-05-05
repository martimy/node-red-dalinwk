module.exports = function(RED) {
    function RuuviScanNode(config) {
        RED.nodes.createNode(this,config);
        this.mac = config.mac;
        this.timeout = config.timeout;
        var node = this;

        node.on('input', function(msg) {

            const { spawn } = require('child_process');
            const py = spawn("python", ['/home/pi/node-red-dalinwk/node-inwk/get_tag_data.py', this.mac, this.timeout]);

            //setTimeout(function(){ py.kill()}, this.timeout);

            py.stdout.on('data', function(data){
              msg.payload = data.toString();
              node.send(msg);
            });
  
        });
    }
    RED.nodes.registerType("ruuvi-scan",RuuviScanNode);
}




