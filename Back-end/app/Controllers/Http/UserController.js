'use strict'
const User = use ('App/Models/User')
const Database = use('Database')
const Helpers = use('Helpers')

class UserController {
async store({request,response})
{

    const userData = request.only(['nombre','email','password'])
    const user = await User.create(userData)

    return response.created({
        status : true,
        data : user
    })

}
async Miperfil({response,auth}){
  return response.send([await Database
  .table('users')
  .where('id', auth.user.id)
  .first()])


}
async Foto({request,response,auth}){
    const avatar = request.file('avatar', {
      types: ['image'],
      size: '10mb'
    });
var nombre ='assets/'
    const nombreArchivo = auth.user.id + '.' + avatar.extname;
    await avatar.move('../FRONT-END/src/assets', {
      name: nombreArchivo,
      overwrite: true
    })
      const directorio = await User.findOrFail(auth.user.id);
      directorio.url_foto = nombre+nombreArchivo;
      await directorio.save();

      return response.status(200).send({
        res: true,
        message: "Foto registrada correctamente!"
      })
    }

    async Delete({response,auth}){
      const directorio = await User.findOrFail(auth.user.id);
     directorio.url_foto =null
     await directorio.save();

          return response.json(
              {
                 rer:true,
                 message:"registro eliminado correctamente"
              }
          )

  }
  }

module.exports = UserController
