'use strict'

class plantavalidator {
  get rules () {
    return {
      nombre :'required|max:180',
    }
  }
}

module.exports = plantavalidator
