
class Api {
  constructor(apiUrl) {
      this.apiUrl =  apiUrl;
  }
getToken () {
  if (document.getElementsByName('csrfmiddlewaretoken').length > 0) {
    return document.getElementsByName('csrfmiddlewaretoken')[0].value    
  } else {
    return ''
  }
}
getPurchases () {
  return fetch(`/purchases`, {
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    }
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
addPurchases (id) {
  return fetch(`/purchases`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    },
    body: JSON.stringify({
      id: id
    })
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
removePurchases (id){
  return fetch(`/purchases/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    }
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
addSubscriptions(id) {
  return fetch(`/api/subscriptions/${id}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    },
    body: JSON.stringify({
      id: id
    })
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
removeSubscriptions (id) {
  return fetch(`/api/subscriptions/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    }
  })
    .then( e => {
        if(e.ok) {
            return e.json()
        }
        return Promise.reject(e.statusText)
    })
}
addFavorites (id)  {
  return fetch(`/favorites`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    },
    body: JSON.stringify({
      id: id
    })
  })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
}
removeFavorites (id) {
  return fetch(`/favorites/${id}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': this.getToken()
    }
  })
      .then( e => {
          if(e.ok) {
              return e.json()
          }
          return Promise.reject(e.statusText)
      })
}
  getIngredients  (text)  {
      return fetch(`/ingredients?search=${text}`, {
          headers: {
              'Content-Type': 'application/json'
          }
      })
          .then( e => {
              if(e.ok) {
                  return e.json()
              }
              return Promise.reject(e.statusText)
          })
  }
}
