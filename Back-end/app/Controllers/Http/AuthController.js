'use strict'
const Database = use('Database')

class AuthController {
    async login ({request,response,auth})
    {

        const {email,password} = request.only(['email','password'])
        const x =  await Database.table('users').where('email', email).first()
        const token = await auth.attempt (email,password)
        return response.ok(token)
    }
    async logout ({response,auth})
    {

       await auth.logout()
        return response.json({
          data: "eliminado"
        })
    }
}

module.exports = AuthController
