
'use strict'

const { incrementing } = require("@adonisjs/lucid/src/Lucid/Model")
const autoIncrement = require('mongoose-auto-increment');
const mongooseLeanGetters = require('mongoose-lean-getters');
const mongoose = use('Mongoose')
const ObjectId = mongoose.Schema.Types.ObjectId
const Mixed = mongoose.Schema.Types.Mixed



let Configuraciones = mongoose.Schema({
   User_id: { type: Number, default: '' },
   temperatura_ambiente: { type: Number, default: '' },
  configuraciones: [{ type: Mixed, default: {} }],

}, {
  timestamps: true
})

module.exports = mongoose.model('test', Configuraciones)

