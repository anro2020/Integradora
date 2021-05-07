const Env = use('Env')

module.exports = {
  url: Env.get('MONGO_URL', 'mongodb+srv://admin:admin@cluster0.jaq7d.mongodb.net/test?retryWrites=true&w=majority'),
  host: Env.get('MONGO_HOST', ''),
  port: Env.get('MONGO_PORT', ''),
  user: Env.get('MONGO_USER', ''),
  pass: Env.get('MONGO_PASS', ''),
  db: Env.get('MONGO_DATABASE', '')
}
