'use strict'

const plantavalidator = require('../app/Validators/plantavalidator');


/** @type {typeof import('@adonisjs/framework/src/Route/Manager')} */
const Route = use('Route')

Route.post('/login','AuthController.login')
Route.post('/users','UserController.store')

Route.group(()=>{
Route.get('/perfil','UserController.Miperfil')
Route.post('/perfil','UserController.Foto')
Route.delete('/perfil','UserController.Delete')
Route.post('/planta','PlantaController.store')
Route.post('/plantafoto/:id','PlantaController.Foto')
Route.get('/misplantas','PlantaController.Misplantas')
Route.delete('/deleteplanta/:id','PlantaController.Delete')
Route.delete('/deletefoto/:id','PlantaController.Deletefoto')
Route.post('/configuracion','ConfiguracionController.store')
Route.get('/verconfiguraciones/:id','ConfiguracionController.ver')
Route.post('/agregarconfiguracion/:id','ConfiguracionController.agregar')
Route.delete('/eliminarconfiguracion/:id','ConfiguracionController.eliminar')
Route.delete('/logout','AuthController.logout')
}).middleware('auth');
