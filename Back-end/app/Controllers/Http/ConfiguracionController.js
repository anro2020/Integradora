'use strict'
const Configuracion = use('App/Models/Configuracion')

class ConfiguracioneController {

async store({response,request})
{
  const config =  request.only(['User_id','temperatura_ambiente','configuraciones'])
  const obj = {
    'configura':config
  }
  const configuracionnn = new Configuracion (config)
  await configuracionnn.save()
  return response.json(
    {
       rer:true,
       message:config
    }
  )

  }
async storeconfig({request,response}){

  const config =  request.only(['configuraciones'])

  const configuracionnn = new Configuracion (config)
  await configuracionnn.save()
  return response.json(
    {
       rer:true,
       message:config
    }
  )
  }

  async ver({response,request,params=id}){
    const id = params.id
    const Configuraciones = await Configuracion.find({'UserID':id})

    return response.json(

        Configuraciones

    )

  }
  async agregar({response,request,params:{id}}){

 const idc = await Configuracion.findOne({User_id:id}).lean()
 const Configuracionn = await Configuracion.findByIdAndUpdate({'_id':idc._id},{$push:{configuraciones:{$each:[request.all()]}}})


return response.json(
  {
        rer:true,
        message:'exito'
     }
    )

}
async eliminar({response,request,params:{id}}){

  const idc = await Configuracion.findOne({User_id:id}).lean()
  const Configuracionn = await Configuracion.findByIdAndUpdate({'_id':idc._id},{$pull:{configuraciones:request.all()}})


 return response.json(
   {
         rer:true,
         message:'exito'
      }
     )

 }
 }


module.exports = ConfiguracioneController


//        await producto.query().where('id',params.id).update(input)

