const http = require('http');

const hostname = '0.0.0.0';
const port = 10000;

const server = http.createServer((req, res) => {
    if (req.method === 'GET') {
        console.log(`GET request received for path: ${req.url}`);
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('GET request logged\n');
    } else if (req.method === 'POST') {
        let body = '';

        req.on('data', chunk => {
            body += chunk.toString(); // Convert Buffer to string
        });

        req.on('end', () => {
            console.log(`POST request received for path: ${req.url}`);
            console.log(`Request body: ${body}`);
            res.writeHead(200, { 'Content-Type': 'text/plain' });
            res.end('POST request logged\n');
        });
    } else {
        res.writeHead(405, { 'Content-Type': 'text/plain' });
        res.end('Method Not Allowed\n');
    }
});

server.listen(port, hostname, () => {
    console.log(`Server listening on http://${hostname}:${port}`);
});
