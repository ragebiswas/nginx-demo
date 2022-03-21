const http = require('http')
const port1 = 3000
const port2 = 3001
const port3 = 3002

const requestHandler = (request, response) => {
  var props = {};
  Object.assign(props, request.headers);
  Object.assign(props, { path: request.url, port: request.socket.localPort });
  console.log(props)
  response.end('hello from server!\n')
}

const server1 = http.createServer(requestHandler)
server1.listen(port1, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }
  console.log(`server1 is listening on ${port1}`)
})

const server2 = http.createServer(requestHandler)
server2.listen(port2, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }
  console.log(`server2 is listening on ${port2}`)
})

const server3 = http.createServer(requestHandler)
server3.listen(port3, (err) => {
  if (err) {
    return console.log('something bad happened', err)
  }
  console.log(`server3 is listening on ${port3}`)
})