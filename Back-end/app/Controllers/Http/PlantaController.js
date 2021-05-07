'use strict'
const Planta = use ('App/Models/Planta')
const Database = use('Database')
const Helpers = use('Helpers')

class PlantaController {
  async store({request,response,auth})
{
   const input = request.all()

     await Planta.create(input)


  
      return response.json(
          {
             rer:true,
             message:"registro insertado correctamente"
          }
      )
}
async Foto({request,response,params=id}){


  const avatar = request.file('avatar', {
    types: ['image'],
    size: '10mb'
  });
var nombre ='assets/plantas/'
  const nombreArchivo = params.id + '.' + avatar.extname;
  await avatar.move('../FRONT-END/src/assets/plantas', {
    name: nombreArchivo,
    overwrite: true
  })
    const directorio = await Planta.findOrFail(params.id);
    directorio.url_foto = nombre + nombreArchivo;
    await directorio.save();

    return response.status(200).send({
      res: true,
      message: "Foto registrada correctamente!"
    })
  }

  async Delete({response,auth}){

    const directorio = await Planta.findOrFail(buscador.id);
   directorio.url_foto =null
   await directorio.save();

        return response.json(
            {
               rer:true,
               message:"registro eliminado correctamente"
            }
        )

}
async Misplantas({response,auth}){
  return response.send(await Database
  .table('plantas')
  .where('user_id', auth.user.id)
 )


}
async Deletefoto({response,params=id}){
  const directorio = await Planta.findOrFail(params.id);
 directorio.url_foto =null
 await directorio.save();

      return response.json(
          {
             rer:true,
             message:"registro eliminado correctamente"
          }
      )

}



async Delete ({response,params=id}){
  const plantae = await Planta.findOrFail(params.id)
  await plantae.delete()

  if (plantae.delete()){
      return response.json(
          {
             rer:true,
             message:"registro eliminado correctamente"
          }
      )
  }
}





}




module.exports = PlantaController
